list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]

zip_list = zip(list1, list2, list3)

for item in zip_list:
    print(item)

# (1, 'a', True)
# (2, 'b', False)
# (3, 'c', True)
