class Bank:

    def __init__(self, name, age, balance :float):
        """"""
        self.name = name
        self.age = age
        self.balance = balance

    def deposit(self, amount) -> None:
        """입금"""
        self.balance += amount

    def withdraw(self, amount) -> None:
        """출금"""
        self.balance -= amount

minjin = Bank("이민진", "21", 10000)

minjin.deposit(200)
minjin.withdraw(200)

print(minjin.balance)

help(Bank)