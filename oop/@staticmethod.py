"""
@staticmethod
表明这个方法是类的静态方法
"""


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def say_hello(name):
        print("你好啊 %s！" % name)


if __name__ == "__main__":
    Person.say_hello("李帅")
