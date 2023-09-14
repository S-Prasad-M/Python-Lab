import numpy as np 
T = (1.1,2.2,3.3,4.4)
L= [[1.1,2.2,3.3],[4.4,2.2,5.5]]
arr=np.array(L) 
print("Ärray from list:",arr)
a = np.zeros((3, 4))
print("Array with 3x4 zeroes",a)
arr=np.array(T) 
print("Ärray from tuple:",arr) 
array = np.random.rand(3, 4)
print("2D Array filled with random values : \n", array)