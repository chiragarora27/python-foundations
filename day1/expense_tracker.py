expenses = []


def add_expense():
    expense = {}
    expense['Name'] = input("Enter name of expense: ")
    expense['Cost'] = float(input("Enter cost of expense: "))
    expense['Category'] = input("Enter category of expense: ")
    expenses.append(expense)


def view_expenses():
    if not expenses:
        print("No expenses added yet.")
        return

    for spendings in expenses:
        for key, value in spendings.items():
            print(key + ': ', value)

        print("\n")


def total_spendings():
    total = 0
    if not expenses:
        print("No expenses added yet.")
        return
    for spendings in expenses:
        total = total + spendings['Cost']

    print("Total spendings: ", total)


def category_total():
    total = 0
    if not expenses:
        print("No expenses added yet.")
        return
    categ = input("Which category? ")

    for spendings in expenses:
        if (spendings['Category'] == categ):
            total = total + spendings['Cost']

    print("Total in Category " + ": ", categ, total)


while True:
    print("1. Add Expense\n2. View Expenses\n3. Total Spendings\n4. Category Wise Spending\n5. Exit")
    task = int(input("Enter task number: "))

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
