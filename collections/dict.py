dict1 = {
    "firstName": "Jon",
    "lastName": "Snow",
    "age": 33
}

"""
遍历dict
"""
for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for key, value in dict1.items():
    print(key, value)
