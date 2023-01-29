# 差集
example_set = {'abcdefg', 'hijklmn', 'opqrst', 'uvwxyz'}

example_set_one = {'abcdefg', 'hijklmn', 'opqrst', 'uvwxyzs'}

example_set_two = {'hijklmn', 'opqrst', 'uvwxyz'}

print(example_set.difference(example_set_one))
print(example_set.difference(example_set_two))

# 交集
print(example_set.intersection(example_set_two))
# 并集
print(example_set.union(example_set_two))

# Path: func_set\sub_difference_union_intersection.py
