'''
Slicing is the method to get the part of the array 

'''

import numpy as np 
array=np.array([1,23,52,2])

# if we want to get the 1,23 we use slicing [0:2]  last number -1 we get the limit for slicing 

# print(array[0:2])



#  lets try for 2 d array 

array_2d=np.array([[1,2,3],[5,6,7]])

# print(array_2d[0:2][0:2])



# Reversing the 

print(array[::-1])