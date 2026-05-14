# Here we create our own data type for fraction using class in python 
class Fraction:
    # Create a constructor for the fraction class
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den
        # This will call the display method of the class and display the fraction
        #self.display() 
    # Create a method to display the fraction by using magic method __str__ which will return the string representation of the fraction
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    # Create a method to display the fraction by using a normal method
    def display(self):
        print(f"{self.numerator}/{self.denominator}")
    # Create a method to add two fractions by using magic method __add__ which will take another fraction as an argument and return the sum of the two fractions
    def __add__(self, other):
        # To add two fractions we need to find the common denominator and then add the numerators
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)
    # create a method to add two fractions by using a normal method which will take another fraction as an argument and return the sum of the two fractions 
    def add(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)
# Create an object of the fraction class
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
# Display the fractions using the display method
f1.display()
f2.display()
# Add the two fractions using the add  magic method
sum_fraction = f1 + f2
# Add the two fractions using the add normal method
sum_fraction2 = f1.add(f2)
print(sum_fraction)
print(sum_fraction2)

# print(f1)