RANDOM NUMBERS
import numpy as np 
print(np.random.rand()) # prints any random number in float datatype
0.3722041943812293
print(np.random.rand(5)) # 5 indicates no.of elements in the array
[0.55453628 0.50135267 0.62848269 0.76184106 0.27541185]
print(np.random.randint(3)) # prints any random integer below 3
1
print(np.random.randint(2,10,5)) # print array of integer 2- lower limit , 10- higher limit , 5 no.of elements
[9 6 3 6 3]

RANDOM DISTRIBUTION:
1) NORMAL DISTRIBUTION:
print(np.random.normal(loc=50,scale=10,size=10)) # loc = average/mean , scale = Standard deviation , size = no.of inputs/data point
[59.38775455 55.48121519 51.01956367 37.88076245 39.6441901  44.4062516
 49.22644899 37.94572062 31.45870077 62.73280414]
2) UNIFORM DISTRIBUTION:
print(np.random.uniform(5,15,5)) # 5 = lower limit , 15 = higher limit , 5 = size
[11.24430962 14.3908925  11.59477724 10.60903673 13.08156431]

NOTE:
np.random.seed(10) -> reproduce the same value or input 
import numpy as np 
np.random.seed(10) 
print(np.random.rand()) 
# Gives the same output everytime



