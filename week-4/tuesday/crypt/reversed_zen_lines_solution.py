my_file = open( "reversed_zen_lines.txt")

lines = my_file.readlines()


for line in lines:
    print(line[::-1], end="")

my_file.close()
