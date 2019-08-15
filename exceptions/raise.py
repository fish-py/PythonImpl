def raise_exception(value):
    if value < 0:
        raise ArithmeticError("特性引用和赋值失败时会引发属性错误")
    elif value < 10:
        raise NameError("试图访问的变量名不存在")
    elif value < 100:
        raise KeyError("使用了映射中不存在的关键字（键）时引发的关键字错误")
    else:
        raise ValueError("值错误，传给对象的参数类型不正确")


raise_exception(-1)
