import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";

const config: HardhatUserConfig = {
    networks: {
        hardhat: {
        },
        sepolia: {
          url: "https://sepolia.infura.io/v3/bb67d73db1db449b9140a67ad38ab87f", // API Key of INFURA - RPC
          accounts: ["6092e6033c0dcb18f3cdb1c51f847e7112eb49488eedf2bc3ba3abdc9ac75565"]
        }
      },
    etherscan: {
        apiKey: {
            sepolia: "WDEIINZHN7I2XNZ19NHK7ME1J54JHRQBBJ", // API KEY of Sepoila.etherscan
        }
    },
    solidity: "0.8.24",
};

export default config;