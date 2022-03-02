class SalaryAccount:
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def deposit(self, value):
        self._balance += value

    def __str__(self):
        return f"Code: {self._code}, Balance: {self._balance}"

    def __eq__(self, other):
        return self._code == other.__code

    # The "__lt__" is called when one object is compared to another
    def __lt__(self, other):
        return self._balance < other._balance
