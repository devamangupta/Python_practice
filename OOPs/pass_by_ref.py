# Here we learn pass by reference in python
def modify_list(lst):
    lst.append(4)  # This will modify the original list passed as an argument       
my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
"""
In this example, we define a function modify_list that takes a list as an argument and appends the number 4 to it. When we call this function with my_list, it modifies the original list because lists in Python are mutable objects. This demonstrates that when we pass a mutable object (like a list) to a function, we are passing a reference to that object, and any modifications made to the object within the function will affect the original object outside the function.
However, if we were to pass an immutable object (like a string or a tuple) to a function, we would not see this behavior, as immutable objects cannot be modified after they are created. In that case, we would be passing a reference to the object, but since it cannot be modified, any changes would result in the creation of a new object rather than modifying the original one.
For example:
"""
def modify_string(s):
    s += " World"  # This will not modify the original string passed as an argument 
    print("Inside the function:", s)  # Output: Hello World
my_string = "Hello"
print("Outside the function:", my_string)  # Output: Hello
modify_string(my_string)
