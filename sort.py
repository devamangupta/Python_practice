# Write code here
l1 = [23,45,67,78,89,34]
l2 = [34,89,55,56,39,67]
common = list(set(l1) & set(l2))
print(common)
common.sort()
print(common)
