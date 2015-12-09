from reverse import reverse_list

import os

print(reverse_list([1, 2, 3]))
print(os.getcwd())

alma_file = open( "alma.txt", "w")
print(alma_file.read())
alma_file.write( "eper" )
alma_file.close()
