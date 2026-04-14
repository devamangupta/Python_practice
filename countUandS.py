"""
sentance = "CampusX is an Online Mentorship Program fOr EnginEering studentS"
count_for_capital = 0
count_for_small = 0
count_for_space = 0
for i in sentance:
  if i.isupper():
    count_for_capital += 1
  elif i.isspace():
    count_for_space += 1
  else:
    count_for_small += 1
print("No. of upper case characters: ", count_for_capital)
print("No. of lower case characters: ", count_for_small)
"""
# Now we try to do this same program with the help of function 
def count(s):
    count_for_capital = 0
    count_for_small = 0
    count_for_space = 0
    for i in s:
        if i.isupper():
            count_for_capital += 1
        elif i.isspace():
            count_for_space += 1
        else:
            count_for_small += 1
    
    return count_for_capital,count_for_small
sentance = "CampusX is an Online Mentorship Program fOr EnginEering studentS"
print(count(sentance))