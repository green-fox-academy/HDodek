class Car:
    def __init__(self, color, type, km):
        self.color = color
        self.type = type
        self.km = km

    def ride(self, km):
        self.km += km

tesla = Car("pink", "TeslaX", 1200)
tesla.ride(2300)

print(tesla.km)
