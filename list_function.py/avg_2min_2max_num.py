def avgminmax(mylist):
    mylist.sort()
    s=(mylist[1]+mylist[-2])/2
    return s

newlist=[]
print("Enter limit: ")
s=int(input())
print("Enter elements of list")
for i in range(s):
    newlist.append(int(input()))
print(f"The output is {avgminmax(newlist)}")