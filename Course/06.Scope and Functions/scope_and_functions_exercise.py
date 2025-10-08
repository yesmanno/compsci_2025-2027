balance = 1000

def deposit(amount):
    balance = balance + amount
    print("Deposited", amount, "New balance:", balance)

def withdraw(amount):
    if balance >= amount:
        balance = balance - amount
        print("Withdrew", amount, "New balance:", balance)
    else:
        print("Insufficient funds!")

def bank_app():
    print("Welcome to your bank account!")
    deposit(200)
    withdraw(150)
    withdraw(1200)
    print("Final balance:", balance)

bank_app()