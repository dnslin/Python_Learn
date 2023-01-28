example_list = [1, 2, 3, 4, 5]
example_list_copy = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 合并 list 参数不会覆盖 只是合并
example_list.extend(example_list_copy)
print(example_list)
