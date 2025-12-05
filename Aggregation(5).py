Aggregation -> Aggregation in numpy refers to the process of computing summary statistics (such as sum,mean,max,min etc) over an array

Aggreation of 1 dimension:
import numpy as np 
arr = np.array([1,2,3,4])
print("Sum:", np.sum(arr))
print("Mean:",np.mean(arr))
print("Median:",np.median(arr))
print("Max:",np.max(arr))
print("Min:",np.min(arr))
print("Variance:",np.var(arr))
print("STD:",np.std(arr))
#output:
Sum: 10
Mean: 2.5
Median: 2.5
Max: 4
Min: 1
Variance: 1.25
STD: 1.118033988749895

Aggreation of 2 dimension:
arr = np.array([[1,2,3],[4,5,6]])
print("sum:",np.sum(arr,axis = 0))
sum: [5 7 9]
print("sum:",np.sum(arr,axis=1))
sum: [ 6 15]
axis = 0 # column wise
axis = 1 # row wise

Arithmetic operation with condition
arr = np.array([[1,2,3],[4,5,6]])
print("Sum:", np.sum(arr[arr>3]))
# Sum: 15

