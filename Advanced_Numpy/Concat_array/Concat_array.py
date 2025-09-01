'''
concatatination of 2 or more numpy array


'''
#  axis 0 ----> vertical stacking 
#  axis 1 ----> horizontal stacking 


import numpy as np 

array=np.array([[1,2,3],[4,5,6]])
array2=np.array([[7,8,9],[10,11,12]])

array_concatenate=np.concatenate((array,array2),axis=0)
print(array_concatenate)