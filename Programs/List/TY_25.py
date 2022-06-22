# Merge two list

l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(l1+l2)

l3 = [*l1, *l2]
print(l3)



# Using Chain Function

from itertools import chain
res = chain(l1, l2)
print(res)