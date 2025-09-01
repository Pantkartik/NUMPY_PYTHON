import numpy as np 

n=int(input('enter the number 1 to enter the matrix : '))
m=int(input('enter the number 2 to enter the matrix : '))
list_full=np.full((2,2),n,m)
print(list_full)