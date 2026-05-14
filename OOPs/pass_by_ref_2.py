# class name customer with name, gender
class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
# Create a function to greet that customer
def Greeting(cus):
    if cus == "Male":
        print(f"Hello Mr. {cus.name}")
    else:
        print(f"Hello Ms. {cus.name}")
    cus2 = Customer("Bob", "Male")
    return cus2




# Here we are creating an object of the class customer and passing the name and gender
cus1 = Customer("Alice", "Female")
# Call the function with the object cus1
Greeting(cus1)
# new_cus = Greeting(cus1)
# print(new_cus.name)  # Output: Bob






"""
print(cus1.name)  # Output: Alice
print(cus1.gender)  # Output: Female
"""