# The structure of major folder in project
<pre>
____________________________________________________________
|                                                          |
|client/src/py                                             |
|contracts                                                 |
|iroha/irohad/consensus && iroha/iroha-cli                 |
|library/sumo/tool                                         |
|migrations                                                |
|simulation/data && simulation/script                      |
|test                                                      |
|__________________________________________________________|
</pre>

# I Install wallet application, smart contract compiler and web environment
## 1.1. Download Ganache wallet
Ganache wallet ignored consensus algorithm. To install hyperledger with consensus algorithm, go to **II. Build iroha hyperledger**
Ganache GUI: https://trufflesuite.com/ganache/ 

Download Ganache CLI
```
npm i ganache
```

Launching Ganache CLI
```
ganache
```
Note: all commands can run anywhere

## 1.2. Install smart contract compiler
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
Note: all commands run start at folder path /project-vanet-blockchain

## 1.3. Install web environment
Install react application with npm
```
npm install create-react-app
```

Install web3 
```
npm install web3
```


# II. Build simulated environment and statistic data
## 2.1. Download sumo and config environment variable  
Operating System: Ubuntu 20.04 LTS
```
$ sudo apt install git
$ git clone https://github.com/eclipse/sumo
$ cd
$ export SUMO_HOME=”$PWD/sumo”
$ mkdir sumo/build/cmake-build
$ cd sumo/build/cmake-build
$ sudo apt install python3-dev
$ cmake ../..
$ make -j8
$ cd 
$ nano ~/.bashrc
=> export PATH=$PATH:/home/sumo/bin
=> export SUMO_HOME=/home/sumo
$ source .bashrc
```
Note: all commands run start at ~

## 2.2. Statistic data
To statistic data of proof of driving algorithm, we used file py_main.py at folder simulation/script to do it. <br/>
To running simulation if you have another scenarios with data, go to file py_main.py to change argument of the parameter <br/>

# III. Build Iroha hyperledger
## 3.1. In Ubuntu

### 3.1.1. Install environment dependences on Linux 
```
$ cd ~
$ sudo apt-get update
$ sudo apt-get -y --no-install-recommends install 
$ sudo apt-get install build-essential ninja-build 
$ sudo apt-get install git ca-certificates tar curl unzip cmake
$ sudo apt-get install pkg-config zip
```

### 3.1.2. Install go 
Go version must match with version in file project-vanet-blockchain/iroha/goSrc/src/vmCaller/go.mod.in
```
$ curl -OL https://golang.org/dl/go1.14.linux-amd64.tar.gz
$ sha256sum go1.14.linux-amd64.tar.gz
$ sudo tar -xvf go1.14.linux-amd64.tar.gz
$ sudo nano ~/.bashrc
=> export PATH=$PATH:/usr/local/go/bin
$ source ~/.bashrc
```

### 3.1.3. Install grpc
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
Note: all commands run start at ~
### 3.1.4. Install postgresql and set password
```
$ sudo apt install postgresql postgresql-contrib
$ sudo -i -u postgres
$ psql
$ postgres=# \password 
```
Note: all commands can run anywhere
### 3.1.5. Install Vcpkg Dependency Manager
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
Note: all commands run start at project-vanet-blockchain/iroha
### 3.1.6. Building Iroha
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