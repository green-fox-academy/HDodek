numbers = [3, 4, 5, 6, 7]

def reverse():
    output = []
    num = len(numbers) - 1
    while num >= 0:
        output.append(numbers[num])
        num -= 1
    return output

print(reverse())



def reverse2(input_list):
    output_list = []
    i = len(input_list) - 1
    while i >= 0:
        output_list.append(input_list[i])
        i -= 1
    return output_list

print(reverse2(numbers))
