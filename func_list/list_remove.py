example_list = [1, 2, 3, 4, 5, 1]
# 删除某个元素 如果元素不存在则报错 如果元素存在多个 则删除从左到右的第一个
print(example_list.remove(1))
print(example_list)

# del() 删除变量
del example_list

# print(example_list) NameError: name 'example_list' is not defined

# Path: func_list\list_remove.py

