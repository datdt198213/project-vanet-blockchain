import "./App.css";
// import Navbar from "./Navbar";
import Web3 from "web3";
import RideShare from "./contracts/RideShare.json";
import { useState, useEffect } from "react";
import React from "react";
import Home from "./component/Home";
import News from "./component/News";
import Contact from "./component/Contact";
import {Routes, Route, Link} from 'react-router-dom';

function App() {

  const [account, setAccount]= useState("");
  async function requestAccount(){
    console.log('Requesting account...');
    // Kiem tra xem trinh duyet co ket noi voi Metamask ko 
    if (window.ethereum){
      console.log('MetaMask Detected');
      try {
        const accounts = await window.ethereum.request({method: "eth_requestAccounts"});
        const web3 = new Web3(window.ethereum);
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
    } 
  }
  useEffect (() => {
    // the code that we want to run
   connectWallet();
  //  console.log(account)
    return () => {
      //console.log('I am being cleaned up!');
    }
  }, []); // The dependencies array

    return (
      <div className="App">
        <div>
          <nav className="navbar navbar-dark fixed-top shadow p-0" style={{backgroundColor:'black', height:'50px'}}>
            <Link to="/" className="navbar-brand col-sm-3 col-md-2 mr-0"
             style={{color:'white'}}>Rideshare Application</Link>

              <Link to='/news'>News</Link>
              <Link to='/contact'>Contact</Link>
             
            <ul className="navbar-nav px-3">
              <li className="text-nowrap nav-item d-sm-block">
                <small style={{color:'white'}}>Account: {account}</small>
              </li>
            </ul>
          </nav>


          <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/news" element={<News/>}/>
            <Route path="/contact" element={<Contact/>}/>

          </Routes>

           
        
        </div>
        
      </div>
    );
}


export default App;
