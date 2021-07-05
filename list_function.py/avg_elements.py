  
myList = [62, 58, 25, 11, 39, 27, 34, 18]
count = 0
for i in myList:
    count += i
sumOfList = sum(myList)
# We can do this by either the sum function that takes the list as the argument and also we can do this by the count that we created using the for loop over our list
avg = sumOfList / len(myList)
print("Sum = {}".format(count))
print("Average = {}".format(avg))