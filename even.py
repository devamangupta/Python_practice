# Write a Python program to print the even numbers from a given list.
n = int(input("Enter how much number of elements you want: "))
l = []
for i in range(n):
    no = int(input("Enter a number for your list elements:"))
    # print("Enter a number for your list:")
    l.append(no)
print(l)
def even(l):
    n =[]
    for i in l:
        if i%2 == 0:
            n.append(i)
    
    return n
even_list = even(l)
print(even_list)

    
