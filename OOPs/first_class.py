# Here we are going to learn objects, classes in python
# Create a class name car
class Car:
    # Create a constructor
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    # Create a method to display the car details
    def display(self):
        print(f"Car Brand_Name: {self.name}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")
class Hello:
    def __init__(self):
        print("Hello World")
    def display(self):
        print("This is my first class and we try to call it using object")
# Create an object for hello class
greeting = Hello() #This will call the constructor of the class and print "Hello World"

"""
# Create an object of the Car class
maruti = Car("Maruti", "Swift", 2026)
# Call the display method of the Car class
maruti.display()
"""