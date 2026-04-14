"""
Add Space between Potential Words.
Example:

Input:

['campusxIs', 'bestFor', 'dataScientist']
Output:

['campusx Is', 'best For', 'data Scientist']
"""
l = ['campusxIs', 'bestFor', 'dataScientist']
N = []
for i in l:
    result = ''
    for j in i:
        if j.isupper():
            result += ' ' + j
        else:
            result += j
    N.append(result)
print(N)
m = []
for i in N:
    k = i.split()
    for j in k:
        m.append(j)
print(m)