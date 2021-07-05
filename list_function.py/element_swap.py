''' Swaping First and Last element of the list 
    Example:
    [24,45,56,67,89]
    [89,45,56,67,24]
'''

def swap1(mylist):
    temp=mylist[0]
    mylist[0]=mylist[-1]
    mylist[-1]=temp
    return mylist

def swap2(mylist):
    temp=mylist[0]
    mylist[0]=mylist[len(mylist)-1]
    mylist[len(mylist)-1]=temp
    return mylist

def swap3(mylist):
    a,*b,c=mylist
    mylist=[c,*b,a]
    return mylist

def swap4(mylist):
    mylist[0],mylist[-1]=mylist[-1],mylist[0]
    return mylist


#Driver Section

newlist=[]
print("Enter limit of list:")
s=int(input())
print("Enter elements: ")
for i in range(s):
    newlist.append(int(input()))
print(newlist)
print("List after swaping")
print(swap1(newlist))
print(swap2(newlist))
print(swap3(newlist))
print(swap4(newlist))
