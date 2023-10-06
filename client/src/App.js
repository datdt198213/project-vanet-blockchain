import "./App.css";
import Web3 from "web3";
import CoinReceive from "./contracts/CoinReceiver.json";
import RideShare from "./contracts/RideShare.json";
import {useState, useEffect} from "react";

function App() {
  const [stateCR, setStateCR] = useState({web3:null, contract:null});
  const [stateRS, setStateRS] = useState({web3:null, contract:null});
  const [name, setName] = useState("nil");
  const [balance, setBalance] = useState(0);
  
  // Declare passenger information
  const [passenger, setPassenger] = useState({price: null, state: null});
  const [priceOfPassenger, setPriceOfPassenger] = useState("");
  const [stateOfPassenger, setStateOfPassenger] = useState("");

  // Declare smart contract and web3
  useEffect(() => {
    const provider = new Web3.providers.HttpProvider("HTTP://127.0.0.1:7545");
    async function initializedContract() {
      const web3 = new Web3(provider);

      const networkId = await web3.eth.net.getId();
      const deployedNetwork = CoinReceive.networks[networkId];

      const contractCR = new web3.eth.Contract(CoinReceive.abi, deployedNetwork.address);
      const contractRS = new web3.eth.Contract(RideShare.abi, deployedNetwork.address);

      setStateCR({web3:web3, contractCR:contractCR});
      setStateRS({web3:web3, contractRS:contractRS});
    };
    provider && initializedContract();
  }, []);

  // contract coin receive
  useEffect(() => {
    const { contractCR } = stateCR;
    async function getName() {
      const name = await contractCR.methods.getName().call();
      console.log(name);
      setName(name);
    }
    contractCR && getName();

  }, [stateCR]);

  async function writeName() {
    const { contractCR } = stateCR;
    await contractCR.methods.setName("Hello world Contract").send({from: "0xAe4644cD4b6f71a7A31eE5583D27e8B198d9f489"});
    window.location.reload();
  }

  // Contract ride share
  useEffect(() => {
    const { web3, contractRS } = stateRS;
    async function getBalance() {
      const balance = await web3.eth.getBalance("0xc33103f168f2Fc20f5886E62e538dD908b2ad380");
      const balanceInEther = web3.utils.fromWei(balance, "ether");
      setBalance(balanceInEther);
    }
    contractRS && getBalance();
  }, [stateRS]);

  // Loading passenger information
  // useEffect(() => {
  //   const {web3, contractRS} = stateRS; 
  //     async function retrievePassenger() {
  //       try {
  //         const passenger = await contractRS.methods.retrievePassenger("0xc33103f168f2Fc20f5886E62e538dD908b2ad380").call();
  //         const [price, state] = passenger;
  //         console.log(`Passenger Price: ${price}, State: ${state}`);
  //       } catch(error) {
  //         console.log("Error retrieving passenger information: ", error);
  //       }
  //     }
  //     contractRS && retrievePassenger();
  //   }, [stateRS]); 

  // Set information for passenger
  async function addPassenger(state) {
      const {web3, contractRS} = stateRS;
      try {
        const event = contractRS.events.PassengerAdded("Dat", "0348247064", 4, "initial");

        // await contractRS.methods.addPassenger("Dat", "0348247064", 4, "initial").send({from: "0xAe4644cD4b6f71a7A31eE5583D27e8B198d9f489"});
        window.location.reload();
      } catch (error) {
        console.log("Error adding passenger: ", error);
      }
  }

  return (<div className="App">
    <p> Contract name: {name}</p> 
    <p> Number balance of account: {balance} ETH</p>
    <button onClick={writeName}>Change name</button>
    {/* <p> Passenger price: {priceOfPassenger}</p> */}
    {/* <p> Passenger state: {stateOfPassenger}</p> */}
    <div>
      <button onClick={() => addPassenger("Free")}>Add passenger</button>
    </div>
  </div>);
}

export default App;
