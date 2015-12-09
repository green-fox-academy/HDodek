filename = "alma.txt"

def print_content(filename):
    file_to_print = open(filename)
    file_content = file_to_print.read()
    file_to_print.close()
    return file_content

print(print_content(filename))
