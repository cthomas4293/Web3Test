// "SPDX-License-Identifier: MIT"

// Name solidity version
pragma solidity ^0.6.0;

// Name contract which is much like a class
contract SimpleStorage {

    uint256 favoriteNumber = 0; // unsigned (positive) integer with limit of 256 bits
    // public keyword allows this variable to be visible during compilation
    // ex: variableType variableVisibility variableName;
    uint256 nullValue; // all variables initialize to nullValue or 0 when not initialized
    int256 favoriteInt = - 5; // integer that can be either positive or negative
    bool favoriteBool = true; // boolean variable
    string favoriteString = "hello"; // text variable
    address favoriteAddress = 0xbfCbf2f9F54fC161bF08a201bEF4Ad1dDaB54099; // crypto address
    bytes32 favoriteByte = "cat"; // bytes object which has a total of 32 (Max) bytes(number of bytes can be changed)

    // Class structure for Solidity
    struct People {
        uint256 favoriteNumber;
        string name;
    }

    // Object in solidity
    People public person = People({favoriteNumber : 2, name : "Carl"});

    // Array in solidity (can be dynamic or initialized with a array size)
    // type arrayName [ arraySize ];
    People[] public people;

    // Dictionary for solidity
    mapping(string => uint256) public nameToFavoriteNumber;

    // -----------------------------------------------------------------------------------------------------------------//

    // Defining a function that changes the value of favoriteNumber
    function store(uint256 _favoriteNumber) public {

        favoriteNumber = _favoriteNumber;
    }

    // storage types in solidity: memory or storage
    // memory only stores during execution/ contract call
    // storage means the data will persist even after function call
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People({favoriteNumber : _favoriteNumber, name : _name}));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }

    // view, pure
    // view wants to read some state of the block chain
    // pure functions do some type of computation but doesn't save any state
    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

}