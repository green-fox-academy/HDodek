# 3 = 1 * 2* 3

def fact(numbers):
    output = 1
    i = 1
    while i <= numbers:
        output *= i
        i += 1
    return output

print(fact(6))


def fact(numbers):
    output = 1
    for i in range(1, numbers + 1):
        output *= i
    return output

print(fact(6))


def fact(numbers):
    if numbers == 1:
        return 1
    else:
        return fact(numbers - 1) * numbers

print(fact(6))
