'''

Change the data type of a given array to float.

'''

import numpy as np 

array=np.array([1,2,56])
array_float=array.astype(float)
print(array_float,array_float.dtype)