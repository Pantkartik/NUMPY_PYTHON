'''
incompatible shapes lead to value error



'''


import numpy as np 

array1=np.array([[1,2,3],[4,5,6]])

array2=np.array([1,2])    # here the shape is 2 but the array 1 has shape 3 lead to error 

# print(array1+array2)



'''  To fix this we must use .reshape()'''
array1=np.array([[1,2,3],[4,5,6]])
array2=array2.reshape(2,1)
print(array1+array2)