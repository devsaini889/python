#Basic questions on functions in python

def Greatest(a,b,c):
    if(a> b and a> c):
        print(" a is greatest")
    elif(b> a and b> c):
        print("b is greatest")
    elif(c> a and c> b):
        print(" c is greatest ")
    else:
        print(" Any two number or all number is equal or any number is in negative")


Greatest(1,2,3)