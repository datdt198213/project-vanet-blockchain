// const { ethers, upgrades } = require('hardhat');

// async function main() {
//     const MyToken = await ethers.getContractFactory('Token');

//     const vWMToken = await MyToken.deploy(3000000);
//     console.log(`Deploy to: ${await vWMToken.getAddress()}`);
// }

// main();

import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

const NAME: string = "Token RideShare";
const SYMBOL: string = "TRS";
const SUPPLY: bigint = 3_000_000_000n;

const TokenModule = buildModule("TokenModule", (m) => {
  const name = m.getParameter("name", NAME);
  const symbol = m.getParameter("symbol", SYMBOL);
  const supply = m.getParameter("initialSupply", SUPPLY);

  const token = m.contract("Token", [name, symbol, supply]);

  return { token };
});

export default TokenModule;