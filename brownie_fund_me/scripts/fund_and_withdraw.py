from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    # get latest contract deployed
    fund_me = FundMe[-1]
    # get an account to interact with
    account = get_account()
    # get starting fee
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entrance fee is {entrance_fee}")
    print("Funding...")
    # call fund function from contract instance
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()