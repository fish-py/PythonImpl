class Monkey:
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(self.name, ": hello!")


monkey = Monkey("Jon Snow", 33)
monkey.say_hello()
# Jon Snow : hello!
