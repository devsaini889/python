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

#Printing a square pattern
def hollow_square(size):
  
  for i in range(size):
    for j in range(size):
      if i == 0 or i == size - 1 or j == 0 or j == size - 1:
        print("*", end="")
      else:
        print(" ", end="")
    print()

size = 5
hollow_square(size)
