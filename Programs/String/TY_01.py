# Count the char in String

String = "Hello World"

# Count{}

d = {}

for char in String:
    d[char] = String.count(char)
print(d)

# Without Inbuilt Method

d1 = {}
for char in String:
    if char not in d1:
        d1[char] = 1
    else:
        d1[char] += 1
print(d1)

# Defaut dict()

from collections import defaultdict
dd = defaultdict(int)
for char in String:
    dd[char] += 1
print(dd)