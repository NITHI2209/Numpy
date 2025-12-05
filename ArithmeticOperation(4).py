Operation with same shape:
import numpy as np
a = np.array([10,20,30])
b = np.array([30,15,14])
print(a+b)
[40 35 44]
print(a-b)
[-20   5  16]
print(a*b)
[300 300 420]
print(b/a)
[3.   0.75   0.46666667]
print(b//a)
[3 0 0]

Operation with different shapes:
import numpy as np
a = np.array([1,2,3])
b = 5
print(a+b)
[6 7 8]

a = np.array([10,20,30])
b = np.array([[30,15,14],[1,2,3]])
print(a+b)
[[40 35 44]
 [11 22 33]]

a = np.array([10,20])
b = np.array([[30,15,14],[1,2,3]])
print(a+b)
  File "D:\Numpy\Numpy.py", line 36, in <module>
    print(a+b)
          ~^~
ValueError: operands could not be broadcast together with shapes (2,) (2,3) 


  



