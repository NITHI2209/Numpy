RESHAPED:
import numpy as np
arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape(2,3)
print("original arr:",arr)
print("reshaped arr:",reshaped)
original arr: [1 2 3 4 5 6]
reshaped arr: [[1 2 3]
 [4 5 6]]
reshaped = arr.reshape(3,2)
print("reshaped arr:",reshaped)
reshaped arr: [[1 2]
 [3 4]
 [5 6]]

import numpy as np
arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape(3,2)
reshaped [0][0] =100
print("original arr:",arr)
print("reshaped arr:",reshaped)
original arr: [100   2   3   4   5   6]
reshaped arr: [[100   2]
 [  3   4]
 [  5   6]]
NOTE: changes in reshaped value create changes in original value

RAVEL:
arr = np.array([[1,2,3],[4,5,6]])
print("original arr:",arr)
original arr: [[1 2 3]
 [4 5 6]]
ravel = arr.ravel()
print("ravel arr",ravel)
ravel arr: [1 2 3 4 5 6]
NOTE: changes in ravel value create changes in original value

FLATTEN:
similar to ravel()
But changes in flatten value doesnt change the value in original value unlike reshaped and ravel

