example_string = "This is a string . ."
# find 找不到 返回 -1 index 找不到 会抛出异常
print(example_string.find("t"))

print(example_string.find("."))

print(example_string.find("b"))
print("----------------------------------------------------------------")
print(example_string.index("t"))

print(example_string.index("."))

print(example_string.index("b"))
