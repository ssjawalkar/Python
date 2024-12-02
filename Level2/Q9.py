def access_list_element(my_list, index):
    try:
        element = my_list[index]  
    except IndexError:
        return "Index out of range"

my_list = [10, 20, 30, 40, 50]


print(access_list_element(my_list, 2)) 


print(access_list_element(my_list, 10)) 


