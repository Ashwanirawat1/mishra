# write function to convert a string to list & vice versa

s = 'hello word'

def convert(s):
    return list(s)

print(list(s))

def convert_list(list_):
    return " ".join(list_)
print()