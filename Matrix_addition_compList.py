#By comprehension list
x = [[5, 7, 3], [4, 10, 6], [7, 8, 9]]
y = [[1, 7, 3], [7, 5, 8], [3, 10, 9]]
add=[[],[],[]]

add=[[x[i][j]+y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
print(add)