students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]
# create a function that takes a list of students,
# then returns how many candies are own by students
# under 10

def how_many_candies(children_list):
    candy_count = 0
    for student in children_list:
        if student[ "age" ] < 10:
            candy_count += student[ "candies"]
    return candy_count

print(how_many_candies(students))
