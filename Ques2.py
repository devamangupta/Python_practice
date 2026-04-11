# WAP to reverse a string
# n = input("Enter a string:")
# reverse_n = n[::-1]
# print(reverse_n)

# Reverse a string by using a loop 
text = input("Enter a text:")
r = ""
for i in text:
    r = i + r
print(r)