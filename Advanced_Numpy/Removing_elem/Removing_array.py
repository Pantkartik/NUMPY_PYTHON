'''
np.delete(array,index of array,axis=None)

return a new array 

old array remain same 

'''


import numpy as np 
array=np.array([1,2,3])
print(array,"array before deletion ")

print(f"array after deletion : {np.delete(array,2,axis=0)}")
