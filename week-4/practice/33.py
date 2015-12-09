numbers = [4, 5, 6, 7, 8]

def list(my_list):
    output = 0
    for i in my_list:
        output += i
    return output

numbers = list(numbers)
print(numbers)
