'''
1.   .Ravel() ----> return views
2.   .Flatten()   ----> returns copy


when we want to convert multidemensional array into 1d array

'''
import numpy as np 

array_2d=np.array([[1,2,3],[4,5,6]])



# return view 
print(array_2d.ravel())

# returns copy 

print(array_2d.flatten())

