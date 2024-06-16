# Sample Hardhat Project

This project demonstrates a basic Hardhat use case. It comes with a sample contract, a test for that contract, and a Hardhat Ignition module that deploys that contract.

Try running some of the following tasks:

```shell
npx hardhat help
npx hardhat test
REPORT_GAS=true npx hardhat test
npx hardhat node
npx hardhat ignition deploy ./ignition/modules/Token.ts --network sepolia
npx hardhat ignition deploy ./ignition/modules/Rideshare.ts --network sepolia --deployment-id second-deploy
npx hardhat ignition deploy ./ignition/modules/Rideshare.ts --network sepolia --deployment-id third-deploy
npx hardhat verify --network sepolia 0xBA32155BC48Ac63b89c88b6FA032F9C077Dcee55 "Token RideShare" "TRS" 3000000000
npx hardhat verify --network sepolia 0xa95566d1362Cce4e245Cbe86Aa083D596F8ec7e1 0xBA32155BC48Ac63b89c88b6FA032F9C077Dcee55
```

0xBA32155BC48Ac63b89c88b6FA032F9C077Dcee55: Address of contract <br>
"Token RideShare" "TRS" 3000000000: Parameter of contract's constructor

1. Env File <br>
There are my accounts with available sepolia ETH 