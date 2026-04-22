num = int(input("Enter a number: "))
"""
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
"""
def tableMult(num):
    if num < 0:
        return f"{num} is a negative number. so reenter a non-negative integer."
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")
    return f"Table for {num} generated."

print(tableMult(num))