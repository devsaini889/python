# A program to calculate the avg of marks of student using the Oop concept

from itertools import tee


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum+=val
        
        print("hi",self.name,"Your avg score is", sum/3)


s1 = Student( "dev" , [55,60,90])
s1.avg_marks()