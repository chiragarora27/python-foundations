import math_utilis as m

try:
    task1 = int(input("Enter an integer: "))

except ValueError:
    print("invalid input!")

else:
    print("square = ", m.square(task1))
    print("cube = ", m.power(task1, 3))
    print("factorial = ", m.factorial(task1))
