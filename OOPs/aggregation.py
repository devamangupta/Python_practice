# Aggregation in Python
"""Aggregation is a concept in object-oriented programming where one class contains a reference to another class. It represents a "has-a" relationship between two classes. In aggregation, the contained class (the part) can exist independently of the containing class (the whole). This means that if the containing class is destroyed, the contained class can still exist."""
class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
class Address:
    def __init__(self, city, state, zip_code):
        self.city = city
        self.state = state
        self.zip_code = zip_code
# Create an address object
add = Address("New York", "NY", "10001")
# Create a customer object and pass the address object to it
customer = Customer("John Doe", "john.doe@example.com", add)
print("Here we get the memory address object of the address class which is used in the customer class")
print(customer.address) #Output:  The output will be the memory address of the address object.
# Access the customer's information
print(f"Now we try to print data of the customer object")
print("Customer Name:", customer.name)  # Output: Customer Name: John Doe
print("Customer Email:", customer.email)  # Output: Customer Email: john.doe@example.com
print("Customer Address:", customer.address.city, customer.address.state, customer.address.zip_code)  # Output: Customer Address: New York NY 10001