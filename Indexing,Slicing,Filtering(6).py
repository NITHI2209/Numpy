import numpy as np
arr = np.array([1,2,3,4,5])
arr2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

Indexing:
print(arr[1])
2
print(arr2d[1][0])
5

Slicing:
print(arr[1:4])
[2 3 4]
print(arr2d[1:3,2:4])
[[ 7  8]
 [11 12]]
print(arr[::])
[1 2 3 4 5]
print(arr2d[::])
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
print(arr2d[::-1])
[[ 9 10 11 12]
 [ 5  6  7  8]
 [ 1  2  3  4]]
print(arr2d[2:3:2,1:4:2])  
[[10 12]]

Boolean Indexing:
arr_bool = arr > 2
print(arr_bool)
[False False  True  True  True]
print(arr[arr_bool]) # shows value that is TRUE
[3 4 5]

Filtering: # direct filtering 
print(arr[arr>2])
[3 4 5]
print(arr[arr%2==0])
[2 4]
print(arr[(arr>2) & (arr< 6)])
[3 4 5]
print(arr2d[(arr2d>2)&(arr2d<5)])
[3 4]





