my_file = open( "reversed_zen_order.txt")

lines = my_file.readlines()

my_file.close()

reversed_lines = lines[::-1]

for line in reversed_lines:
    print(line.rstrip())
