"""
作为函数式编程，Python肯定是支持闭包的
"""


def avg_factory():
    values = []

    def avg(value):
        values.append(value)
        return sum(values) / len(values)

    return avg


if __name__ == "__main__":
    avg1 = avg_factory()

    for i in range(10):
        print(avg1(i))


