'''
to maths in al elements at once is broadcasting 

'''


#  getting discount in the data of 10% of each element 


price = [20,40,60,80,100]

discount= 10

final_prices=[]
for price in price:
    final_price=price-(price * discount/100)
    final_prices.append(final_price)

print(final_prices)



'''
we do this above with broadcasting 


#  get rid of for loop 
#  fast efficient codeing 

'''

import numpy as np 

price =np.array([10,20,30,40,50,60,70,80,90,100])

discount=10

price_after_discount=price-(price*discount/100)

print(price_after_discount)



'''
Rules of broadcasting 

1. Matching dimensions
   if the dimension of array 1 and 2 are same then the mathmatical operation will be applied
   
2. Expanding the elements
   if there is mathmatical operation in 2 array of different dimensions then the lowest dimension array element will perform the task with each element of other array 
   
3. Incompatible shapes
    the shape of array should me same 
    
    
    
    

'''




