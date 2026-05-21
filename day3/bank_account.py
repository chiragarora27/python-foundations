import csv


def add_owner():
    name = input("enter name: ")
    username = input("enter username: ")
    count = 1

    while (count != 0):
        with open('data.csv', 'r') as file:
            file_reader = csv.DictReader(file)
            for entry in file_reader:
                if entry['username'] == username:
                    print("not available! try again: ")
                    username = input()
                else:
                    count = 0

    count = 1
    password = input("enter password: ")
    while (count != 0):
        if len(password) < 8:
            print("password not strong enough! try again: ")
            password = input()
        else:
            count = 0

    try:
        balance = int(input("deposit money: "))
    except ValueError:
        print("invalid amount!")

    with open("data.csv", 'a', newline='') as accounts_file:
        fname = ['name', 'username', 'password', 'balance']
        file_writer = csv.DictWriter(accounts_file, fieldnames=fname)

        details = {}
        details['name'] = name
        details['username'] = username
        details['password'] = password
        details['balance'] = balance

        file_writer.writerow(details)


def deposit():
    username = input("enter username: ")
    count = 0
    with open('data.csv', 'r') as file:
        file_reader = csv.DictReader(file)
        for entry in file_reader:
            if entry['username'] == username:
                count += 1
                break
            else:
                continue
    if (count == 0):
        print("no account exits! ")
        return
    password = input("enter password: ")

    count = 0
    with open('data.csv', 'r') as file:
        file_reader = csv.DictReader(file)
        for entry in file_reader:
            if (entry['username'] == username and entry['password'] == password):
                count = 1
                break
            else:
                continue

    if (count == 0):
        print("wrong password! ")
        return

    try:
        amount = float(input("enter amount: "))
    except ValueError:
        print("invalid amount! ")

    with open('data.csv', 'r') as file:
        file_reader = csv.DictReader(file)
        data = list(file_reader)

        for entry in data:
            if entry['username'] == username and entry['password'] == password:
                entry['balance'] = float(entry['balance']) + float(amount)

    fnames = ['name', 'username', 'password', 'balance']
    with open('data.csv', 'w', newline='') as file2:
        file_editor = csv.DictWriter(file2, fieldnames=fnames)
        file_editor.writeheader()
        for entry in data:
            file_editor.writerow(entry)


def withdraw():
    username = input("enter username: ")
    count = 0
    with open('data.csv', 'r') as file:
        file_reader = csv.DictReader(file)
        for entry in file_reader:
            if entry['username'] == username:
                count += 1
                break
            else:
                continue
    if (count == 0):
        print("no account exits! ")
        return
    password = input("enter password: ")

    count = 0
    with open('data.csv', 'r') as file:
        file_reader = csv.DictReader(file)
        for entry in file_reader:
            if (entry['username'] == username and entry['password'] == password):
                count = 1
                break
            else:
                continue

    if (count == 0):
        print("wrong password! ")
        return

    try:
        amount = float(input("enter amount: "))
    except ValueError:
        print("invalid amount! ")

    with open('data.csv', 'r') as file:
        file_reader = csv.DictReader(file)
        data = list(file_reader)

        for entry in data:
            if entry['username'] == username and entry['password'] == password:
                entry['balance'] = float(entry['balance']) - float(amount)

    fnames = ['name', 'username', 'password', 'balance']
    with open('data.csv', 'w', newline='') as file2:
        file_editor = csv.DictWriter(file2, fieldnames=fnames)
        file_editor.writeheader()
        for entry in data:
            file_editor.writerow(entry)


def balance():
    username = input("enter username: ")
    count = 0
    with open('data.csv', 'r') as file:
        file_reader = csv.DictReader(file)
        for entry in file_reader:
            if entry['username'] == username:
                count += 1
                break
            else:
                continue
    if (count == 0):
        print("no account exits! ")
        return
    password = input("enter password: ")

    count = 0

    with open('data.csv', 'r') as file:
        file_reader = csv.DictReader(file)
        for entry in file_reader:
            if entry['username'] == username and entry['password'] == password:
                count = 1
                break
            else:
                continue
    if (count == 0):
        print("no account exits! ")
        return
    password = input("enter password: ")

    for entry in file_reader:
        if entry['username'] == username:
            print(entry['balance'])


while True:
    print("Enter your choice: ")
    try:
        print("1. Add Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid choice!")
        continue
    except choice < 1 or choice > 5:
        print("Invalid choice!")
        continue

    else:
        if (choice == 1):
            add_owner()
        elif (choice == 2):
            deposit()
        elif (choice == 3):
            withdraw()
        elif (choice == 4):
            balance()
        elif (choice == 5):
            print("Exiting...")
            break
