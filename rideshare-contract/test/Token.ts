import {
    time,
    loadFixture,
  } from "@nomicfoundation/hardhat-toolbox/network-helpers";
  import { anyValue } from "@nomicfoundation/hardhat-chai-matchers/withArgs";
  import { expect } from "chai";
  import ethers from "ethers";
  import hre from "hardhat";
  
  describe("TOken", function () {
    // We define a fixture to reuse the same setup in every test.
    // We use loadFixture to run this setup once, snapshot that state,
    // and reset Hardhat Network to that snapshot in every test.
    async function deployContract() {
  
      // Contracts are deployed using the first signer/account by default
      // const [owner, otherAccount] = await hre.ethers.getSigners();
      const ownerAddress = "0xB0C8c9c04f2Dec2526Bb355eEC7eD7C36dAdfE90";
      
      const owner = new hre.ethers.Wallet("6092e6033c0dcb18f3cdb1c51f847e7112eb49488eedf2bc3ba3abdc9ac75565", hre.ethers.provider);
      const passenger = "0xc2CCcfd3215A44104D74c5188217574c92d9d745";
      const driver = "0xf40063350544F3104fc072C5a09A010f28dbdCF7";
      const tokenContractAddress = "0x59A22958b648E09002B8c438DBbCB2645959C915";
      const rideshareContractAddress = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512";
      // const Lock = await hre.ethers.getContractFactory("Token");
      // const lock = await Lock.deploy(unlockTime, { value: lockedAmount });
      const Token = await hre.ethers.getContractFactory("Token");
      const token = await Token.attach(tokenContractAddress);
  
      const Rideshare = await hre.ethers.getContractFactory("Rideshare");
      const rideshare = await Rideshare.attach(rideshareContractAddress);
  
      return { token, rideshare, owner, passenger, driver };
    }
  });