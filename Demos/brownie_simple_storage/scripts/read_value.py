from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1]

    print(simple_storage.Retrieve())

def main():
    read_contract()