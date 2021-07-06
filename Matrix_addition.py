
'''
    Matrix Addition Problem
'''

x = [[5, 7, 3], [4, 10, 6], [7, 8, 9]]
y = [[1, 7, 3], [7, 5, 8], [3, 10, 9]]
add = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):             # Iterating through the rows
    
    for j in range(len(x[0])):      # Iterating through the column
        add[i][j] = x[i][j] + y[i][j]

print(add)

