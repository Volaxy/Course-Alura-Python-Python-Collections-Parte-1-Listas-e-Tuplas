class SalaryAccount:
    def __init__(self, code):
        self.__code = code
        self.__balance = 0

    def deposit(self, value):
        self.__balance += value

    def __str__(self):
        return f"Code: {self.__code}, Balance: {self.__balance}"

    def __eq__(self, other):
        return self.__code == other.__code
