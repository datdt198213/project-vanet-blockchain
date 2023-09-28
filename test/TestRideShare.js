
const RideShare = artifacts.require("RideShare");

contract("RideShare", (accounts) => {

    before(async() => {
        this.owner = accounts[0];
        this.rideShareInstance = {};
    })

    it("Should get balance of an account", async() => {
        const accountAddress = "0xc33103f168f2Fc20f5886E62e538dD908b2ad380";
        const blance = await web3.eth.getBalance(accountAddress);

        // Convert the balance from wei to ether (optional)
        const balanceInEther = web3.utils.fromWei(balance, "ether");

        console.log(`Balance of ${accountAddress}: ${balanceInEther} ETH`);

        // Add your assertions here, e.g., check that the balance is greater than a certain amount
        expect(parseFloat(balanceInEther)).to.be.greaterThan(0);
    });
})