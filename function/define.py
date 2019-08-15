"""
使用 def 关键字定义一个函数

函数属于callable的对象
"""


def hi():
    print("Hi")


def hello(name):
    """ 这是一段标准格式的注释，可以作为文档输出 """
    print("hello " + name)


# 执行函数
hi()
hello("Jon")

print(type(hi))
# <class 'function'>

print(hello.__doc__)
# 这是一段标准格式的注释，可以作为文档输出
