"""
 Split String of list on K character.

Example :

Input:

['CampusX is a channel', 'for data-science', 'aspirants.']
Output:

['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']
"""
l = ['CampusX is a channel', 'for data-science', 'aspirants.']
result = []
for i in l:
    result.extend(i.split())
print(result)
