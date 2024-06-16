import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

const TOKEN_ADDRESS: string = "0x59A22958b648E09002B8c438DBbCB2645959C915";

const RideshareModule = buildModule("RideshareModule", (m) => {
  const tokenAddress = m.getParameter("_tokenAddress", TOKEN_ADDRESS);

  const rideShare = m.contract("Rideshare", [tokenAddress]);

  return { rideShare };
});

export default RideshareModule;