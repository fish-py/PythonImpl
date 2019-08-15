"""
sorted函数可以将一个iterable进行排序
使用的时候我们需要传递一个函数作为排序规则
https://www.runoob.com/python/python-func-sorted.html
"""


# 自定义排序规则： 按照字符串的长度来排序
def key(item):
    return len(item)


if __name__ == "__main__":
    list1 = ["Java", "Python", "C", "Go", "C++"]

    list2 = sorted(list1, key=key)

    print(list2)
    # ['C', 'Go', 'C++', 'Java', 'Python']

