"""
x = input("Enter a string to check it's palandrom: ")
if x == x[::-1]:
    print(f"{x} is a palandrom...")
else:
    print(f"{x} is not a palandrom...")
"""
n = input("Enter a string: ")
def pala(n):
    reverse = ""
    for i in n:
        reverse = i + reverse
    if reverse == n:
        return f"{n} is a palandrom string"
    else:
        return f"{n} is not a palandrom string.."

print(pala(n))
