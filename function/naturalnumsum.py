num = int(input("Enter a number:"))
# total = 0
def natural_sum(n):
    total = 0
    if n < 0:
        return "Error: Input must be a non-negative integer."
    else:
        for i in range(1,n+1):
            total = total + i
        return total
    
"""
for i in range(1,num+1):
    total = total + i
print(f"The sum of first {num} natural numbers is: {total}")
"""    
print(natural_sum(num))