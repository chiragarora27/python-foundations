print("imported math\n")


def square(x):
    return x*x


def power(x, y):
    t = x
    while (y > 1):
        x = x*t
        y -= 1

    return x


def factorial(x):

    if (x == 0):
        return 1

    y = x-1
    while (y):
        x = x * y
        y -= 1
    return x
