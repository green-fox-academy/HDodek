names = ["Zakarias", "Hans", "Otto", "Ole"]

def shortest_name(my_name):
    output = my_name[0]
    for string in my_name:
        if len(output) > len(string):
            output = string
    return output

print(shortest_name(names))
