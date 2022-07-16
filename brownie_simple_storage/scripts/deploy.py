from brownie import accounts, SimpleStorage, network
import os


def deploy_simple_storage():
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    print(account)
    # account = get_account()
    # simple_storage = SimpleStorage.deploy({"from": account})
    # stored_value = simple_storage.retrieve()
    # print(stored_value)
    # transaction = simple_storage.store(15, {"from": account})
    # transaction.wait(1)
    # updated_stored_value = simple_storage.retrieve()
    # print(updated_stored_value)


# def get_account():
#     if network.show_active() == "development":
#         return accounts[0]
#     else:
#         return accounts.add(os.getenv("WEB3_INFURA_PROJECT_ID"))


def main():
    deploy_simple_storage()
