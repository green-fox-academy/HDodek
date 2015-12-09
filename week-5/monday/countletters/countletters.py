
def count_letters(input_string):
    output = {}
    for char in input_string:
        if not char in output:
            output[char] = 0
        output[char] += 1
    return output
