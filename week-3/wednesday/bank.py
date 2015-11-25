class Bankaccount():
    def __init__(self, name, start_balance):
        self.balance = 0
        self.name = name
        self.start_balance = start_balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
