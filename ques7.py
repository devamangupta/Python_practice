# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
# output should be [['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]
l1 = ["M", "na", "i", "Kh"]
l2 = ["y", "me", "s", "an"]
L3 = []
for i in range(max(len(l1), len(l2))):
    if i < len(l1) and i < len(l2):
        L3.append([l1[i], l2[i]])
    elif i < len(l1):
        L3.append(l1[i])
    else:
        L3.append(l2[i])
print(L3)