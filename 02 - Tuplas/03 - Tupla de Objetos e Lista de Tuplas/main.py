from account import Account


def __main__():
    # When we have a tuple of objects, the indexes of the tuple is not modify, but the object inside the index can be
    # modify
    gui_account = Account(1)
    gab_account = Account(2)
    print(gui_account)
    print(gab_account)

    accounts = (gui_account, gab_account)
    print(accounts)

    # When we have a list of tuple, the indexes of the list can be modified, but the tuple in the index not
    gui = (1, 10)
    gui_tuple = deposit_in_tuple(gui)
    gab = (2, 50)
    gab_tuple = deposit_in_tuple(gab)

    users = [gui_tuple, gab_tuple]
    print(users)


def deposit_in_tuple(account):
    balance = account[1] + 100
    code = account[0]

    return code, balance


def deposit_for_all(accounts):
    for account in accounts:
        account.deposit(100)


if __name__ == "__main__":
    __main__()
