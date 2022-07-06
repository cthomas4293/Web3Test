// SPDX-Identifier-MIT

pragma solidity ^0.8.0;

contract TestContract {
    uint256 userNumber = 0;

    function updateNum(uint256 _newNum) public {
        userNumber = _newNum;
    }

    function retrieveNum() public returns (uint256) {
        return userNumber;
    }

}