# 2. Python Program to Delete an Element From a Dictionary

my_dict = {11: 'a', 12: 'b', 13: 'c'}
def delete_an_element(element):
    del my_dict[element]
    print(my_dict)

delete_an_element(11)