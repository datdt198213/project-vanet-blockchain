const CoinReceiver = artifacts.require("CoinReceiver");

contract("CoinReceiver", (accounts) => {

    it("Should get data", async () => {
        const coin = await CoinReceiver.deployed();
        const data = await coin.getName();
        console.log(data);
    })
})