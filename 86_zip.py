# zip() build in function in python

list1 = [1,2,3,4,5]
list2 = ['A','B','C','D']
tuple1 = ('man','woman','girl1','boy')
dict1 = {'name' : 'mohamed' , 'age' : 26 , 'country' : 'Egypt'}

for item1 , item2,item3,item4 in zip(list1,list2,tuple1,dict1):
    print('List 1 Item => ' , item1)
    print('List 2 Item => ' , item2)
    print('Tuple 1 Item => ' , item3)
    print('dict 1 Item => ' , item4 , 'Value => ' , dict[item4])
