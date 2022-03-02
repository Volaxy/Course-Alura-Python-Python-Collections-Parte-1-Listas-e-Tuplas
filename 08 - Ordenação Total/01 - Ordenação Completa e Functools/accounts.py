from functools import total_ordering


# The "total_ordering" prevents us from creating a function "<=" to compare 2 objects
@total_ordering
class SalaryAccount:
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def deposit(self, value):
        self._balance += value

    def __str__(self):
        return f"Code: {self._code}, Balance: {self._balance}"

    def __eq__(self, other):
        return self._code == other._code

    def __lt__(self, other):
        return self._balance < other._balance
