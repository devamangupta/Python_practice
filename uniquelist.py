"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Exercise 1:

Input:

[1,2,3,3,3,3,4,5]
Output:

[1, 2, 3, 4, 5]
"""

def unique_list(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x

l = [1,2,3,3,3,3,4,5]
print(unique_list(l))
