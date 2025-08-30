'''
using numpy to find the data visualization using array 

'''
import numpy as np 


# 0 D array
data=np.array(42)
print(data,type(data))


#  1 D array 
data_1d=np.array([43,12,67])
print(data_1d,type(data_1d))

# 2 D array 

data_2d=np.array([1,2,3],[4,5,6])
print(data_2d)


# 3 D array

data_3d=np.array([1,2,3],[4,5,6],[7,8,9])
print(data_3d)



#  to check the dimensions of the array 

print(data_3d.ndim)
print(data_2d.ndim)
print(data_1d.ndim)


