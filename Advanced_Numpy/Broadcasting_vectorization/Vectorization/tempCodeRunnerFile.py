list1=[1,2,3,4,5,6]
list2=[1,2,3,4,5,6]


list3= [x+y for x,y in zip(list1,list2)]

list3=[]
for list1,list2 in list1,list2:
    list=list1[list1]+list2[list2]
    list3=list3.append(list)


print(list)