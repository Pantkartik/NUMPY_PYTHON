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

import numpy as np 

array=np.array([1,2,3])
array_insert=np.insert(array,2,5,axis=None)
print(array_insert)


# for 2 d array
array_insert_2d=np.insert(array,1,[5,6,7],axis=1)
print(array_insert_2d)

