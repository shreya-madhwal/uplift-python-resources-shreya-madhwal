'''
Print the Pattern
1 1
4 4 4
9 9 9 9
16 16 16 16
25 25 25 25 25
'''
for a in range(1,6):
  for i in range(1,a+2):
    print(a*a,end=" ")
  print("\n")