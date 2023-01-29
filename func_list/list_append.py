# 数组 内容可以是任何类型的元素
example_list = [1, 2, 3, 4, 5]
example_list_copy = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# example_list.append(example_list_copy) # [1, 2, 3, 4, 5, [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
# append 是追加到结尾
for example in example_list_copy:
    example_list.append(example)
print(example_list)

# Path: func_list\list_append.py
