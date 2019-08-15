"""
通过集合相关的魔法函数，可以让普通对象变成集合

类似于实现了Collection接口的效果
"""


class Company:
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def __getitem__(self, key):
        return self.employee_list[key]

    def __setitem__(self, key, value):
        self.employee_list[key] = value

    def __delitem__(self, index):
        del self.employee_list[index]

    def __contains__(self, item):
        return bool(self.employee_list[item])

    # 对当前对象使用len方法时其实会调用了它的__len__方法
    def __len__(self):
        return len(self.employee_list)


employ_list = ["Jon", "Snow", "Danny"]
company = Company(employ_list)

# 调用对象的 __getitem__ 方法
print(company[0])
# Jon

# 删除一个元素
# 调用对象的 __delitem__ 方法
del company[2]

# 调用对象的 __len__ 方法
print(len(company))
# 现在长度是2

# 修改元素的值
# 调用对象的 __setitem__ 方法
company[1] = "Targaryen"

for item in company:
    print(item)
# Jon
# Targaryen
