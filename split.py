"""
Write a Python function that accepts a hyphen-separated sequence of words as parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.
Example 1:

Input:

green-red-yellow-black-white
Output:

black-green-red-white-yellow
Example 2:"""
n = "green-red-yellow-black-white"
def sort_hyphen(s):
    words = s.split("-")
    words.sort()
    return "-".join(words)
print(sort_hyphen(n))   