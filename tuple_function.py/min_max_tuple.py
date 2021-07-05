'''
   Min Max problem in tuple
   Example
   (6,7,15,9,4,8)
   (4,6,9,15)
'''
def minmax(mytuple):
    mylist=list(mytuple)
    reslist=[]
    mylist.sort()
    for j in range(2):
        reslist.append(mylist[j])
        reslist.append(mylist[-j-1])
    reslist.sort()
    restuple=tuple(reslist)
    return restuple

tuple1=(6,7,15,9,4,8)
print(minmax(tuple1))