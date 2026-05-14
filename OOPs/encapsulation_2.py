# Here we learn about encapsulation in python get and set method in python
# first we create a class name student
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter methods for displaying the private variables
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter methods for updating the private variables
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age

"""
We use these methods to access and modify the private variables of the class. This is a way to protect the integrity of the data and ensure that it is not modified in an unintended way. By using getter and setter methods, we can control how the data is accessed and modified, and we can also add validation logic to ensure that the data is valid before it is updated."""
student1 = Student("Alice", 20)
print(student1.get_name())  # Output: Alice
print(student1.get_age())   # Output: 20
student1.set_name("Bob")
print(student1.get_name())  # Output: Bob
student1.set_age(25)
print(student1.get_age())   # Output: 25