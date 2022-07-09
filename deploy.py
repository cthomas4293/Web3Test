import pprint

import semantic_version
import solcx
import json
from web3 import Web3

with open("./Test.sol", "r") as file:
    raw_sol_file = file.read()

# install and save solcx version
solcx.install_solc("0.8.0")
solc_version = semantic_version.Version("0.8.0")

# compile solidity file using solcx
compiled_file = solcx.compile_standard(
    {
        "language": "Solidity",
        "sources": {"Test.sol": {"content": raw_sol_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "evm.bytecode", "evm.sourceMap", "metadata"]}
            }
        },
    }
)

# get json file
with open("compiled_code.json", "w") as file:
    json.dump(compiled_file, file)

# get api
abi = compiled_file["contracts"]["Test.sol"]["TestContract"]["abi"]
# get bytecode
bytecode = compiled_file["contracts"]["Test.sol"]["TestContract"]["evm"]["bytecode"][
    "object"
]

# connect to a testnet
w3 = Web3(
    Web3.HTTPProvider("https://rinkeby.infura.io/v3/27c482d1e432482b9d7ecab36ee9d840")
)
# address
address = "0xbfCbf2f9F54fC161bF08a201bEF4Ad1dDaB54099"
# private key
private_key = "0x0ff90379c81e741c88f2ed7673f1ddaa76ce9fe2cee23d26d69f4fcdc283f3be"
# nonce
nonce = w3.eth.getTransactionCount(address)
# get chain ID
chainId = 4

# create a contract object
print("-> Creating Contract...")
TestContract = w3.eth.contract(abi=abi, bytecode=bytecode)
print("-> Contract Created!")

# build a transaction
print("-> Building New Transaction...")
test_txn = TestContract.constructor().buildTransaction(
    {
        "chainId": chainId,
        "nonce": nonce,
        "gasPrice": w3.eth.gas_price,
        "from": address,
    }
)
print("-> Transaction Built!")

# sign transaction
print("-> Signing Transaction Now...")
signed_txn = w3.eth.account.sign_transaction(test_txn, private_key=private_key)
print("-> Transaction Signed Successfully!")

# send transaction
prompt = input("Ready to send Transaction? Yes/ No\n")
if prompt == "Yes" or prompt == "Y":
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print("-> Sent Transaction!")
else:
    print("Closing Program!")
    raise Exception

print("-> Getting Transaction Receipt")
# get transaction receipt
txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
pprint.pprint("-> Here is Txn Receipt: {}".format(txn_receipt))

# -----------------------------------------------------------------
# CREATE A TRANSACTION USING YOUR CURRENT CONTRACT OBJECT

# create a contract object
print("-> Creating Contract...")
TransactionContract = w3.eth.contract(
    txn_receipt.contractAddress, abi=abi
)  # this contract is made from data of constructor contract
print("-> Contract Created!")

# build a transaction
print("-> Building New Transaction...")
newTransaction = TransactionContract.functions.retrieveNum().buildTransaction(
    {
        "chainId": chainId,
        "nonce": nonce + 1,
        "gasPrice": w3.eth.gas_price,
        "from": address,
    }
)
print("-> Transaction Built!")

# sign transaction
print("-> Signing Transaction Now...")
signedNewTransaction = w3.eth.account.sign_transaction(newTransaction, private_key=private_key)
print("-> Transaction Signed Successfully!")

# send transaction
prompt = input("Ready to send Transaction? Yes/ No\n")

if prompt == "Yes" or prompt == "yes":
    signedTransactionHash = w3.eth.send_raw_transaction(
        signedNewTransaction.rawTransaction
    )
    print("-> Sent Transaction!")
else:
    print("Closing Program!")
    raise Exception

print("-> Getting Transaction Receipt")
# get transaction receipt
newTransactionReceipt = w3.eth.wait_for_transaction_receipt(signedTransactionHash)
pprint.pprint("-> Here is Txn Receipt: {}".format(txn_receipt))
