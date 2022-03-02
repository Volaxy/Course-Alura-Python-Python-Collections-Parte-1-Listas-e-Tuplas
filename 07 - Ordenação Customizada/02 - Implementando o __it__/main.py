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

    print(acc1 < acc2)

    for account in sorted(accounts):
        print(account)


if __name__ == "__main__":
    __main__()
