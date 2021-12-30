def add(*args):
    total_sum = 0
    for number in args:
        total_sum += number
    return total_sum


print(add(3, 5, 6, 2, 1))


def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
