# Create list of Integer where the no in l1 are raised to the power of the number present in l2

l1 = [1, 2, 3, 4, 5]
l2 = [0, 1, 4, 6, 2]
def exponent(n1,n2):
    return n1**n2
power = lambda n1, n2 : n1**n2
print(list(map(exponent,l1,l2)))

# ****************************************************************************

l1 = [1, 4, 9, 16, 25]
l2 = [1, 2, 81, 4096]
#print(zip(l1, l2))
print(list(zip(l1,l2)))

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from itertools import zip_longest
li = list(zip_longest(l1,l2))
print(li)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
lii = list(zip_longest(l1, l2, fillvalue=100))
print(lii)

#########################################################################################

list_ = list(range(1, 21))
def evens(num):
    if num%2 == 0:
        return num**2
print(list(filter(evens, list_)))