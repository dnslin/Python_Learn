class Object(object):
    name = "faker"
    age = 27

    def run(self):
        print("my name is %s, I am %d years old" % (self.name, self.age))

    def going(self):
        print("my name is %s, I am %d years old" % (self.name, self.age))


obj = Object()
obj.run()
obj.going()

# Path: func_def\def_static.py
