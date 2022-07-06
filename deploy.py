import semantic_version
import solcx
import json

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
# address
# private key
# nonce
