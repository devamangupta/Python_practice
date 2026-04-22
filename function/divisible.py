l = []
start = 2000
ending = 3200
def divisible(x,y):
    for i in range (x,y+1):
        if i % 7 == 0 and i % 5 != 0:
            l.append(int(i))
    return l

"""
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        l.append(int(i))
print(l)
"""
print(divisible(start,ending))