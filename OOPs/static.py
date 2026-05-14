# Here we learn about static/class variables in python
class Student:
    school_name = "ABC School"  # This is a static variable (class variable)

    def __init__(self, name, age):
        self.name = name  # This is an instance variable
        self.age = age    # This is an instance variable
# Create two student objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
# Access the static variable using the class name
print(Student.school_name)  # Output: ABC School
print(student1.school_name)  # Output: ABC School
print(student2.school_name)  # Output: ABC School
# Change the static variable using the class name
print(student1.name)  # Output: Alice
print(student2.name)  # Output: Bob