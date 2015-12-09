student = {"labmeret": 45, "nev": "tibike", "kor": 8.5}
print(student["labmeret"])


students = [
    {"name": "tibi", "age": 6},
    {"name": "adorjan", "age": 9},
    {"name": "aurel", "age": 7},
    {"name": "dezso", "age": 12}
]

students_at_least_8 = []

for student in students:
    if student[ "age"] > 8:
        students_at_least_8.append(student["name"])


print(students_at_least_8)


students_name_starts_a = []

for student in students:
    if student[ "name" ][0] == "a":
        students_name_starts_a.append(student[ "name"])
print(students_name_starts_a)
