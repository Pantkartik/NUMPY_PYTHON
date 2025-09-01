#  for entering the desired number in the matrix and the shape 


#  full(shape,value)


import numpy as np 

n=int(input('enter the number to enter the matrix : '))

list_full=np.full((2,2),n)
print(list_full)