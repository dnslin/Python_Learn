example_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# 伪列表
print(example_dict.keys())
# 伪列表转 list
print(list(example_dict.keys()))

# 直接获取KEY
print(example_dict['a'])

# GET 获取 key
print(example_dict.get('a'))

# 增加
example_dict['f'] = 6
print(example_dict)

# Path: func_dict\dict_all_key.py
