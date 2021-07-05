'''
Print the Pattern
1 1 1 1 1
4 4 4 2 2
9 9 3 3 3
16 4 4 4 4
5 5 5 5 5
'''
for a in range(1,6):
  for i in range(1,6):
    if (i<6-a):
      print(a*a,end=" ")
    else:
      print(a,end=" ")
  print("\n")