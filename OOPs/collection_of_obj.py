# Here we try to create a collection of objects in python by using list and try to print them 
class Customer:
    def __init__(Self, name, age):
        Self.name = name
        Self.age = age
    def intro(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
c1 = Customer("Alice", 30)
c2 = Customer("Bob", 25)
c3 = Customer("Charlie", 35)
customers = [c1, c2, c3]   
for i in customers:
    print(i.name, i.age)
    # i.intro()