module.exports = {

  // Confiure directory accommodate deployed contract files
  contracts_build_directory: "./client/src/contracts/",

  // configure network id
  networks: {
    // Deploy smart contract in Ganache
    host: "127.0.0.1",     // Localhost (default: none)
    development: {
     port: 8545,            // Standard Ethereum port (default: none)
     network_id: "*",       // Any network (default: none)
    },
  },

  mocha: {
    // timeout: 100000
  },

  // Configure compilers version
  compilers: {
    solc: {
      version: "0.8.19",      // Fetch exact version from solc-bin (default: truffle's version)
    }
  },

  // db: {
  //   enabled: false,
  //   host: "127.0.0.1",
  //   adapter: {
  //     name: "indexeddb",
  //     settings: {
  //       directory: ".db"
  //     }
  //   }
  // }
};
