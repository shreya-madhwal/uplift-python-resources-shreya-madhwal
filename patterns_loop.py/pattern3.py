'''
Print the Following Pattern
11115
22244
33333
42222
11111
'''
for a in range(1,6):
  for i in range(1,6):
    if (i<6-a):
      print(a,end=" ")
    else:
      print(6-a,end=" ")
  print("\n")