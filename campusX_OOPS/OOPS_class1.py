class MyFirstClass:
    def __init__(self):
        print("This is my first class")

# another class for my program
class MySecondClass:
    def __init__(self):
        print("This is my second class")
        self.my_method()

    def my_method(self):
        print("This is my method")
obj2 = MySecondClass()
print(obj2)
# print(obj2.my_method())
# obj1 = MyFirstClass()
# print(obj1)
# mmm