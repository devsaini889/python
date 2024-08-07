# Recursions

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
m = int(input("Enter the number for factorial: "))
print(factorial(m))

# Print the facnacci series

def series(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return series(n-1)+series(n-2)

def fabnacci(n):
    for i in range(n):
        print(series(i),end=" ")
    print()

n = int(input("Enter the number: "))
fabnacci(n)
