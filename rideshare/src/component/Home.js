import Web3 from "web3";
import RideShare from "../contracts/RideShare.json";
import { useState, useEffect } from "react";
import React from "react";
import { Modal, Button } from "react-bootstrap";
import RideInfor from "./RideInfor";

const Home = () => {
  const [account, setAccount] = useState("");
  const [drivingCost, setDrivingCost] = useState(0);
  const [capacity, setCapacity] = useState(0);
  const [confirmAt, setConfirmAt] = useState("");
  const [originAddress, setOriginAddress] = useState("");
  const [destAddress, setDestAddress] = useState("");
  const [showSuccessModal, setShowSuccessModal] = useState(false); // State để kiểm soát hiển thị modal
  const now = new Date();
  const formattedNow = now.toISOString().slice(0, 16); // Định dạng thời gian hiện tại thành YYYY-MM-DDTHH:MM
  const handleCheckYourRideList = () => {
    //onCheckYourRideList(); // Gọi hàm để thay đổi tab sang "Home"
    setShowSuccessModal(false); // Đóng modal thông báo
    // handleTabChange('home'); // Chuyển tab sang "Home"
  };
  const handleClose = () => setShowSuccessModal(false);

  async function requestAccount() {
    console.log("Requesting account...");
    // Kiem tra xem trinh duyet co ket noi voi Metamask ko
    if (window.ethereum) {
      console.log("MetaMask Detected");
      try {
        const accounts = await window.ethereum.request({
          method: "eth_requestAccounts",
        });
        const web3 = new Web3(window.ethereum);
        //console.log(accounts);
        setAccount(accounts[0]);
      } catch (error) {
        console.log("Error connecting with MetaMask");
      }
    } else {
      console.log("MetaMask not detected");
      window.alert("Please install MetaMask");
    }
  }
  //ket noi voi tai khoan MetaMask
  async function connectWallet() {
    //kiem tra MetaMask ton tai khong
    if (typeof window.ethereum !== "undefined") {
      await requestAccount();
      const web3 = new Web3(window.ethereum);
    }
  }
  useEffect(() => {
    // the code that we want to run
    connectWallet();
    //  console.log(account)
    return () => {
      //console.log('I am being cleaned up!');
    };
  }, []); // The dependencies array

  const handleCreateRide = async () => {
    if (
      !drivingCost ||
      !capacity ||
      !confirmAt ||
      !originAddress ||
      !destAddress
    ) {
      // Nếu bất kỳ trường nào còn trống, hiển thị thông báo hoặc thực hiện hành động phù hợp
      alert("Please fill in all required fields.");
      return; // Ngăn chặn việc tiếp tục thực hiện hành động
    }

    const web3 = new Web3(window.ethereum);
    const accounts = await web3.eth.getAccounts();
    const networkId = await web3.eth.net.getId();
    const deployedNetwork = RideShare.networks[networkId];
    const contract = new web3.eth.Contract(
      RideShare.abi,
      deployedNetwork && deployedNetwork.address
    );

    const confirmAtUnix = Math.floor(new Date(confirmAt).getTime() / 1000);
    try {
      await contract.methods
        .createRide(
          drivingCost,
          capacity,
          confirmAtUnix,
          originAddress,
          destAddress
        )
        .send({ from: accounts[0], value: drivingCost * 1e18 });
      setShowSuccessModal(true);
    } catch (error) {
      console.log("Error create ride passenger: ", error);
    }
  };
  return (
    <div className="container">
      <div style={{ marginTop: "70px" }}>
        <h2>Create Ride</h2>
        <div className="row">
          <div className="col-md-6">
            <label>From:</label>
            <input
              type="text"
              className="form-control"
              required
              value={originAddress}
              onChange={(e) => setOriginAddress(e.target.value)}
            />
          </div>
          <div className="col-md-6">
            <label>To:</label>
            <input
              type="text"
              className="form-control"
              required
              value={destAddress}
              onChange={(e) => setDestAddress(e.target.value)}
            />
          </div>
        </div>
        <div className="row">
          <div className="col-md-6">
            <label>Driving Cost:</label>
            <input
              type="number"
              className="form-control"
              required
              value={drivingCost}
              min="0"
              onChange={(e) => setDrivingCost(e.target.value)}
            />
          </div>
          <div className="col-md-6">
            <label>Start Time:</label>
            <input
              type="datetime-local"
              className="form-control"
              required
              value={confirmAt}
              onChange={(e) => setConfirmAt(e.target.value)}
            />
          </div>
        </div>
        <div className="row">
          <div className="col-md-6">
            <label>Capacity</label>
            <input
              type="number"
              className="form-control"
              required
              value={capacity}
              min="1"
              onChange={(e) => setCapacity(e.target.value)}
            />
          </div>
        </div>
        <button className="btn btn-primary mt-3" onClick={handleCreateRide}>
          Create Ride
        </button>

        <RideInfor account={account} />

        <Modal show={showSuccessModal} onHide={handleClose}>
          <Modal.Header closeButton>
            <Modal.Title>Ride Created Successfully</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <p>Your ride has been created successfully!</p>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="primary" onClick={handleClose}>
              OK
            </Button>
          </Modal.Footer>
        </Modal>
      </div>
    </div>
  );
};

export default Home;
