# I Install wallet application, smart contract compiler and 
## 1. Download Ganache wallet
Ganache GUI: https://trufflesuite.com/ganache/ 

Download Ganache CLI
```
npm i ganache
```

Launching Ganache CLI
```
ganache
```

Ganache wallet ignored consensus algorithm. To install hyperledger with consensus algorithm, go to **II. Build iroha hyperledger**

## 2. Install smart contract compiler
This project uses truffle compiler to compile from smart contract written by solidity language to json file including ABI byte code. <br/>
Firstly, installing nodejs at https://nodejs.org/en/download <br/>
Secondly, installing truffle with command
```
npm install truffle
```
To compile smart contract in folder project-vanet-blockchain/contracts, using below command
```
truffle compile
```
Note: all commands run at path folder /project-vanet-blockchain

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
$ cd ~
$ sudo apt-get update
$ sudo apt-get -y --no-install-recommends install 
$ sudo apt-get install build-essential ninja-build 
$ sudo apt-get install git ca-certificates tar curl unzip cmake
$ sudo apt-get install pkg-config zip
```

## 3. Install go 
Go version must match project-vanet-blockchain/iroha/goSrc/src/vmCaller/go.mod.in
```
$ curl -OL https://golang.org/dl/go1.14.linux-amd64.tar.gz
$ sha256sum go1.14.linux-amd64.tar.gz
$ sudo tar -xvf go1.14.linux-amd64.tar.gz
$ sudo nano ~/.bashrc
=> export PATH=$PATH:/usr/local/go/bin
$ source ~/.bashrc
```

## 4. Install grpc
```
$ cd ~
$ git clone --recurse-submodules -b v1.58.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc
$ cd grpc
$ mkdir -p cmake/build
$ pushd cmake/build
$ cmake -DgRPC_INSTALL=ON -DgRPC_BUILD_TESTS=OFF ../..
$ make -j 4
$ sudo apt install libsoci-dev
$ pkg-config --cflags --libs soci
```

## 5. Install postgresql and set password
```
$ sudo apt install postgresql postgresql-contrib
$ sudo -i -u postgres
$ psql
$ postgres=# \password 
```

## 6. Install Vcpkg Dependency Manager
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

## 7. Building Iroha
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