# Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
l1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# for i in range(len(l1)):
#     if l1[i] == 6000:
#         l1.insert(i+1, 7000)
# print(l1)
# l1.insert(2, 7000)
l1[2][2].append( 7000)
print(l1)