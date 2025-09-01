'''
np.insert(array,index,value,asix=None)

array ---> original array
index ----> place where insertion is there
value ----> the values 
axis ---->  if none then inserted as flatted

# for 1 d array
axis = None

# for 2d array 
axis = 0,row wise
axis = 1,column wise

'''

#  to insert the element in an numpy array
import numpy as np 

array=np.array([[1,2,3],[4,5,6]])
array_inserted=np.insert(array,2,[[4,5,6]],axis=0)
print(array_inserted)

