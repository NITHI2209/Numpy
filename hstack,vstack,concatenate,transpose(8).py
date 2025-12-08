hstack:
import numpy as np
arr = np.array([1,2,3,4])
arr1 = np.array([5,6,7,8])
print("Original array:",arr,arr1)
print("hstack arrary:",np.hstack([arr,arr1]))
Original array: [1 2 3 4] [5 6 7 8]
hstack arrary: [1 2 3 4 5 6 7 8]

vstack:
import numpy as np
arr = np.array([1,2,3,4])
arr1 = np.array([5,6,7,8])
print("Original array:",arr,arr1)
print("vstack array:",np.vstack([arr,arr1]))
Original array: [1 2 3 4] [5 6 7 8]
vstack array: [[1 2 3 4]
 [5 6 7 8]]

concatenate:
import numpy as np
arr = np.array([1,2,3,4])
arr1 = np.array([5,6,7,8])
print(np.concatenate([arr,arr1]))
[1 2 3 4 5 6 7 8]
import numpy as np
arr = np.array([[1,2],[3,4]])
arr1 = np.array([[5,6],[7,8]])
print(np.concatenate([arr,arr1]))
[[1 2]
 [3 4]
 [5 6]
 [7 8]]

Transpose:
import numpy as np
arr = np.array([[1,2],[3,4]])
print(arr.T)
[[1 3]
 [2 4]]
print(arr.T.T)
[[1 2]
 [3 4]]
