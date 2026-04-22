n = int(input("Enter a number: "))

"""
if n <= 0:
    print(f"{n} is not a valid input. ")
else:
    for i in range(1, n+1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")
"""
def factor(n):
    if n <= 0:
        return f"{n} is not a valid input. Please enter a positive integer."
    else:
        for i in range(1,n+1):
            if n% i == 0:
                print(f"{i} is a factor of {n}")
            
        return f"Factors of {n} generated."

print(factor(n))