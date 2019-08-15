"""
@property 是一个语法糖，它可以让我们
把方法调用写成属性的读写的形式
"""


class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    # 注意我的写法，名字要对应
    @full_name.setter
    def full_name(self, value):
        self.first_name = value.split(" ")[0]
        self.last_name = value.split(" ")[1]


if __name__ == "__main__":
    p1 = Person("Jon", "Snow")
    print(p1.full_name)

    p1.full_name = "Jon Targaryen"
    print(p1.last_name)
