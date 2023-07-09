tuple1 = (11, [22, 33], 44, 55)

modified_list = list(tuple1)
modified_list[1][0] = 222
modified_tuple = tuple(modified_list)

print(modified_tuple)
