const CoinReceiver = artifacts.require("CoinReceiver");

module.exports = function(deployer) {
    deployer.deploy(CoinReceiver);
}