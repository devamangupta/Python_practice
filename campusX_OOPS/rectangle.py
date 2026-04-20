class rectangle:
    def __init__(self,x,y):
        self.length = x
        self.width = y
    def parameter(self):
        return 2*(self.length + self.width)
    def area(self):
        return self.length*self.width
    def display(self):
        print(f"Length: {self.length}, Width: {self.width}")
        print(f"Parameter of rectangle is: {self.parameter()}")
        print(f"Area of rectangle is: {self.area()}")
        # return f"Length: {self.length}, Width: {self.width}"
rec1 = rectangle(10,20)
print(rec1.length)
print(rec1.width)
# print(rec1)
print(rec1.parameter())
print(rec1.area())
rec1.display()