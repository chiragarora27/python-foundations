import datetime
import sys
import random

accounts = []


class BankAccount:
    no_of_accounts = 0
    test = 0

    def __init__(self, name, username, password, balance):
        self.name = name
        self.username = username
        self.password = password
        self.balance = balance

        BankAccount.no_of_accounts += 1

    def deposit_money(self, amount):
        self.balance = self.balance + amount

    def withdraw_money(self, amount):
        if (amount <= self.balance):
            self.balance = self.balance - amount
        else:
            print("insuffecient balance!")

    def balance_amount(self):
        return self.balance

    def transfer_money(self, other, amount):
        if (amount < self.balance):
            self.withdraw_money(amount)
            other.deposit_money(amount)
            print("Transaction successful!")
            return

        else:
            print("insuffecient balance! ")
            return

    @staticmethod
    def check_working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    @classmethod
    def accounts_population(cls):
        print(cls.no_of_accounts)

    @classmethod
    def default_accounts(cls):
        name = 'test' + str(cls.test)
        username = 'testusername' + str(cls.test)
        password = str(cls.test) + 'password'
        balance = random.randint(1000, 10000)

        holder = cls(name, username, password, balance)
        accounts.append(holder)
        cls.test += 1


def authenticate():
    username = input("enter username: ")
    password = input("enter password: ")

    for object in accounts:
        if object.username == username and object.password == password:
            return object
    return -1


def check_username(username):
    for account in accounts:
        if account.username == username:
            return account
    return True


my_day = datetime.date.today()

if (BankAccount.check_working_day(my_day) == False):
    print("Bank closed! ")
    sys.exit()

while True:
    print("Enter your choice: ")
    print("1. Add Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Balance")
    print("5. Create a default account")
    print("6. Transfer money")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid choice!")
        continue

    if (choice < 1 or choice > 7):
        print("Invalid choice!")
        continue

    else:
        if (choice == 1):
            name = input("enter name: ")
            username = input("enter username: ")
            if (check_username(username) != True):
                print("username not available")
                continue
            password = input("set password: ")
            try:
                balance = float(input("deposit money: "))
            except ValueError:
                print("invalid amount! ")
                continue
            if (balance <= 0):
                print("invalid amount!")
                continue

            holder = BankAccount(name, username, password, balance)
            accounts.append(holder)

        elif (choice == 2 or choice == 3):
            check = authenticate()
            if (check == -1):
                print("invalid credentials! ")
                continue
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("invalid amount!")
                continue
            if (amount <= 0):
                print("invalid amount!")
                continue

            if (choice == 2):
                check.deposit_money(amount)
            else:
                check.withdraw_money(amount)

        elif (choice == 4):
            check = authenticate()
            if (check == -1):
                print("invalid credentials! ")
                continue
            check.balance_amount()

        elif (choice == 5):
            BankAccount.default_accounts()
            for object in accounts:
                print(object.balance)

        elif (choice == 6):
            check = authenticate()

            if (check == -1):
                print("invalid credentials! ")
                continue

            username = input("Enter receiver username: ")
            check_2 = check_username(username)

            if (check_2 != True):
                try:
                    amount = int(input("Enter amomunt: "))
                except ValueError:
                    print("invalid amount!")
                    continue
                if (amount < 0):
                    print("invalid amount!")
                    continue
                BankAccount.transfer_money(check, check_2, amount)

            else:
                print("account not found!")

        elif (choice == 7):
            print("Exiting...")
            break
