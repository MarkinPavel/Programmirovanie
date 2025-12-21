my_list = [1, 2, 3]
print(my_list)

my_list[0] = 100
print(my_list)

my_tuple = (1, 2, 3)
print(my_tuple)

my_list = list(my_tuple)
my_list[0] = 100
my_tuple = tuple(my_list)
print(my_tuple)

my_string = "cat"
print(my_string)

my_string[0] = 'b'
print(my_string)