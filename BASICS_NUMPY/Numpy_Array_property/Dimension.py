'''

To check the dimensions of the matrix 

.ndim

'''

import numpy as np

array_1d =np.array([1,2,3])
array_2d =np.array([[1,2,3],[4,5,6]])
array_3d =np.array([[[1,2,3],[4,5,6],[7,8,9]]])

print(array_1d.ndim,f'Dimension')
print(array_2d.ndim,f'Dimension')
print(array_3d.ndim,f'Dimension')

