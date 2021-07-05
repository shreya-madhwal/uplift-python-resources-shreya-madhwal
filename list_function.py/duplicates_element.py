
def dup_elem(x):
    size = len(x)
    dup_elements = []
    for i in range(size):
        for j in range(i+1, size):
            if x[i] == x[j] and x[i] not in dup_elements:
                dup_elements.append(x[i])
    return dup_elements

myList = [12,45,89,92,45,67,11,73,11,89,52,93,89,71]
print(dup_elem(myList))