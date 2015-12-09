ag = "kuty"

def my_word(string):
    return string + "a"

ag = my_word(ag)
print(ag)



ag2 = ["cic", "kacs", "alm"]

for i in range(len(ag2)):
    ag2[i] = my_word(ag2[i])

print(ag2)
