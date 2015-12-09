ab = [3, 4, 5, 6, 7]
i = 0

while i < len(ab):
    ab[i] *= 2
    i += 1

print(ab)

----
for i in range(len(ab)):
    ab[i] *= ab[i]
