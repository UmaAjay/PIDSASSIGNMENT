#6.5.1
# UMA AJAY KUMAR REDDY P S   19ETCS002134
import numpy as np

arr1 = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])  # creating 1-d array and initializing the elements
arr2 = arr1.reshape(2, 5)  # converting 1-d array to  2-d array using reshape
print("the 1-d array created is ", arr1)  # printing the 1-d array of size 10
print("dimension of resized array is ", arr2.ndim)
print("the 2-d array obtained is \n", arr2)
x1 = []  # creating emptylist to store common elements
x = np.array([1, 2, 3, 4, 15, 6, 7, 8, 9, 10])  # array1
y = np.array([1, 12, 13, 14, 15, 16, 17, 18, 19, 20])  # array2
print("1st array is ", x)
print("2nd array is ", y)
for i in range(len(x)):
    for j in range(len(y)):
        if (x[i] == y[j]):  # comparing the elements of one array are present in another array
            x1.append(x[i])  # if present append it to list

print("common elements are", x1)  # printing the common elements