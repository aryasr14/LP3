//SPDX-License-Identifier : UNLICENSED
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank{
    uint256 balance = 0;
    address public accOwner;

    constructor(){
        accOwner = msg.sender;
    }

    //Deposit
    function Deposit() public payable {
        require(accOwner == msg.sender, "You are the account owner");
        require(msg.value>0, "Amount should be greater than zero ");
        balance+=msg.value;
    }

    //Withdraw
    function Withdraw(uint256 amount) public {
    require(accOwner == msg.sender, "You are not the account owner");
    require(amount > 0, "Amount should be greater than zero");
    require(balance >= amount, "Insufficient balance");

    balance -= amount;

    payable(msg.sender).transfer(amount);
}

    //Show Balance
    function showBalance() public view returns(uint256){
        require(accOwner == msg.sender, "You are the account owner");
        return balance;
    }

}