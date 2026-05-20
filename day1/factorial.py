n = int(input("Enter a number: "))


def factorial(p):
    x = 1
    y = p

    if (p == 0):
        return 1

    while (x < p):
        y = y * x
        x += 1

    return y


print(factorial(n))
