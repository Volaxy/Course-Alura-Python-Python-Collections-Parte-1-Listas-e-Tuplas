from accounts import Account, CheckingAccount, SavingAccount


def __main__():
    gui_account = CheckingAccount(1)
    gab_account = SavingAccount(2)
    print(gui_account)
    print(gab_account)

    gui_account.deposit(50)
    gab_account.deposit(25)

    accounts = [gui_account, gab_account]

    for account in accounts:
        account.month_passes()

    for account in accounts:
        print(account)


if __name__ == "__main__":
    __main__()
