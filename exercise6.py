# This is a program for playing KBC

print("WELCOME TO KBC")


Que=["Which of the following is the national animal of india ","Elephant" , "Dog", "Tiger","lion" ]
print(Que[0])
print(f" a:{Que[1]} \n b:{Que[2]} \n c:{Que[3]} \n d:{Que[4]} ")

correct_answer="c"
m = input("Enter your answer:")
if (m==correct_answer):
    print(" you win prize 5000")
    
else:
    print("your answer is wrong")
    exit()


Que2=["Which of the following is the capital of india? ", "Delhi" , "Mumbai", "Kolkata","Pune" ]
print(Que2[0])
print(f" a:{Que2[1]} \n b:{Que2[2]} \n c:{Que2[3]} \n d:{Que2[4]} ")

correct_answer="a"
m = input("Enter your answer:")
if (m==correct_answer):
    print(" you win prize 10000")
    
else:
    print("your answer is wrong")
    exit()

Que3=["Which of the following is the national bird of india? ","piegon" , "Hen", "peacock","sparrow" ]
print(Que3[0])
print(f" a:{Que3[1]} \n b:{Que3[2]} \n c:{Que3[3]} \n d:{Que3[4]} ")

correct_answer="c"
m = input("Enter your answer:")
if (m==correct_answer):
    print(" you win prize 25000")
        
else:
    print("your answer is wrong")
    exit()

Que3=["Which of the following is king of jungle of india? ","dog" , "lion", "sparrow","fox" ]
print(Que3[0])
print(f" a:{Que3[1]} \n b:{Que3[2]} \n c:{Que3[3]} \n d:{Que3[4]} ")

correct_answer="b"
m = input("Enter your answer:")
if (m==correct_answer):
    print(" you win prize 25000")
        
else:
    print("your answer is wrong")
    exit()
#can generate more questions like this