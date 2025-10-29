class BankAccount():
    __balance = None

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        print('Ваш баланс: ', self.__balance)

account1 = BankAccount()
account2 = BankAccount()
account3 = BankAccount()

account1.deposit(500)
account1.withdraw(200)
account1.get_balance()

account2.deposit(1000)
account2.withdraw(600)
account2.get_balance()

account3.deposit(800)
account3.withdraw(1)
account3.get_balance()