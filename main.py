def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(a = 2)
print_params(a = 3, b = "не строка", c = False)
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [1,"строка", True]

values_dict = {'a' : 1, 'b' : 'строка', 'c' : True}

values_list_2 = [54.32, 'Строка']

print_params(*values_list)
print_params(**values_dict)
print_params(values_list_2)
print_params(*values_list_2, 42)