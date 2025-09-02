'''
using list comprehension 


'''


list1=[1,2,3,4,5,6]
list2=[1,2,3,4,5,6]


# using list comprehension 


list3=[x+y for x,y in zip(list1,list2)]
print(list3)