example_set = {"1", "2", "3", "4", "5"}
# 增加元素 无序
example_set.add('6')
print(example_set)

# 更新元素
example_set.update('7')
example_set.update(["8", "9"])
print(example_set)

# 删除元素
example_set.remove('10')  # 不存在会报错
example_set.remove('9')  # 无返回

example_set.discard('10')  # 不存在不会报错

# 清空集合
example_set.clear()

# 删除集合

del example_set
