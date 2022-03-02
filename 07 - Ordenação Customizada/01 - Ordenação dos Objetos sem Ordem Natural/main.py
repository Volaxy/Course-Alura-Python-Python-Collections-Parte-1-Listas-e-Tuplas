from operator import attrgetter

from accounts import SalaryAccount


def __main__():
    acc1 = SalaryAccount(1)
    acc2 = SalaryAccount(2)
    acc3 = SalaryAccount(3)

    acc1.deposit(100)
    acc2.deposit(200)
    acc3.deposit(300)

    accounts = [acc2, acc3, acc1]

    for account in accounts:
        print(account)

    print()
    # The "attrgetter()" gets the attribute of the object inside the list, and compares with the same attribute of the
    # other object with "<"
    accounts = sorted(accounts, key=attrgetter("_balance"))

    for account in accounts:
        print(account)


if __name__ == "__main__":
    __main__()
