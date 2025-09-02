'''
for infinite numbers

np.isinf()   return boolean

'''

import numpy as np 

array_1=np.array([1,2,4,67,8,np.inf,66,89,2,np.inf])


# checking if there is any infinite number using the np.isinf(array_1)

print(np.isinf(array_1))


# for replacing the infinite to num 

array_2=np.nan_to_num(array_1,posinf=1000,neginf=-1000)   

# replace by 1000
print(array_2)