// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CoinReceiver {
    string private name = "Custom Coin";
    string public symbol = "CC";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    address public owner;
    mapping (address => uint256) public balanceOf;

    constructor() {
        owner = msg.sender;
        totalSupply = 0; //Initialize total supply to 0
    }   

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    function getName() external view returns (string memory) {
        return name;
    }

    function deposit(address recipient, uint256 amount) public onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        balanceOf[recipient] += amount;
        totalSupply -= amount;
    }

    function transfer(address to, uint256 value) public returns (bool success){
        require(balanceOf[msg.sender] >= value, "Insufficient balance");
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        
        return true;
    }
}