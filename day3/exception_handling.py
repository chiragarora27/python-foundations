try:
    task = int(input("Enter a number: "))
    task2 = int(input("Enter another number: "))
    task3 = task / task2

except ValueError as e:
    print("Not a number!")

except ZeroDivisionError:
    print("cannot divide by 0!")

else:
    print(task)
    print(task3)

finally:
    print("Anyways good code!")
