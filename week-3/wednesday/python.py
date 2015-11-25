def get_fizz(number):
    if number % 3 == 0:
        return"fizz"
    else:
        return number


def fizzbuzz(minimum, maximum):
    n = minimum
    while n <= maximum:
        print(get_fizz(n))
        n +=1

fizzbuzz(0, 50)
