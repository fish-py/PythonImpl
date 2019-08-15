"""
有专门的变量保存列表的长度
所以 len(list) 是O(1)
"""

myList = [1, 2, 'a', True]

myList.insert(1, "insert")
myList.pop()

for item in myList:
    print(item)


for index, item in enumerate(['a', 'b', 'c']):
    print(index, item)
