# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# # Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types
#  listed above. Iterate through each command in order and perform the corresponding operation on your list.



N = int(input())
ls = []
for i in range(N):
        odr = input().split()
        if odr[0]=='insert':
            ls.insert(int(odr[1]), int(odr[2]))
            
        elif odr[0]== 'append':
            ls.append(int(odr[1]))
            
        elif odr[0]=='print':
            print(ls)
            
        elif odr[0]=='remove':
            ls.remove(int(odr[1]))
            
        elif odr[0]=='pop':
            ls.pop()
            
        elif odr[0] == 'reverse':
            ls.reverse()
            
        elif odr[0]=='sort':
            ls.sort()
            
        else:
            print("invalid input!")
