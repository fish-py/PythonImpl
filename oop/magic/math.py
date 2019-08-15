from math import hypot
# Return the Euclidean distance, sqrt(x*x + y*y).


class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    # 返回当前向量的摸
    def __abs__(self):
        return hypot(self.x, self.y)

    # 重写 + 加运算符
    # 这里其实发生了类型（信息）丢失，other就是按照Vector来的
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # 重写*元素符
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)







