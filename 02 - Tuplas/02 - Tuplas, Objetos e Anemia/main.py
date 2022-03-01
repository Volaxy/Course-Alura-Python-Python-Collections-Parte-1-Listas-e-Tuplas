from account import Account


def __main__():
    gui_account = Account(1)
    gab_account = Account(2)
    print(gui_account)
    print(gab_account)

    accounts = [gui_account, gab_account]

    deposit_for_all(accounts)
    for account in accounts:
        print(account)

    gui_tuple = (1, 1000)

    print(gui_tuple)
    gui_tuple = deposit_in_tuple(gui_tuple)
    print(gui_tuple)
    # Usually the list stores a set of objects, and the tuple stores a set of values


def deposit_in_tuple(account):
    balance = account[1] + 100
    code = account[0]

    return code, balance


def deposit_for_all(accounts):
    for account in accounts:
        account.deposit(100)


if __name__ == "__main__":
    __main__()
