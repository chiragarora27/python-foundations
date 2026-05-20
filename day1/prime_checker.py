p = int(input("Enter a number: "))


def prime_check(n):

    if (n == 2):
        return True

    if (n % 2 == 0):
        return False

    x = n ** 0.5

    while (x > 0):
        if (n % x == 0):
            return False
        x -= 1

    return True


print(prime_check(p))
