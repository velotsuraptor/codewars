class Blahh():
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Blahh(self.x+self.y)
    def __repr__(self):
        return str(self)

first = Blahh(5,8)

print(first)

