# Print the Charecter & the no of occurence of that char in the String

# using string count

names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
d = {}

for char in set(names):
    d[char] = names.count(char)

print(d)

# without using inbuilt method

b = {}

for char in names:
    if char not in b:
        b[char] = 1
    else:
        b[char] += 1
print(b)

# default Dict

from collections import defaultdict
dd = defaultdict(int)
for char in names:
    dd[char] += 1

print(dd)