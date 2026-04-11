"""
WAP to solve the below equation till nth term and n provide by user
1 + x^2/2 + x^3/3 + x^n/n
"""
n = int(input("Enter a n:"))
sum = 1
eq = 1

for i in range(2,n+1):
    eq = (n**i)/i
    # sum = sum + eq
    sum = sum + eq
print(sum)