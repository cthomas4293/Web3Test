from brownie import SimpleStorage, accounts, config, network


def read_contract():
    # [-1] gets the most recent address
    simple_storage = SimpleStorage[-1]
    # ABI
    # Address
    print(simple_storage.retrieve())


def main():
    read_contract()
