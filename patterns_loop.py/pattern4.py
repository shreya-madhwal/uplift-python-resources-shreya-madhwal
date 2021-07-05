'''
Print the Following Pattern
55551
44422
33333
24444
55555
'''
for a in range(1,6):
  for i in range(1,6):
    if (i<6-a):
      print(6-a,end=" ")
    else:
      print(a,end=" ")
  print("\n")