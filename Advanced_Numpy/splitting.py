'''
np.split()  -----> for equal splitting
np.hsplit()  -----> for horiziontal splitting
np.vsplit()   -----> for vertical splitting



'''


import numpy as np 
array=np.array([[1,2,3,4],[5,6,7,8]])
# print(np.split(array,2))
print(np.hsplit(array,2))