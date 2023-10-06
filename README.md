Introduction:

Blockchain technology has revolutionized various industries, and the ability to simulate it using JavaScript and Ganache provides developers with a powerful tool for testing Solidity contracts on a personal Ethereum Blockchain. In this document, we will explore the process of setting up Ganache and utilizing JavaScript to simulate blockchain technology for testing purposes.

### 1. Setting up Ganache:

To begin, we need to install Ganache, a personal Ethereum Blockchain that allows us to simulate blockchain transactions and interactions. Here are the steps to set it up:

1.1. Download and Install Ganache:

Visit the official Ganache website and download the appropriate version for your operating system. 
Link download: https://trufflesuite.com/ganache/

1.2. Launching Ganache:

After installation, open Ganache and you will be greeted with a user-friendly interface. Ganache provides you with a local Ethereum Blockchain network, complete with pre-funded accounts for testing your Solidity contracts.

### 2. Setting environment

2.1. Download node version LTS
Link download: https://nodejs.org/en/download

2.2. Download truffle
```
npm install truffle
```

### 3. Initialized project

3.1. Create folder project-vanet-blockchain
```
mkdir project-vanet-blockchain
```

3.2. Change directory to folder project-vanet-blockchain and initialize truffle project
```
cd project-vanet-blockchain
```

```
truffle init
```

3.3. Install create-react-app to initalized reactjs project
```
npm install create-react-app
```

3.4. Inside folder project-vanet-blockchain, initialize project reactjs 
```
npx create-react-app client
```

3.5. Install web3 
```
npm install web3
```

### 4. Compile, Migrate, Deploy Solidity Contracts:
4.1. Compile with truffle
```
truffle compile
```

4.2. Migrate with truffle
```
truffle migrage
```

When smart contracts be migrated by truffle, file deployed contracts be placed in "./client/src/contracts"

To reset migration when contracts have changed, run below command

```
truffle migrate reset
```
