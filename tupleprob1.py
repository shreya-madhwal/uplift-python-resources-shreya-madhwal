"""
Lets' say we have four tuples and we have four list
Now, we need to write a program where we can have all those elements but in an alterate manner
but the twist is the user would choose the first set of elements
[1,2] [3,4] [5,6] [7, 8, 9]
(11,12) (13,14) (15,16) (17, 18, 19)
1 for list and 2 for tuple 
so, if the user says that i want 1 
then the entry will be 1 2 11 12 3 4 13 14 5 6 15 16 7 8 9 17 18 19
then the entry will be 1 2 11 12 3 4 13 14 5 6 15 16 7 8 9 17 18 19
"""
list1=[1,2]
list2=[3,4]
list3=[5,6]
list4=[7,8,9]
tuple1=(11,12)
tuple2=(13,14)
tuple3=(15,16)
tuple4=(17,18,19)
reslist=[]
list5=list(tuple1)
list6=list(tuple2)
list7=list(tuple3)
list8=list(tuple4)

def addlist(mylist,reslist):
    for i in range(len(mylist)):
        reslist.append(mylist[i])
    return reslist

    

print("Enter 1(for list) or 2(for tuple): ")
s=int(input())
if s==1:
    addlist(list1,reslist)
    addlist(list5,reslist)
    addlist(list2,reslist)
    addlist(list6,reslist)
    addlist(list3,reslist)
    addlist(list7,reslist)
    addlist(list4,reslist)
    print(addlist(list8,reslist))

elif s==2:
    addlist(list5,reslist)
    addlist(list1,reslist)
    addlist(list6,reslist)
    addlist(list2,reslist)
    addlist(list7,reslist)
    addlist(list3,reslist)
    addlist(list8,reslist)
    print(addlist(list4,reslist))

else:
    print("Invalid input")
    exit()



