#def greet(name, hi = "Hello"):
#    print(hi + ", " + name)
#
#greet("Dorka" , "hello")
#greet("Dorka" , "hy")


def add(a, b, res = None):
    if res is None:
        res = []
    r = a + b
    res.append(r)
    print(res)
    return r

add(1, 2)
add(3, 4)
add(5, 6)
