"""
Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
Input:

['1ac21', '23fg', '456', '098d','1','kls']
Output:

['456', '23fg', '1ac21', '1', 'kls', '098d']
"""
l1 = ['1ac21', '23fg', '456', '098d','1','kls']
def product_value(s):
    product = 1
    for char in s:
        if char.isdigit():
            product *= int(char)
    return product

l1.sort(key=product_value, reverse=True)
print(l1)