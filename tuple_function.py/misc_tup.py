def read_list(newlist,n):
    s=n
    for i in range(s):
        e=int(input())
        newlist.append(e)
    print(newlist)
    return newlist

def read_list2(newlist,n):
    s=n
    for i in range(s):
        e=int(input())
        newlist.append(e)
    newtuple=tuple(newlist)
    print(newtuple)
    return newlist

def otpList(lis, tup):
    usIp = int(input("Enter 1 for tuple and 2 for list : "))
    if(usIp == 1):
        for i in range(8):
            if (i % 2 == 0):
                opList.append(tup[int(i / 2)])
            else:
                opList.append(lis[int(i / 2)])
    elif(usIp == 2):
        for i in range(8):
            if (i % 2 == 0):
                opList.append(lis[int(i/2)])
            else:
                opList.append(tup[int(i/2)])
    else:
        print("WRONG INPUT SORRY !!!")
        exit()
    return opList


list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
list8=[]


n1=int(input("Enter no. of elements in list1: "))
print("Enter elements:")
read_list(list1,n1)
n2=int(input("Enter no. of elements in list2: "))
print("Enter elements:")
read_list(list2,n2)
n3=int(input("Enter no. of elements in list3: "))
print("Enter elements:")
read_list(list3,n3)
n4=int(input("Enter no. of elements in list4: "))
print("Enter elements:")
read_list(list4,n4)
n5=int(input("Enter no. of elements in tuple1: "))
print("Enter elements:")
read_list2(list5,n5)
n6=int(input("Enter no. of elements in tuple2: "))
print("Enter elements:")
read_list2(list6,n6)
n7=int(input("Enter no. of elements in tuple3: "))
print("Enter elements:")
read_list2(list7,n7)
n8=int(input("Enter no. of elements in tuple4: "))
print("Enter elements:")
read_list2(list8,n8)


lis = [list1, list2, list3, list4]
tup = [list5, list6, list7, list8]
opList = []

print(otpList(lis, tup))

