class computation:
    def __init__(self):
        pass

    def Fraction(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

    def natural_sum(self, n):
        if n < 0:
            return "Error: Input must be a non-negative integer."
        # Using the arithmetic series formula: n(n+1)/2
        return (n * (n + 1)) // 2

    def testPrime(self, num):
        if num <= 1:
            return f"{num} is not prime."
        if num == 2:
            return f"{num} is a prime number."
        if num % 2 == 0:
            return f"{num} is not a prime number."
        
        # Optimization: Only check up to the square root of num
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return f"{num} is not a prime number."
        return f"{num} is a prime number."

    def tableMult(self, num):
        if num < 0:
            return "Please enter a non-negative integer."
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

    def allFactors(self, num):
        """Returns all factors of a number."""
        if num <= 0:
            return "Please enter a positive integer."
        factors = []
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                factors.append(i)
                if i*i != num:
                    factors.append(num // i)
        return sorted(factors)

    def prime_divisors(self, num):
        """Finds prime factors using Trial Division."""
        if num <= 1:
            return "Input must be greater than 1."
        
        d = 2
        temp = num
        prime_factors = set()
        
        while d * d <= temp:
            while temp % d == 0:
                prime_factors.add(d)
                temp //= d
            d += 1
        if temp > 1:
            prime_factors.add(temp)
            
        for factor in sorted(prime_factors):
            print(f"{factor} is a prime divisor of {num}")

# Execution
obj1 = computation()
# print(f"Sum of natural numbers: {obj1.natural_sum(10)}")
print(obj1.natural_sum(-1))
# print(obj1.testPrime(7))
# obj1.prime_divisors(100)