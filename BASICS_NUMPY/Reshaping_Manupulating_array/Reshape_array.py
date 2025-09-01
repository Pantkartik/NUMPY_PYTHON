'''
To reshape the dimension of array 
'''

# arr.reshape(rows,columns)


import numpy as np 
arr=np.array([10,20,30,40,50,60])

reshape_arr=arr.reshape(2,3)
print(reshape_arr)


# note
'''  Reshaping doesnot create a copy returns view changing valu in new shape array will change in old one  '''