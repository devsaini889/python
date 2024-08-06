#  a pattern for building mountain of stars

n = int(input("Enter the number of lines to be printed: "))
for i in range(0,n):
    for j in range(0,n-i-1):
        print( end=" ")
    for j in range(0,i+1):
        print("*" , end=" ")
    print()


# Pattern for printing pyramid of stars
n = int(input("Enter The number of rows:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*" , end=" ")
    print() 

#More pattern soon