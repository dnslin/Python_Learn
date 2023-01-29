class Person(object):

    def __init__(self):
        pass

    @staticmethod
    def function(arg1: int, arg2: int):
        # 静态方法 无需实例化 但是也无法传递 self 和 cls
        return arg1 + arg2

    def function_one(self):
        print("function_one")


print(Person.function(1, 2))

# Path: func_def\def_classmethod.py
