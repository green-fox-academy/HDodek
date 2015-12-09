numbers = [3, 4, 5, 6, 7]

def filter_odd(my_list):
    output = []
    for i in my_list:
        if i % 2 == 0:
            output.append(i)
    return output

print(filter_odd(numbers))
