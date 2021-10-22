dict_list= {'a':30,'u':80,'r':40} # a = key and 30 = value.
new_dict = {value:key for key ,value in dict_list .items()}
print (new_dict)


list_dict = {'a':3,'b':4,'c':5,'d':6,'e':7}
l1 = ['a','c','e']
new_dict={key:list_dict[key] for key in l1}
print(new_dict)
