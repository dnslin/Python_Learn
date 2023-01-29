class Person(object):
    def __init__(self, name: str, age: int, cry: str):
        self.name = name
        self.age = age
        self.__cry = cry

    def __str__(self):
        return "my name is %s, I am %d years old" % (self.name, self.age)

    def run(self):
        print("run my name is %s, I am %d years old" % (self.name, self.age))

    # 私有方法不可外部调用
    def __cry(self):
        print("%s my name is %s, I am %d years old" % (self.__cry, self.name, self.age))


person = Person(name="John", age=20)
person.run()
