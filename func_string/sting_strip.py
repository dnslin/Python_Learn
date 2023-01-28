example_string = " abcdefghijklmnopqrstuvwxyz "
example_string_one = "abcdefghijklmnopqrstuvwxyz"

# 不传参 默认去掉两边空格
print(example_string.strip())
# 去掉两边的 “a”
print(example_string_one.strip('a'))

# 向左或者向右 去除对应字符串
print(example_string_one.lstrip('a'))

print(example_string_one.rstrip('z'))
