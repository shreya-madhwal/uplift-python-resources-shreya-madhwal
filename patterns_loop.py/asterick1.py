'''
*
**
***
****
*****
'''
print("Enter number of lines: ")
s=int(input())
for i in range(0,s):
  for j in range(0,i+1):
    print("*",end="")
  print("\n")