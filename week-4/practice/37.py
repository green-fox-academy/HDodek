numbers = [7, 5, 8, -1, 2]

def minimal_element(my_list):
    min_number = my_list[0]
    for num in my_list:
        if min_number > num:
            min_number = num
    return min_number

print(minimal_element(numbers))
