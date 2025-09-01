'''
To append the element 

'''

import numpy as np 

array=np.array([[1,2,3],[4,5,6]])
array_appended=np.append(array,[[7,8,9]],axis=0)

print(array_appended)