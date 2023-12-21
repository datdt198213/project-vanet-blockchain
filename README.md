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

# I. Install environment
## 1.1. Download Ganache wallet
Ganache wallet ignored consensus algorithm. To install hyperledger with consensus algorithm, go to II 
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
**1. Create project blockchain**

Step 1: Initialize project based on npm
```
$ npm init
```

Step 2: install truffle version 5.4.11
```
$ npm install truffle@5.4.11 --save-dev
```

Step 3: Address vulnerabilities
```
$ npm audit fix
```

Step 4: Initialize truffle project
```
$ npx truffle init
```

**2. Deploy code into Ganache**

a. Config network address

```
networkds: {
      ganache :{
        host: "127.0.0.1",     // Localhost (default: none)
        port: 7545,            // Standard Ethereum port (default: none)
        network_id: "*",       // Any network (default: none)
      },
}
```

b. Create file 1_rideshare.js
```
const RideShare = artifacts.require("RideShare");

module.exports = function(deployer) {
    deployer.deploy(RideShare);
}
```

**3. Compile smart contract**
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

# II. Build simulated environment
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

## 2.2. Generate data with proof of driving algorithm
To generate vehicle moving data applying proof of driving algorithm, we used file py_main.py at folder project-vanet-blockchain/simulation/script/ to do it. If you have another scenarios, going to **Category 2.3** <br/>
Run file py_main.py
```
python3 py_main.py
```
Note: this command need to run at folder project-vanet-blockchain/simulation/script
## 2.3. The parameters need to change if having another scenarios.
**insertionRate**: is a number of vehicles which you want to add in simulation, etc. 90 (vehicle) <br/>


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

Interaction with postgres
```
List databases: \l
Acessing a database: \c iroha_default;
List tables: \dt
Select information in a table: SELECT * FROM account;
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
Note: all commands run at project-vanet-blockchain/iroha
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
4. Running iroha
```
build/bin/irohad --config example/config1.sample --genesis_block example/genesis.block --keypair_name example/node0
```
Note: all command run at project-vanet-blockchain/iroha


# IV. Statistic data
After data generates successfully at **category 2.2**, there are several data files added our project including statistic data files containing number of vehicle satisfied proof of driving algorithm conditions, configured simulation files, moving of vehicles files <br/>
Statistic data files
```
project-vanet-blockchain/simulation/data/data_statistic_[number of vehicle].csv
```
```
project-vanet-blockchain/simulation/data/data_test_[number of vehicle].csv
```
Configured simulation files 
```
project-vanet-blockchain/simulation/data/simulation[running times].sumo.cfg
```
Moving of vehicles files
```
project-vanet-blockchain/simulation/data/vehicle[running times].sumo.xml
```