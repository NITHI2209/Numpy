MATRIX MULTIPLICATION:
import numpy as np
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8],[9,10],[11,12]])
C = A @ B
print("C:",C)
C: [[ 58  64]
 [139 154]]
X = np.matmul(A,B)
print("x:",X)
x: [[ 58  64]
 [139 154]]
Y = np.dot(A,B)
print("Y:",Y)
Y: [[ 58  64]
 [139 154]]

INVERSE MATRIX:
import numpy as np 
from numpy.linalg import inv
A = np.array([[4,7],[2,6]])
inverse_A = inv(A)
print(inverse_A)
[[ 0.6 -0.7]
 [-0.2  0.4]]

DETERMINANCE:
import numpy as np
from numpy.linalg import inv,det
A = np.array([[4,6],[3,8]])
deter = det(A)
print("Deter:",deter)
Deter: 14.000000000000004
print("Deter:",int(round(deter)))
Deter: 14
