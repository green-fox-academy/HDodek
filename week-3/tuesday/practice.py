def greet(name):
    return "Hello, " + name

result = greet ("Dorka")
print(result)

g = []
def add (a, b):
    res = a + b
    g.append(res)
    return res

print (add(1, 2))
print (add(8, 4))
print (g)
