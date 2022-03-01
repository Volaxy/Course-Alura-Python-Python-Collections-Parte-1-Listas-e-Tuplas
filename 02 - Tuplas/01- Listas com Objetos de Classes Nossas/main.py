from account import Account


def __main__():
    gui_account = Account(1)
    print(gui_account)

    gui_account.deposit(500)
    print(gui_account)

    gab_account = Account(2)
    gab_account.deposit(1000)

    print()

    accounts = [gui_account, gab_account, gui_account]
    for account in accounts:
        print(account)


if __name__ == "__main__":
    __main__()
