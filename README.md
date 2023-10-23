The process of setting up Ganache and utilizing JavaScript to simulate blockchain technology for testing purposes.

# 1. Setting up Ganache:

To begin, we need to install Ganache, a personal Ethereum Blockchain that allows us to simulate blockchain transactions and interactions. Here are the steps to set it up:

### 1.1. Download and Install Ganache:

Visit the official Ganache website and download the appropriate version for your operating system. 
Link download: https://trufflesuite.com/ganache/

### 1.2. Launching Ganache:

After installation, open Ganache and you will be greeted with a user-friendly interface. Ganache provides you with a local Ethereum Blockchain network, complete with pre-funded accounts for testing your Solidity contracts.

# 2. Setting environment

##### Download node version LTS
Link download: https://nodejs.org/en/download

##### Download truffle
```npm install truffle```

# 3. Initialized project

##### Create folder project-vanet-blockchain
```mkdir project-vanet-blockchain```

##### Change directory to folder project-vanet-blockchain and initialize truffle project
```cd project-vanet-blockchain```

```truffle init```

##### Install create-react-app to initalized reactjs project
```npm install create-react-app```

##### Inside folder project-vanet-blockchain, initialize project reactjs 
```npx create-react-app client```

##### Install web3 
```npm install web3```

# 4. Compile, Migrate, Deploy Solidity Contracts:
##### Compile with truffle
```truffle compile```

##### Migrate with truffle or reset truffle
```truffle migrage```

```truffle migrate reset```