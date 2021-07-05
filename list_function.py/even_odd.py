myList = []
print("Enter limit: ")
s=int(input())
print("Enter elements of list")
for i in range(s):
    myList.append(int(input()))
print(myList)
evenList = []
oddList = []
size = len(myList)
for i in range(0, size):
    if(myList[i] % 2 == 0):
        evenList.append(myList[i])
    else:
        oddList.append(myList[i])
print(evenList)
print(oddList)
print(f"There were {len(evenList)} Even Numbers in the first list and {len(oddList)} Odd Numbers in the first list")