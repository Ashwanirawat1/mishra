# reverse the values in the dictonary if the value is string type



d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
#     else:
#         d[key] = value
# print(value)

d1 = {key: value[::-1] if isinstance(value, str) else value for key, value in d.items()}
print(d1)