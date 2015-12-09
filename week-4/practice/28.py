ac = ["kuty", "macsk", "cic"]
i = 0

while i < len(ac):
    ac[i] += "a"
    i += 1

print(ac)

-----

for i in range(len(ac)):
    ac[i] += "a"
