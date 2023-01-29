class Person(object):
    def __init__(self, name: str):
        self.__name = name

    @property
    def function(self):
        # property 修饰器 不能传参
        return 1

    def function_one(self):
        print("function_one")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


person = Person("dnslin")
# 不需要加括弧
print(person.function)
# 不能类调用
print(Person.function)

# 读取私有属性
print(person.name)

# 设置私有属性
# 类似于 java的 get set 方法
person.name = "dnslin—new"
print(person.name)

# Path: func_def\def_static.py
