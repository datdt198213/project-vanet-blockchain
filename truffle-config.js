module.exports = {

  // Confiure directory accommodate deployed contract files
  contracts_build_directory: "./client/src/contracts/",

  // configure network id
  networks: {
    // Deploy smart contract in Ganache
    development: {
      host: '127.0.0.1',     // Localhost (default: none)
      port: 7545,            // Standard Ethereum port (default: none)
      network_id: "*",       // Any network (default: none)
    }
  },

  // Configure compilers version
  compilers: {
    solc: {
      version: "0.8.0",      // Fetch exact version from solc-bin (default: truffle's version)
    }
  },
};
