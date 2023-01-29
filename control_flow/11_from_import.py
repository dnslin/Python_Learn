# 等于把random这个模块中的所有内容都导入到当前的命名空间中
from random import *
# 那么就可以直接使用模块中的内容 不需要加模块名
print(randint(1, 10))

# Path: control_flow\11_from_import.py
