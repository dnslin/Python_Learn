example_string = "this is a string"
# 开始位是否是包含元素
print(example_string.startswith("this"))  # True
print(example_string.startswith("t"))  # True
print(example_string.startswith("i"))  # false

# 结束位是否是包含元素
print(example_string.endswith("string"))  # True
print(example_string.endswith("g"))  # True
print(example_string.endswith("b"))  # false
