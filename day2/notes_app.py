def add_note():
    with open('notes.txt', 'a') as source_file:
        source_file.write(input("Enter a note: ") + '\n')


def view_notes():
    with open('notes.txt', 'r') as source_file:
        for line in source_file:
            print(line)


def clear_notes():
    with open('notes.txt', 'w') as source_file:
        source_file.write("")


while True:

    print("1. Add note ")
    print("2. View notes ")
    print("3. Clear notes ")
    print("4. Exit ")

    choice = int(input("Enter your choice as a number: "))

    if (choice == 1):
        add_note()

    elif (choice == 2):
        view_notes()

    elif (choice == 3):
        clear_notes()

    elif (choice == 4):
        print('exiting...')
        break
    else:
        print("invalid choice!")
        continue
