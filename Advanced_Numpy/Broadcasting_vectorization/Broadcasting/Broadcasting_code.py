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