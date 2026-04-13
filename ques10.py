"""
Running Sum on list
Write a program to print a list after performing running sum on it.

i.e:

Input:

list1 = [1,2,3,4,5,6]
Output:

[1,3,6,10,15,21]
"""
# l = input("Enter the number of elements in the list: ")
n = int(input("Enter the number of elements in the list: "))
list1 = []
for i in range (n):
    e = int(input("Enter a number: "))
    list1.append(e)
print("The list is: ", list1)
running_sum = []
current_sum = 0
for j in list1:
    current_sum += j
    running_sum.append(current_sum)
print("The running sum of the list is: ", running_sum)