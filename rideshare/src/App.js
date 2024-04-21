import "./App.css";
// import Navbar from "./Navbar";
import Web3 from "web3";
import RideShare from "./contracts/RideShare.json";
import { useState, useEffect } from "react";
import React, { Component } from "react";
import { Modal } from "bootstrap";
// import Main from './Main';

function App() {
  // const [stateRS, setStateRS] = useState({ web3: null, contract: null });
  // const [account, setAccount] = useState("");
  // const [name, setName] = useState("nil");
  // const [balance, setBalance] = useState(0);

  // // Declare passenger information
  // const [passenger, setPassenger] = useState({ price: null, state: null });
  // const [priceOfPassenger, setPriceOfPassenger] = useState("");
  // const [stateOfPassenger, setStateOfPassenger] = useState("");

  // // Declare smart contract and web3
  // useEffect( () => {
    
  //   initializedContract();
  //   getAccount();
  //   getBalance();
  // }, [account]);

  // async function initializedContract() {
  //   const web3 = new Web3(window.ethereum);
  //   const networkId = await web3.eth.net.getId();
  //   const deployedNetwork = await RideShare.networks[networkId];
  //   const contractRS = new web3.eth.Contract(
  //     RideShare.abi,
  //     deployedNetwork && deployedNetwork.address
  //   );
  //   setStateRS({ web3: web3, contractRS: contractRS });
  // }

  // async function getBalance() {
  //   const { web3, contractRS } = stateRS;
  //   if (web3 !== null) {
  //     const balance = await web3.eth.getBalance(account);
  //     // console.log(balance)
  //     var balanceInEther;
  //     if (balance) {
  //       balanceInEther = web3.utils.fromWei(balance, "ether");
  //     }
  //     setBalance(balanceInEther);
  //   } else {
  //     console.error("web3 is null");
  //   }
  // }

  // async function getAccount() {
  //   if (window.ethereum) {
  //     try {
  //       const accounts = await window.ethereum.request({ method: "eth_requestAccounts",});
  //       setAccount(accounts[0]);
  //     } catch (e) {
  //       console.log(e);
  //     }
  //   }
  // }

  // Contract ride share
  // async function addPassenger(name, phoneNumber, noPeople, state) {
  //   const { web3, contractRS } = stateRS;
  //   try {
  //     const result = contractRS.methods.addPassenger(name, phoneNumber, noPeople, state).send({ from: account });
  //     console.log(result);
  //     // window.location.reload();
  //   } catch (error) {
  //     console.log("Error adding passenger: ", error);
  //   }
  // }

  const [account, setAccount]= useState("");
  const [balance, setBalance] = useState("");
  const [drivingCost, setDrivingCost] = useState(0);
  const [capacity, setCapacity] = useState(0);
  const [confirmAt, setConfirmAt] = useState('');
  const [originAddress, setOriginAddress] = useState('');
  const [destAddress, setDestAddress] = useState('');

  const [showSuccessModal, setShowSuccessModal] = useState(false); // State để kiểm soát hiển thị modal
  const now = new Date();
  const formattedNow = now.toISOString().slice(0, 16); // Định dạng thời gian hiện tại thành YYYY-MM-DDTHH:MM
  
  
  async function requestAccount(){
    console.log('Requesting account...');
    // Kiem tra xem trinh duyet co ket noi voi Metamask ko 
    if (window.ethereum){
      console.log('MetaMask Detected');
      try {
        const accounts = await window.ethereum.request({method: "eth_requestAccounts"});
        //console.log(accounts);
        setAccount(accounts[0]);
        
      }catch(error){
        console.log('Error connecting with MetaMask');
      }
    }
    else {
      console.log('MetaMask not detected');
      window.alert('Please install MetaMask');
    }

  }
  //ket noi voi tai khoan MetaMask
  async function connectWallet () {
    //kiem tra MetaMask ton tai khong
    if (typeof window.ethereum !=="undefined"){
      await requestAccount ();
      const web3 = new Web3(window.ethereum);
      const provider = new Web3(web3.currentProvider);
    } 
  }
  useEffect (() => {
    //the code that we want to run
   connectWallet();
    
    //Khi đã đăng nhập vào ví Metamask, chuyến đến màn hình chính
    //optional return function 
    return () =>{
      //console.log('I am being cleaned up!');
    }
  }, []); // The dependencies array

 const handleCreateRide = async () => {
    console.log(drivingCost, capacity, confirmAt, originAddress, destAddress);

    if (!drivingCost || !capacity || !confirmAt || !originAddress || !destAddress) {
      // Nếu bất kỳ trường nào còn trống, hiển thị thông báo hoặc thực hiện hành động phù hợp
      alert('Please fill in all required fields.');
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
      await contract.methods.createRide(drivingCost, capacity, confirmAtUnix, originAddress, destAddress).send({ from: accounts[0], value: drivingCost*1e18});
      
      // window.location.reload();
    } catch (error) {
      console.log("Error create ride passenger: ", error);
    }
  }

    return (
      <div className="App">
        {/* <p> Account: {account}</p> */}
        {/* <p> Balance: {balance} ETH</p> */}
        <div>
          {/* <button onClick={() => addPassenger("Dat", "0348247064", 2, "initial")}>Add passenger</button> */}
          <nav className="navbar navbar-dark fixed-top shadow p-0" style={{backgroundColor:'black', height:'50px'}}>
            <a className="navbar-brand col-sm-3 col-md-2 mr-0"
             style={{color:'white'}}>Rideshare Application</a>
            <ul className="navbar-nav px-3">
              <li className="text-nowrap nav-item d-sm-block">
                <small style={{color:'white'}}>Account: {account}</small>
              </li>
              <li className="text-nowrap nav-item d-sm-block">
                <small style={{color:'white'}}>Balance: {balance} ETH</small>
              </li>
            </ul>
          </nav>
          <div className="container">
            <div style={{marginTop:'70px'}}>
            <h2>Create Ride</h2>
            <div className="row">
              <div className="col-md-6">
                  <label>From:</label>
                  <input type="text" className="form-control" required value={originAddress} onChange={(e) => setOriginAddress(e.target.value)} />
              </div>
              <div className="col-md-6">
                  <label>To:</label>
                  <input type="text" className="form-control" required value={destAddress} onChange={(e) => setDestAddress(e.target.value)} />
              </div>
            </div>
            <div className="row">
              <div className="col-md-6">
                  <label>Driving Cost:</label>
                  <input type="number" className="form-control" required value={drivingCost} min ='0' onChange={(e) => setDrivingCost(e.target.value)} />
              </div>
              <div className="col-md-6">
                  <label>Start Time:</label>
                  <input type="datetime-local" className="form-control" required value={confirmAt} onChange={(e) => setConfirmAt(e.target.value)} />
              </div>
            </div>
            <div className="row">
              <div className="col-md-6">
                  <label>Capacity</label>
                  <input type="number" className="form-control" required value={capacity} min='1'onChange={(e) => setCapacity(e.target.value)} />
              </div>
          </div>
          <button className="btn btn-primary mt-3" onClick={handleCreateRide}>Create Ride</button>
          
          {/* <Modal show={showSuccessModal} onHide={handleClose}>
            <Modal.Header closeButton>
              <Modal.Title>Ride Created Successfully</Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <p>Your ride has been created successfully!</p>
            </Modal.Body>
            <Modal.Footer>
              <Button variant="secondary" onClick={handleClose}>
                Close
              </Button>
              <Button variant="primary" onClick={handleCheckYourRideList}>
                Check Your Ride List
              </Button>
            </Modal.Footer>
          </Modal> */}
    
        
        </div>
          </div>
          
        
        </div>
      </div>
    );
  }


// class App extends Component {

//   async UNSAFE_componentWillMount() {
//     await this.loadWeb3();
//     await this.loadBlockchainData()
//   }

//   async loadWeb3() {
//     if (window.ethereum) {
//       window.web3 = new Web3(window.ethereum);
//       await window.ethereum.enable();
//     } else if (window.web3) {
//       window.web3 = new Web3(window.web3.currentProvider)
//     } else {
//       window.alert('No ethereum browser detected! You can check out metamask!')
//     }
//   }

//   async loadBlockchainData() {
//     const web3 = window.web3;
//     const account = await web3.eth.getAccounts();
//     this.setState({account: account[0]});
//     const networkId = await web3.eth.net.getId();

//     // Load RideShare contract
//     const rideShareData = RideShare.networks[networkId];
//     if(rideShareData) {
//       const rs = new web3.eth.Contract(RideShare.abi, rideShareData.address);
//       this.setState({rideShare: rs});
//       // let rbl = await rideShare.methods.balanceOf(this.state.account).call()
//       let rbl = await web3.eth.getBalance(this.state.account)
//       let balanceInEther = await web3.utils.fromWei(rbl, "ether");
//       this.setState({rideShareBalance: balanceInEther.toString()})
//     } else {
//       window.alert('Error! RideShare contract not deployed - no detected network!');
//     }
//     this.setState({loading: false});
//   }

//   constructor(props) {
//     super(props);
//     this.state = {
//       account: '0x0',
//       rideShare: {},
//       rideShareBalance: '0',
//       loading: true
//     }
//   }

//   render() {

//     let content;
//     {this.state.loading ? content =
//     <p id='loader'
//     className="text-center"
//     style={{margin: '30px'}}>
//       Loading Please...</p> : content =
//       <Main rideShareBalance={this.state.rideShareBalance}
//       rideShare={this.state.rideShare} account={this.state.account}
//       />}
//     return (
//       <div>
//         <Navbar account={this.state.account}/>
//         <div className="container-fluid mt-5">
//           <div className="row content">
//             <main role="main" className="col-lg-12 ml-auto mr-auto" style={{maxWidth:'600px', minHeight:'100vm'}}>
//               <div>
//                 {content}
//               </div>
//             </main>
//           </div>
//         </div>
//       </div>
//     )
//   }
// }

// App = {
//   loading: false,
//   contracts: {},
//   account: null,
//   rideContract: null,
//   web3Provider: null,
//   balance: 0,
 
 
 
//   load: async () => {
//     await App.loadWeb3();
//     await App.loadAccount();
//     await App.loadContract();
//     await App.render();
//     await App.updateBalance();// Cập nhật số dư khi tải ứng dụng
//     // Lấy thời gian hiện tại
//     const now = new Date();
 
//     // Định dạng thời gian hiện tại thành YYYY-MM-DDTHH:MM để có thể sử dụng trong thuộc tính "min" của input
//     const formattedNow = now.toISOString().slice(0, 16);
 
//     // Gán giá trị cho thuộc tính "min" của input
//     document.getElementById("startDateTime").min = formattedNow;
 
//   },
 
//   loadWeb3: async () => {
//     if (typeof web3 !== 'undefined') {
//       App.web3Provider = window.ethereum;
//       web3 = new Web3(window.ethereum);
//     } else {
//       window.alert("Please connect to Metamask.");
//     }
 
//     if (window.ethereum) {
//       //App.web3Provider = new Web3(ethereum);
//       try {
//         await ethereum.request({ method: 'eth_requestAccounts' })
//        // web3.eth.sendTransaction({/*...*/});
//       } catch (error) {
//         console.error('User denied account access');
//       }
//     } else if (window.web3) {
//       App.web3Provider = web3.currentProvider;
//       window.web3 = new Web3(web3.currentProvider);
//       web3.eth.sendTransaction({});
//     } else {
//       console.log('Non-Ethereum browser detected. You should consider trying MetaMask!');
//     }
//   },
 
//   loadAccount: async () => {
//     const accounts = await web3.eth.getAccounts();
//     App.account = accounts[0];
//     $('#account').html(`Account: ${App.account}`);
//   },
 
//   loadContract: async () => {
     
//       const rideContracts = await $.getJSON('RideContract.json');
//       App.contracts.RideContract = TruffleContract(rideContracts )
//       App.contracts.RideContract.setProvider(App.web3Provider)
 
//        // Hydrate the smart contract with values from the blockchain
//       App.rideContracts  = await App.contracts.RideContract.deployed()
//   },
 
//   render: async () => {
//     if (App.loading) {
//       return;
//     }
//     App.setLoading(true);
//     await App.renderRides();
//     App.setLoading(false);
//   },
//   updateBalance: async () => {
//       try {
//         // Truy vấn số dư của tài khoản hiện tại
//         const accounts = await window.web3.eth.getAccounts();
//         const account = accounts[0];
//         const balanceWei = await window.web3.eth.getBalance(account);
//         const balanceEther = window.web3.utils.fromWei(balanceWei, 'ether');
//         App.balance = parseFloat(balanceEther);
//         $('#balance').html(`Balance: ${App.balance} ETH`);
        
//       } catch (error) {
//         console.error('Error updating balance:', error);
//       }
//     },
  
//   createRide: async () => {
//     App.setLoading(true);
//     const startPoint = $('#startPoint').val();
//     const endPoint = $('#endPoint').val();
//     const fare = $('#fare').val();
//     // Get the value of the start date and time input field
//     const startDateTimeInput = document.getElementById('startDateTime').value;
//     const numOfSeats = $('#numOfSeats').val();
//     // Convert the start date and time to Unix timestamp
//     const startTime = Math.floor(new Date(startDateTimeInput).getTime() / 1000);
//     await App.rideContracts.createRide(startPoint, endPoint, fare, startTime, numOfSeats,{ from: App.account });
//     window.location.reload();
//   },
 
//   setLoading: (boolean) => {
//     App.loading = boolean;
//     const loader = $('#loader');
//     const content = $('#content');
//     if (boolean) {
//       loader.show();
//       content.hide();
//     } else {
//       loader.hide();
//       content.show();
//     }
//   }
// }
 
// $(() => {
//   $(window).load(() => {
//     App.load();
//   });
// });
 

export default App;
