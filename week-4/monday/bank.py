class Bank_account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount

    def receive(self, amount):
        self.balance += amount

    def print_balance(self):
        print ("balance of ")
        print(self.name)
        print("is")
        print(self.balance)

    def transfer(self, other_account, amount):
        self.pay(amount)
        other_account.receive(amount)

feri = Bank_account( "Feri", 700000)
szamla = Bank_account("Bela", 1000)
szamla.pay(50)

szamla.transfer(feri, 6000)
feri.print_balance()
szamla.print_balance()
