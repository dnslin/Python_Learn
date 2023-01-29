class Person(object):

    @classmethod
    def function(cls, arg1: int, arg2: int):
        # cls 即当前类 类似于 java 的 this
        return arg1 + arg2

    def function_one(self):
        print("function_one")


person = Person()
# 装饰器修饰
print(Person.function(1, 2))
# 实例化
person.function_one()

# 没有实例化 报错
Person.function_one()

# Path: func_def\def_classmethod.py

