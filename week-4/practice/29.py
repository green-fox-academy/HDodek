ad = [3, 4, 5, 6, 7]
i = 0
summa = 0

while i < len(ad):
    summa += ad[i]
    i += 1

print(summa)

---

for n in ad:
    summa += n

print(summa)
