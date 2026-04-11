# WAP to check a string is same while reversing
n = input("Enter a Text: ")
r = ""
for i in n:
    r = i + r
if r == n:
    print("Yeah it's a paranomal string")
else:
    print("No it's not")