n = int(input("Enter a number: "))
def dictonary(n):
    d = dict()
    for i in range(1, n+1):
        d[i] =i*i
    return d

print(dictonary(n))