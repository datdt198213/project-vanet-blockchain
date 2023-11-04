#
# Copyright Soramitsu Co., Ltd. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
#

# Đặt đường dẫn đầu ra cho các tệp được thực thi khi sử dụng biến EXECUTABLE_OUTPUT_PATH
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

# Xây dựng các target từ thư mục con interactive
add_subdirectory(interactive)

# Định nghĩa thư viện tĩnh cli-flags_validators có chứa code của validator.cpp
# Gflags config validators
add_library(cli-flags_validators
    validators.cpp
    )

# Liên kết thư viện cli-flags_validators với gflags
target_link_libraries(cli-flags_validators
    gflags
    )

# Định nghĩa thư viện tĩnh client với các file client.cpp, impl/query_response_handler.cpp
# impl/transaction_response_handler.cpp và impl/grpc_response_handler.cpp
add_library(client
    client.cpp
    impl/query_response_handler.cpp
    impl/transaction_response_handler.cpp
    impl/grpc_response_handler.cpp
    )

# Liên kết thư viện client với các thư viện phía dưới nó
target_link_libraries(client
    ed25519_crypto
    grpc_channel_factory
    logger
    RapidJSON::rapidjson
    pb_model_converters
    json_model_converters
    model_generators
    command_client
    query_client
    model_generators
    parser
    model
    )

# Target có tên client sẽ bao gồm thư mục /iroha-cli 
target_include_directories(client PUBLIC
    ${PROJECT_SOURCE_DIR}/iroha-cli
    )

# Định nghĩa và tạo 1 target có tên IrohaCli
add_executable(iroha-cli
    main.cpp
    validators.cpp
    )

# 
target_link_libraries(iroha-cli
    interactive_cli
    model_crypto_provider
    client
    cli-flags_validators
    keys_manager
    Boost::boost
    Boost::filesystem
    logger
    logger_manager
    )

add_install_step_for_bin(iroha-cli)

