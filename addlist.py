n = int(input("Enter a number of elements: "))
l = []
sum = 0
for i in range(n):
    e = int(input("Enter a number: "))
    l.append(e) 
print("The list is: ", l)
sum = 0
for i in range(n):
    sum = sum + l[i]
print("The sum of the list is: ", sum)