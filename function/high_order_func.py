"""
Python这个函数式一等公民，可以作为函数的参数或者返回值
"""


# 这里我们的函数接受另一个函数作为参数，用来
def filter_values(list_, filter_func):
    new_list = []
    for value in list_:
        if filter_func(value):
            new_list.append(value)
    return new_list


if __name__ == "__main__":
    list1 = [-1, 3, 4]

    def check(value):
        return True if value > 0 else False

    list2 = filter_values(list1, check)

    print(list2)
