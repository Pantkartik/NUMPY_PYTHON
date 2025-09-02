'''
to replace the nan numbers with a number 

'''

# default number is zero 


import numpy as np 

arr=np.array([1,2,3,np.nan,8,0,np.nan])

print(np.isnan(arr))
arr=np.nan_to_num(arr)
print(np.isnan(arr))
print(arr)