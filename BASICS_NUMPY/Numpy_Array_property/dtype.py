'''

.dtype {  to find the data type of the element }

'''

import numpy as np 

array_check_data_type=np.array(['kartik','pant'])
print(f'The data type of array numpy is {array_check_data_type.dtype} ')



'''
to change the datatype we use 

'''
import numpy as np
change_data_type=np.array([1.2,45.2,32.89])
int_arr=change_data_type.astype(int)
print(int_arr,int_arr.dtype)
