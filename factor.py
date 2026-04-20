n = int(input("Enter a number:"))
if n < 0:
    print("Error: Input must be a non-negative integer.")
else:
    for i in range(1,n+1):
        if n % i == 0:
            print(f"{i} is the factor of {n}.")
        else:
            pass
