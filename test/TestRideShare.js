
const RideShare = artifacts.require("RideShare");

contract("RideShare", (accounts) => {

    // Hàm này sẽ được gọi trước khi chạy các unit test bên dưới
    before(async() => {
        this.owner = accounts[0];
        this.rideShareInstance = {};
    })

    it("Should get balance of an account", async() => {
    });
})