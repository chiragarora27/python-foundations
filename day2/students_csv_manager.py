import csv

with open('students_records.csv', 'a', newline='') as csv_file:

    fnames = ['name', 'marks', 'branch']

    csv_writer = csv.DictWriter(csv_file, fieldnames=fnames)

    while True:
        choice = int(input("Enter 1 if you want to add a student. 0 if not. "))

        if (choice == 0):
            print("ending...")
            break

        elif (choice != 0 and choice != 1):
            print("invalid choice!")
            continue

        elif (choice == 1):
            student = {}
            student['name'] = input("Enter name: ")
            student['marks'] = int(input("Enter marks: "))
            student['branch'] = input("Enter branch: ")

            csv_writer.writerow(student)


def print_students():
    with open('students_records.csv', 'r') as source_file:
        csv_reader = csv.reader(source_file)

        for line in csv_reader:
            print(line)


print_students()


def average_marks():
    with open('students_records.csv', 'r') as source_file:
        csv_reader = csv.reader(source_file)

        sum = 0
        n = 0

        for line in csv_reader:
            n += 1

        source_file.seek(0)

        for line in csv_reader:
            sum = sum + int(line[1])

        average = sum / n

        print(average)


average_marks()
