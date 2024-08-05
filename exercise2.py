import datetime

a= datetime.datetime.now()
m = int(a.strftime('%H'))
print('The date and time are: ',a)



if( m == 12):
    print("Good Morning Sir!")
elif(m> 12 and m<17 ):
    print(" Good Afternoon Sir!")
elif(m >17 and m<20):
    print('Good Evening Sir!')
elif(m>20):
    print('Good Night Sir!')
else:
    print('invalid input')
