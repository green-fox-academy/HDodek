class SuperString(object):
    def __init__(self, my_greet):
        self.greet = greet

    def reversed(self):
        n = len(self.greet)
        reversed = ""
        for i in range(n):
            reversed = self.greet(i) + reversed
        return reversed
