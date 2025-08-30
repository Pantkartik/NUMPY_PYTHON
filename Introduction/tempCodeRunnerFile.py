list_temp=[35.6,56,51.9,90.0,12.4]

# lets find the average of the list 
total=0
for temp in list_temp:
    total+=temp
    avg=total/len(list_temp)
    
    print(avg)