# This is our first exercise and a calculator in python

a =  int(input(" Enter the first digit: "))
b= int(input("Enter the second digit: "))
c= str(input("Enter the operation: "))

if (c=="+"):
    print("The Addition of the numbers is:" , a+b)
elif(c=="-"):
    print("The subtraction of the number is:", a-b)
elif(c=="*"):
    print("The multiplication of the numbers is:", a*b)
elif(c=="/"):
    print("The division of the numbers is:", a/b)
elif(c=="%"):
    print("The Modulus of the numbers is:", a%b)
else:
    print("Invalid input")


