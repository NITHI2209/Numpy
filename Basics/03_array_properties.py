import numpy as np
arr = np.array([10,20,30])
arr2d = np.array([[10,20,30],[40,50,60]])
print(type(arr))
# <class 'numpy.ndarray'>
print(arr.size) # number of elements 
print(arr2d.size)
# 3
# 6
print(arr.shape) # to identify shape 
print(arr2d.shape)
# (3,)
#(2, 3)    ---> 2- no.of rows , 3 - no.of columns

print(arr.ndim) # to identify dimension
print(arr2d.ndim)
#1
#2

print(arr.dtype) # to identify data type
print(arr2d.dtype)
#int64
#int64

NOTE : If any one value in the arr or arr2d is float it convert all the value to float value 
int -> float -> str 
Datatype can be assigned 
arr2d = np.array ([[10,2,3],[3,4,5.1]] , dtype = int) 

Creating a array:
print(np.zeros((2,3)))
[[0. 0. 0.]
 [0. 0. 0.]]
print(np.ones((2,3)))
[[1. 1. 1.]
 [1. 1. 1.]]
print(np.full((2,3),10))
[[10 10 10]
 [10 10 10]]
print(np.zeros((2,3), dtype = int))
[[0 0 0]
 [0 0 0]]


