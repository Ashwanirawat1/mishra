# find duplicate 


names = ['apple', 'google', 'apple', 'yahoo', 'google']

# count

for name in set(names):
    if name.count(name) > 1:
        print(name)

# without Inbuilt

res = []
dup = set()
for name in names:
    if name not in res:
        res.append(name)
    else:
        print(name)


from collections import Counter

c = Counter(names)
print(c.most_common())
print(c.most_common(1))

from collections import defaultdict
dd = defaultdict()
for name in names:
    dd[] += 1
print(dd)