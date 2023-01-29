example_list = [9, 2, 5, 4, 7, 6, 1, 3, 8]
# 接收三个参数 cmp 排序方案 key 排序依据 reverse 是否反向排序（true or false）
example_list.sort()
print("example_list =", example_list)

example_list.sort(key=lambda x: x % 3)

print("example_list =", example_list)

# Path: func_list\list_sort.py

