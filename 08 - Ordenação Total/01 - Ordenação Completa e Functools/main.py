from operator import attrgetter

from accounts import SalaryAccount


def __main__():
    acc1 = SalaryAccount(1)
    acc2 = SalaryAccount(2)
    acc3 = SalaryAccount(3)

    acc1.deposit(100)
    acc2.deposit(200)
    acc3.deposit(200)

    accounts = [acc3, acc1, acc2]

    for account in accounts:
        print(account)

    print()

    # The second parameter (in this case), is the tie-breaking factor, case the first is the same in two objects
    for account in sorted(accounts, key=attrgetter("_balance", "_code")):
        print(account)

    print()
    print(acc1 == acc2)
    print(acc1 <= acc2)
    print(acc1 >= acc2)


if __name__ == "__main__":
    __main__()
