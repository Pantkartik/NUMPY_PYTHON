'''
Insertion of a 2 d array 

'''

import numpy as np 
array_2d=np.array([[1,2,3],
                   [4,5,6]])

print(f'Array before insertion : {array_2d}')

array_2d_insert=np.insert(array_2d,1,[8,9,10],axis=0)

print(f'Array after insertion : {array_2d_insert}')
