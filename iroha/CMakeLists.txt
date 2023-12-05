# Copyright Soramitsu Co., Ltd. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.14.0)

# tìm kiếm chương trình ccache trong hệ thống và gán đường dẫn của nó cho biến CCACHE_PROGRAM
find_program(CCACHE_PROGRAM ccache)
# nếu ccache được tìm thấy trong hệ thống
if(CCACHE_PROGRAM) 
  # sets the RULE_LAUNCH_COMPILE property to the path of the ccache program stored in the CCACHE_PROGRAM variable. 
  # when CMake compiles source code, it will use ccache as a wrapper to cache and accelerate the compilation process.
  set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE "${CCACHE_PROGRAM}")
  # tạo thông điệp hiển thị trạng thái
  message(STATUS "ccache enabled (${CCACHE_PROGRAM})")
endif()

# khởi tạo project iroha với version và và ngôn ngữ C and C++
PROJECT(iroha
  VERSION 1.6.0
  LANGUAGES C CXX)
# đặt C++ standard -> C++ 17
SET(CMAKE_CXX_STANDARD 17) 

# position-independent code (PIC)  enabled when building shared libraries.
SET(CMAKE_POSITION_INDEPENDENT_CODE TRUE)

# checks if the current compiler is not Microsoft Visual C++ (MSVC)
if (NOT MSVC)
  # -Wall asks the compiler to report issues in the code as many as possible
  # -fdiagnostics-color=always"  colorized output for compiler diagnostics (warnings and errors) -> easy to read in terminal
  SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -fdiagnostics-color=always")
  #  -03 tối ưu hoá biên dịch tích cực -> đạt hiệu suất tối đa
  # -Wno-error=deprecated-declarations vô hiệu hoá các cảnh báo lỗi về deprecated declarations (các khai báo không được dùng nữa) -> chỉ hiện warning
  SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -O3 -Wno-error=deprecated-declarations")
  # -g bao gồm các thông tin gỡ lỗi ở trong mã đã được biên dịch -> dễ dàng hơn để debug với debugger
  # -Wextra: It enables additional compiler warnings beyond those enabled by -Wall.
  # -Wno-unused-parameter disables warnings about unused function parameters
  # Wno-deprecated-declarations disables treating deprecated declarations as errors. (similar to the release build)
  SET(CMAKE_CXX_FLAGS_DEBUG   "${CMAKE_CXX_FLAGS_DEBUG} -g -Wextra -Wno-unused-parameter -Wno-deprecated-declarations -O0")
else()
  # adds the /bigobj option to the compilation options
  add_compile_options(/bigobj)
endif()

# instructs CMake to replace the standard file extension of C++ object files from .o to .obj.
SET(CMAKE_CXX_OUTPUT_EXTENSION_REPLACE 1)

# CMAKE_INSTALL_RPATH variable specifies the runtime library search path (rpath) for installed binaries. 
SET(CMAKE_INSTALL_RPATH "../lib")

# enables the generation of a compile_commands.json file, which contains compilation information for source files. 
SET(CMAKE_EXPORT_COMPILE_COMMANDS ON)  ## use for code static analyze and vscode cpp plugin

#  check if the CMake build type is set to "Release."  "Release" is used for optimized, production-ready builds.
if(CMAKE_BUILD_TYPE MATCHES "Release")
  # This module contains functions for checking if the compiler supports Interprocedural Optimization (IPO) or Link-Time Optimization (LTO).
  include(CheckIPOSupported)
  # checks whether the compiler supports IPO and stores the result in the lto_supported variable
  # captures any error message in the error variable
  check_ipo_supported(RESULT lto_supported OUTPUT error)
  # checks if IPO is supported.
  if(lto_supported)
    # displays a status message indicating that IPO/LTO is enabled.
    message(STATUS "IPO / LTO enabled")
    # indicating that Link-Time Optimization (LTO) should be enabled for the project.
    # LTO  optimizes the entire program during the linking phase.
    set(CMAKE_INTERPROCEDURAL_OPTIMIZATION TRUE)
  else()
    # If IPO is not supported, this section is executed.
    message(STATUS "IPO / LTO not supported: <${error}>")
  endif()
endif()

## FIXME revert this after change CI to GitHub actions.
## Temporal fix for 'bytecode stream version incompatible' between gcc-9 and gcc-10 and clang
## when dependancies were build via vcpkg with default GCC9 could not be linked with iroha built with GCC-10
set(CMAKE_INTERPROCEDURAL_OPTIMIZATION FALSE)

if(WIN32)
    # We have to set _WIN32_WINNT for gRPC
    if(${CMAKE_SYSTEM_VERSION} EQUAL 10) # Windows 10
        add_definitions(-D _WIN32_WINNT=0x0A00)
    elseif(${CMAKE_SYSTEM_VERSION} EQUAL 6.3) # Windows 8.1
        add_definitions(-D _WIN32_WINNT=0x0603)
    elseif(${CMAKE_SYSTEM_VERSION} EQUAL 6.2) # Windows 8
        add_definitions(-D _WIN32_WINNT=0x0602)
    elseif(${CMAKE_SYSTEM_VERSION} EQUAL 6.1) # Windows 7
        add_definitions(-D _WIN32_WINNT=0x0601)
    elseif(${CMAKE_SYSTEM_VERSION} EQUAL 6.0) # Windows Vista
        add_definitions(-D _WIN32_WINNT=0x0600)
    else() # Windows XP (5.1)
        add_definitions(-D _WIN32_WINNT=0x0501)
    endif()
endif()

# workaround to prevent user-installed dependencies having higher precedence (chặn các dependenicies do người dùng cài đặt có quyền ưu tiên cao hơn)
# than the ones downloaded with externalproject
if(UNIX)
  list(APPEND CMAKE_C_IMPLICIT_INCLUDE_DIRECTORIES
    /usr/local/include
    )
  list(APPEND CMAKE_CXX_IMPLICIT_INCLUDE_DIRECTORIES
    /usr/local/include
    )
endif()

#  checks whether the COVERAGE variable is defined
if(COVERAGE)
  # find the lcov program on the system (lcov is a tool used for collecting code coverage information.)
  find_program(LCOV_PROGRAM lcov)
  if(NOT LCOV_PROGRAM)
    # If lcov is not found, error message is displayed, and the build process is aborted.
    message(FATAL_ERROR "lcov not found! Aborting...")
  endif()
  # locate an lcov configuration file (.lcovrc) in the project's source directory 
  find_file(LCOV_CONFIG_FILE .lcovrc ${PROJECT_SOURCE_DIR})
  # If the configuration file is not found,
  if(NOT LCOV_CONFIG_FILE)
    # a fatal error message is displayed, and the build process is aborted.
    message(FATAL_ERROR "lcov config file not found in project root! Aborting...")
  endif()
  # message indicates that code coverage with lcov is enabled and specifies the path to the lcov program
  message(STATUS "lcov enabled (${LCOV_PROGRAM})")
  # remove -g flag to reduce binary size
  list(REMOVE_ITEM CMAKE_CXX_FLAGS -g)
  # CMake generates a compile_commands.json file during the build process.this JSON contains information about how each source file is compiled, including compiler flags and source file paths. 
  set(CMAKE_EXPORT_COMPILE_COMMANDS "ON")
  # --coverage flags: the compiler instruments the code to collect information about which parts of the code are executed during the program's runtime (for CXX)
  set(CMAKE_CXX_FLAGS "--coverage ${CMAKE_CXX_FLAGS}")
  # It enables code coverage analysis for C code.
  set(CMAKE_C_FLAGS "--coverage ${CMAKE_C_FLAGS}")
  # Appends the --coverage flag to the CMAKE_SHARED_LINKER_FLAGS variable, ensures that they are also built with code coverage instrumentation.
  set(CMAKE_SHARED_LINKER_FLAGS "--coverage ${CMAKE_SHARED_LINKER_FLAGS}")
  # appends the --coverage flag to the CMAKE_EXE_LINKER_FLAGS, ensures that executables are linked with code coverage support. 
  set(CMAKE_EXE_LINKER_FLAGS "--coverage ${CMAKE_EXE_LINKER_FLAGS}")
  
  # defines a custom target named "coverage.init.info."
  # A custom target in CMake is a build target that you can invoke explicitly. This target is used for initializing the code coverage data collection.
  add_custom_target(coverage.init.info
      # specifies the command that should be executed when this target is built
      # ${LCOV_PROGRAM} is a variable containing the path to the lcov program.
      # --config-file ${LCOV_CONFIG_FILE} specifies the path to an lcov configuration file.
      # -o ${PROJECT_BINARY_DIR}/reports/coverage.init.info sets the output file for coverage initialization data.
      # -c specifies that the coverage data should be captured.
      # -i is used to initialize the coverage data.
      # -d ${PROJECT_BINARY_DIR} specifies the directory for source files to be instrumented.
      COMMAND ${LCOV_PROGRAM} --config-file ${LCOV_CONFIG_FILE} -o ${PROJECT_BINARY_DIR}/reports/coverage.init.info -c -i -d ${PROJECT_BINARY_DIR}
      )
  add_custom_target(coverage.info     
      COMMAND ${LCOV_PROGRAM} --config-file ${LCOV_CONFIG_FILE} -o ${PROJECT_BINARY_DIR}/reports/coverage.info -c -d ${PROJECT_BINARY_DIR}
      COMMAND ${LCOV_PROGRAM} --config-file ${LCOV_CONFIG_FILE} -o ${PROJECT_BINARY_DIR}/reports/coverage.info -a ${PROJECT_BINARY_DIR}/reports/coverage.init.info -a ${PROJECT_BINARY_DIR}/reports/coverage.info
      COMMAND ${LCOV_PROGRAM} --config-file ${LCOV_CONFIG_FILE} -o ${PROJECT_BINARY_DIR}/reports/coverage.info -r ${PROJECT_BINARY_DIR}/reports/coverage.info '/usr*' '/Library/Developer/CommandLineTools/*' '${PROJECT_BINARY_DIR}/*' '${CMAKE_BINARY_DIR}/*' '${CMAKE_SOURCE_DIR}/test/*'
      )
  # sets the REPORT_DIR variable to the path where code coverage reports will be generated. The variable is set to a directory within the build directory (CMAKE_BINARY_DIR) called "reports."
  set(REPORT_DIR ${CMAKE_BINARY_DIR}/reports)
  # This command creates the directory specified by REPORT_DIR if it does not already exist. This directory is where the coverage reports will be stored.
  file(MAKE_DIRECTORY ${REPORT_DIR})
  # includes an external CMake script, cmake/analysis.cmake
  include(cmake/analysis.cmake)
endif()
include(cmake/functions.cmake)
# checks if the SANITIZE_THREAD variable is defined. If it is defined, it means that the Thread Sanitizer (TSan) should be enabled for dynamic analysis of multithreaded code
if(SANITIZE_THREAD)
  # appends the -fsanitize=thread compiler flag. This flag instructs the compiler to enable the Thread Sanitizer. TSan helps detect data races and other threading issues in a program.
  append_build_flags(-fsanitize=thread)
endif()
#  checks if the SANITIZE_ADDRESS variable is defined. If it is defined, it means that the AddressSanitizer (ASan) should be enabled for dynamic memory error detection.
if(SANITIZE_ADDRESS)
  # appends two compiler flags:
  # -fsanitize=address enables AddressSanitizer, which detects memory errors like buffer overflows and use-after-free.
  # -fno-omit-frame-pointer ensures that frame pointers are not omitted, which is needed for better error reporting in AddressSanitizer.
  append_build_flags(-fsanitize=address -fno-omit-frame-pointer)
endif()
# checks if the SANITIZE_MEMORY variable is defined.
if(SANITIZE_MEMORY)
  #  append two complier flags
  # -fsanitize=memory enables MemorySanitizer, which detects uninitialized memory reads.
  # -fsanitize-memory-track-origins enables the tracking of origins for memory accesses, which provides more detailed error reports when using MemorySanitizer.
  append_build_flags(-fsanitize=memory -fsanitize-memory-track-origins)
endif()
# checks if the SANITIZE_UNDEFINED variable is defined. If it is defined, it means that the UndefinedBehaviorSanitizer (UBSan) should be enabled for detecting undefined behavior in the code.
if(SANITIZE_UNDEFINED)
  # appends the -fsanitize=undefined compiler flag. This flag enables UndefinedBehaviorSanitizer, which helps catch various forms of undefined behavior in C and C++ code.
  append_build_flags(-fsanitize=undefined)
endif()

# -DCMAKE_C_COMPILER=${CMAKE_C_COMPILER}: Specifies the C compiler to use for dependencies, ensuring it matches the project's C compiler.
# -DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER}: Sets the C++ compiler for dependencies, matching the project's C++ compiler.
# -DCMAKE_C_FLAGS=${CMAKE_C_FLAGS}: Defines C compiler flags for dependencies, using the project's C compiler flags.
# -DCMAKE_CXX_FLAGS=${CMAKE_CXX_FLAGS}: Specifies C++ compiler flags for dependencies, using the project's C++ compiler flags.
# -G${CMAKE_GENERATOR}: Sets the CMake generator used when configuring dependencies, ensuring consistency with the project's generator.
# -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}: Specifies the build type for dependencies (e.g., "Debug" or "Release"), matching the project's build type.
set(DEPS_CMAKE_ARGS
    -DCMAKE_C_COMPILER=${CMAKE_C_COMPILER}
    -DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER}
    -DCMAKE_C_FLAGS=${CMAKE_C_FLAGS}
    -DCMAKE_CXX_FLAGS=${CMAKE_CXX_FLAGS}
    -G${CMAKE_GENERATOR}
    -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
    )
#  sets the CMAKE_MODULE_PATH to a subdirectory named "cmake/Modules" relative to the location of the CMakeLists.txt file.
SET(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake/Modules)

#  configuration choice for a CMake-based project
option(BENCHMARKING          "Build benchmarks"                         OFF)
option(TESTING               "Build tests"                              ON )
option(USE_BTF               "Build Binary Testing Framework"           OFF)
option(COVERAGE              "Enable coverage"                          OFF)
option(FUZZING               "Build fuzzing binaries"                   OFF)
option(PACKAGE_ZIP           "Create ZIP package"                       OFF)
option(PACKAGE_TGZ           "Create TGZ package"                       OFF)
option(PACKAGE_RPM           "Create RPM package"                       OFF)
option(PACKAGE_DEB           "Create DEB package"                       OFF)
option(USE_LIBURSA           "Use Hyperledger Ursa cryptography"        OFF)
option(USE_BURROW            "Use Hyperledger Burrow EVM"               OFF)
option(SANITIZE_THREAD       "Build with thread sanitizer"              OFF)
option(SANITIZE_ADDRESS      "Build with address sanitizer"             OFF)
option(SANITIZE_MEMORY       "Build with memory sanitizer"              OFF)
option(SANITIZE_UNDEFINED    "Build with undefined behaviour sanitizer" OFF)

# checks whether the CMAKE_BUILD_TYPE variable is not already set.
# CMAKE_BUILD_TYPE is a CMake variable used to specify the build configuration (e.g., "Debug," "Release").
if (NOT CMAKE_BUILD_TYPE)
  # set it to "Debug" as a default build type.
  SET(CMAKE_BUILD_TYPE Debug)
endif()

# checks if the CMake generator matches "Make."
# Generators determine the build system used to build the project.
if(CMAKE_GENERATOR MATCHES "Make")
  #  "$(MAKE)" is a variable that refers to the make command, allowing for compatibility with various make-based build systems
  set(MAKE "$(MAKE)")
else()
  # the MAKE variable is set to "make." This is the default make command in many Unix-like systems.
  set(MAKE make)
endif()

#  to print informational messages to the console during the configuration process.
message(STATUS "-DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}")
message(STATUS "-DTESTING=${TESTING}")
message(STATUS "-DUSE_BTF=${USE_BTF}")
message(STATUS "-DBENCHMARKING=${BENCHMARKING}")
message(STATUS "-DFUZZING=${FUZZING}")
message(STATUS "-DCOVERAGE=${COVERAGE}")
message(STATUS "-DPACKAGE_ZIP=${PACKAGE_ZIP}")
message(STATUS "-DPACKAGE_TGZ=${PACKAGE_TGZ}")
message(STATUS "-DPACKAGE_RPM=${PACKAGE_RPM}")
message(STATUS "-DPACKAGE_DEB=${PACKAGE_DEB}")
message(STATUS "-DSANITIZE_THREAD=${SANITIZE_THREAD}")
message(STATUS "-DSANITIZE_ADDRESS=${SANITIZE_ADDRESS}")
message(STATUS "-DSANITIZE_MEMORY=${SANITIZE_MEMORY}")
message(STATUS "-DSANITIZE_UNDEFINED=${SANITIZE_UNDEFINED}")

# specify the location of schema files used by the project.
set(IROHA_SCHEMA_DIR "${CMAKE_CURRENT_SOURCE_DIR}/schema")
#  specify the location of schema files for the shared model.
set(SM_SCHEMA_DIR "${PROJECT_SOURCE_DIR}/shared_model/schema")
# specify the output directory for schema-related files.
set(SCHEMA_OUT_DIR ${CMAKE_BINARY_DIR}/schema)
#  specify the path for generated Go schema-related file
set(GO_GENERATED_SCHEMA_PATH "${CMAKE_BINARY_DIR}/schema_go")

# specify directories to be included in the project's include path
# allowing source files to access headers from these directories:
include_directories(
  ${PROJECT_SOURCE_DIR}
  ${PROJECT_SOURCE_DIR}/shared_model
  ${PROJECT_SOURCE_DIR}/irohad
  ${PROJECT_SOURCE_DIR}/libs
)

# indicate that the current project is considered the root project in a multi-project CMake configuration. 
#  identify the top-level project when multiple projects are configured together.
SET(IROHA_ROOT_PROJECT ON)

# Boost uses RTTI to perform some actions (such as type erasure).
# This is slow. This flag forces boost to use other methods,
# which are generally faster
add_definitions(-DBOOST_NO_RTTI)

include(FeatureSummary)
include(cmake/dependencies.cmake)
include(cmake/clang-cxx-dev-tools.cmake)


# includes a CMake script named "release.cmake" if any of the PACKAGE is set to ON
if(PACKAGE_TGZ OR PACKAGE_ZIP OR PACKAGE_RPM OR PACKAGE_DEB)
  include(cmake/release.cmake)
endif()

#  include and build  subdirectories in a CMake project
add_subdirectory(schema)
if(USE_BURROW)
  add_subdirectory(goSrc/src/vmCaller)
endif()
add_subdirectory(libs)
add_subdirectory(irohad)
add_subdirectory(iroha-cli)
add_subdirectory(iroha-lib)
add_subdirectory(shared_model)

if(TESTING)
  enable_testing()
  add_subdirectory(test)
endif()
