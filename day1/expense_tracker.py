import csv
expenses = []


def add_expense():
    with open('expense_tracker.csv', 'a', newline='') as expense_file:
        fnames = ['Name', 'Cost', 'Category']
        expense_write = csv.DictWriter(expense_file, fieldnames=fnames)

        expense = {}
        expense['Name'] = input("Enter name of expense: ")
        expense['Cost'] = float(input("Enter cost of expense: "))
        expense['Category'] = input("Enter category of expense: ")
        expense_write.writerow(expense)


def view_expenses():
    with open('expense_tracker.csv', 'r') as expense_file:
        expense_reader = csv.DictReader(expense_file)

        for line in expense_reader:
            print(line)


def total_spendings():
    total = 0
    with open('expense_tracker.csv', 'r') as expense_file:
        expense_reader = csv.DictReader(expense_file)

        for line in expense_reader:
            total = total + float(line['Cost'])

        print(total)


def category_total():
    total = 0
    categ = input("Which category? ")

    with open('expense_tracker.csv', 'r') as expense_file:
        expense_reader = csv.DictReader(expense_file)
        for spendings in expense_reader:
            if (spendings['Category'] == categ):
                total = total + float(spendings['Cost'])

    print("Total in Category " + ": ", categ, total)


while True:
    print("1. Add Expense\n2. View Expenses\n3. Total Spendings\n4. Category Wise Spending\n5. Exit")

    try:
        task = int(input("Enter task number: "))

    except:
        print("Invalid input!")
        continue

    if (task == 1):
        add_expense()

    elif (task == 2):
        view_expenses()

    elif (task == 3):
        total_spendings()

    elif (task == 4):
        category_total()

    elif (task == 5):
        print("Exiting...")
        break

    if (task > 5 or task < 1):
        print("invalid response! ")
