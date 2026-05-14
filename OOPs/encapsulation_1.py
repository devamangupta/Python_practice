# Encapsulation is a fundamental concept in object-oriented programming (OOP) that refers to the bundling of data and methods that operate on that data within a single unit, typically a class. It is a way to restrict access to certain components of an object and protect the integrity of the data.
"""
We can hide our Data types by using __ before the variable name. This is called Name Mangling. It makes the variable private and it cannot be accessed directly from outside the class."""
class Car:
    def __init__(self, comapny, model, year):
        # In this time python store data like _Car__company, _Car__model, _Car__year
        self.__company = comapny
        self.__model = model
        self.__year = year
    def display_company(self):
        return self.__company
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
car1 = Car("Toyota", "Camry", 2020)
print(car1.display_company())  # Output: Toyota
car1._Car__company = "Honda"  # This will change the company name of car1 to Honda
print(car1.display_company())  # Output: Honda


"""
Python does not have true private variables, but by convention, a single underscore prefix (e.g., _variable) is used to indicate that a variable is intended for internal use and should not be accessed directly from outside the class. However, this is just a convention and does not enforce any access restrictions. And Python is for adult programmers, so it relies on the programmer's discipline to follow these conventions rather than enforcing strict access control like some other programming languages."""