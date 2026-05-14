class computation:
    def __init__(self):
        # self.num
        pass

    def Fraction(self, num1,num2):
        if num2 == 0:
            return "Error: Division by zero is not allowed:"
        else:
            return num1 / num2
    def natural_sum(self, n):
        if n < 0:
            print("Error: Input must be a non-negative integer.")
        else:
            total = 0
            for i in range(1, n+1):
                total = total + i
            return total
        
    def testPrime(self,num):
        if num <= 1:
            return "Error: Input must be an integer greater than 1."
        else:
            for i in range(2, num):
                if num % i == 0:
                    return f"{num} is not a prime number."
                else:
                    return f"{num} is a prime number."
    def tableMult(self, num):
        if num < 0:
            return f"{num} is a negative number. Please enter a non-negative integer."
        for i in range(1,11):
            print(f"{num} x {i} = {num * i}")
    def allTablesMult(self,num):
        if num < 0:
            return f"{num} is a negative number. Please enter a non-negative integer."
        else: 
            for i in range(1,num+1):
                if num % i == 0:
                    print(f"{i} is the factor of {num}.")
                else:
                    pass
    def prime_divisers(self, num):
        if num <= 1:
            return f"{num} is not a valid input. Please enter an integer greater than 1"
        else:
            for i in range(2, num):
                if num % i == 0:
                    for j in range(2,i):
                        if i % j == 0:
                            break
                        else:
                            print(f"{i} is a prime divisor factor of {num}")

obj1 = computation()
print(obj1.natural_sum(-1))
# print(obj1.testPrime(7))