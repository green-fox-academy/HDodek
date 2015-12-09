filename = "alma.txt"

def read_and_add_a(filename):
    read_file = open(filename)
    file_content = read_file.readlines()
    read_file.close()
    output = ""
    for line in file_content:
        print("a" + line.rstrip())

print(read_and_add_a(filename))


def read_and_add_a(filename):
    read_file = open(filename)
    file_content = read_file.read()
    read_file.close()
    for line in file_content.split("\n"):
        print("a" + line)

read_and_add_a(filename)

def read_and_add_a(filename):
    read_file = open(filename)
    file_content = read_file.read()
    read_file.close()
    output = ""
    for line in file_content.split("\n"):
        output += "a" + line + "\n"
    return output

print(read_and_add_a(filename))
