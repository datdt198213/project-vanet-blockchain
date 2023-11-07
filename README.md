The process of setting up Ganache and utilizing JavaScript to simulate blockchain technology for testing purposes.

## 1. Setting environment

##### Download node version LTS: https://nodejs.org/en/download

## 2. Setting up Ganache

##### Download Ganache GUI version: https://trufflesuite.com/ganache/ 

##### Download Ganache CLI version 
```
npm i ganache
```

##### Launching Ganache CLI
```
ganache
```

## 3. Initialized project reactjs
##### Install create-react-app to initalized reactjs project 
```
npm install create-react-app
```

##### Install web3 
```
npm install web3
```

##### Initialize project reactjs 
```
npx create-react-app client
```


## 4. Install, Init, Compile, Migrate, Test, Deploy Truffle

##### Install truffle
```
npm install truffle
```

##### Initial truffle
```
truffle init
```

##### Compile truffle 
```
truffle compile
```

##### Migrate truffle 
```
truffle migrage
```

##### Reset truffle 
```
truffle migrate reset
```

##### Test truffle 
```
truffle test
```

##### Deploy truffle 
```
truffle deploy
```


# II. Build Iroha hyperledger
# A. In Ubuntu
## 1. Install golang
```
$ cd ~
$ curl -OL https://golang.org/dl/go1.16.7.linux-amd64.tar.gz
$ sha256sum go1.16.7.linux-amd64.tar.gz
$ sudo tar -C /usr/local -xvf go1.16.7.linux-amd64.tar.gz
$ sudo nano ~/.bashrc
$ export PATH=$PATH:/usr/local/go/bin
$ source ~/.bashrc
$ go version
```

## 2. Install environment dependences on Linux 
```
$ sudo apt-get update
$ sudo apt-get -y --no-install-recommends install 
$ sudo apt-get install build-essential ninja-build 
$ sudo apt-get install git ca-certificates tar curl unzip cmake
$ sudo apt-get install pkg-config zip
$ go get github.com/golang/protobuf/protoc-gen-go
$ git clone --recurse-submodules -b v1.58.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc
$ cd grpc
$ mkdir -p cmake/build
$ pushd cmake/build
$ cmake -DgRPC_INSTALL=ON -DgRPC_BUILD_TESTS=OFF ../..
$ make -j 4
$ sudo apt install libsoci-dev
$ pkg-config --cflags --libs soci
```

## 3. Install Vcpkg Dependency Manager
```
$ git clone https://github.com/microsoft/vcpkg.git
$ cd vcpkg
$ ./bootstrap-vcpkg.sh

$ cd ..
$ cmake -DCMAKE_TOOLCHAIN_FILE=$PWD/vcpkg-build/scripts/buildsystems/vcpkg.cmake
$ git clone https://github.com/hyperledger/iroha.git
$ cd iroha
$ ./vcpkg/build_iroha_deps.sh $PWD/vcpkg-build
```

## 4. Building Iroha
1. Build
```
cmake -B build -DCMAKE_TOOLCHAIN_FILE=$PWD/vcpkg-build/scripts/buildsystems/vcpkg.cmake . -DCMAKE_BUILD_TYPE=RELEASE -DUSE_BURROW=ON -DUSE_URSA=OFF -DTESTING=OFF -DPACKAGE_DEB=OFF
```
2. Run
```
cmake --build ./build --target irohad
```
3. Check running result
```
./build/bin/irohad --help
```