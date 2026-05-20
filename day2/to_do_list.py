import csv


def add_task():
    with open('todolist.csv', 'a', newline='') as csv_file:

        fnames = ['S. No.', 'task', 'status']

        csv_writer = csv.DictWriter(csv_file, fieldnames=fnames)
        manager = {}
        manager['S. No.'] = int(input("Enter Serial Number of task: "))
        manager['task'] = input("Enter your task: ")
        manager['status'] = 'incomplete'

        csv_writer.writerow(manager)


def task_completion():
    with open('todolist.csv', 'r+') as csv_file:
        choice = int(input("Which task is completed? "))

        csv_reader = csv.reader(csv_file)
        n = 0

        for line in csv_reader:
            n += 1

            if (int(line[0]) == choice):
                line[2] = 'completed'
                writer = csv.writer(csv_file)
                writer.writerows(line)
            else:
                writer.writerows(line)


add_task()
task_completion()
