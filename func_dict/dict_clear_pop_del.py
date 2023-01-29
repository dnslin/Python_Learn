example_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# clear 清空字典
example_dict.clear()
print(example_dict)

# pop 删除指定 key
example_dict_pop = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

example_dict_pop.pop('a', None)
print(example_dict_pop)

# del 删除指定 key 或者删除整个dict
del example_dict_pop['b']
print(example_dict_pop)

del example_dict_pop