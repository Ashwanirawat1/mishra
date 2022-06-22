
# 1-: sort a list in reverse OrderedDict
from itertools import count


names  = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'zomato']

l = [name[::-1] for name in names]

print(l)

li =[]
for name in names[::-1]:
    li.append(name)
print(li)

# nu = [num[::-1] for num in nums]
# print(nu)
nums = [2, 1, 3, 4, 5, 7]
le =[]
for item in nums[::-1]:
    le.append(item)
print(le)
print(sorted(le))






# 2-: sort a list based on their length
names  = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'zomato']
l = []

def sorting(names):
    l =sorted(names, key=len)
    return l

print(sorting(names))

 # or


print(sorted(names, key=len))



# 3-: sort a list based on the first character of each element
names  = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'zomato']
l =[]
# for char in names:
#     if char[0] in names:
#        l.append(sorted(name))
# print(l)

# for name in names:
#     l.append(name[0])
print(sorted(names))


# 4-: sort a list based on the last character of each element
names  = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'zomato']
l = []

print(sorted(names, key=lambda item:item[-1] ))

# 5-: sort th dictonary based on the key
price = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}

print(sorted(price.items(),key =lambda item:item[0]))


# 6-: sort th dictonary based on the value
price = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
print(sorted(price.items(),key =lambda item:item[-1]))


# 7-: sort th dictonary based on the length of the key
price = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}

print()

# 8-: sort th dictonary based on the length of the value
price = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}

# 9-: sort th dictonary based on the last character of the key/value
price = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}


# 10-: sort th dictonary based on the first character of the key/value
price = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}