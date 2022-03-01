from abc import ABCMeta,abstractmethod


class Account(metaclass=ABCMeta):
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def deposit(self, value):
        self._balance += value

    @abstractmethod
    def month_passes(self):
        pass

    def __str__(self):
        return f"Code: {self._code}, Balance: {self._balance}"


class CheckingAccount(Account):
    def month_passes(self):
        self._balance -= 5


class SavingAccount(Account):
    def month_passes(self):
        self._balance *= 1.1
        self._balance -= 3
