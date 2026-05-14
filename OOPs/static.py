# Here we learn about static/class variables in python
class Student:
    school_name = "ABC School"  # This is a static variable (class variable)
    __counter = 0

    def __init__(self, name, age):
        self.name = name  # This is an instance variable
        self.age = age    # This is an instance variable
        self.sno = Student.__counter # This is an instance variable
        Student.__counter += 1
    # We also create get and set methods for the counter variable
    @staticmethod
    def get_counter():
        return Student.__counter   
    @staticmethod
    def set_counter(value):
        if type(value) == type(Student._Student__counter):
            Student.__counter = value
        else:
            print("Invalid value")

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
print(student1.sno)  # Output: 0 which is the serial number of the student1
print(student2.sno)  # Output: 1  which is the serial number of the student2  
print(Student.get_counter())  # Output: 2 while we call init method two times so the counter is 2
print(student1.get_counter()) #Output: 2 we can also call the static method using the object
student1.set_counter(10) # We can also set the counter value using the set_counter method
print(Student.get_counter())  # Output: 10 after setting the counter to 10 using the set_counter method