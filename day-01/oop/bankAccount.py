class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount = 10000000):
        if amount < 0:
            print("Jumlah deposit Tidak Boleh Negatif")
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Saldo tidak mencukupi")
        else:
            self.balance -= amount
    def cek_balance(self):
        return self.balance
    def main(self, owner, balance):
        account = BankAccount(owner, balance)
        print(f"Owner : {account.owner}")
        print(f"Balance : {account.cek_balance()}")
        print(f"Balance : {account.deposit()}")
        print(f"withdraw : {account.withdraw(5000)}")


print(BankAccount("Naufal", 10000).main("Naufal", 10000))
