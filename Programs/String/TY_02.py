# Create a Dictonary of char & its Index Pare. Where the index sholuld be consisting of all th index in which the charater is present

# Without using Induilt

String = "Malayalam"

d = {}
for index, char in enumerate(String):
    if char not in d:
         d[char] = [index]
    else :
         d[char] = d[char] + [index]      # d[char].append(index):
print(d)

# With using Inbuilt

from collections import defaultdict

dd = defaultdict(list)

for index, char in enumerate(String):
    dd[char] += [index]  # dd[char].append(index), dd[char] = dd[char]+[index]
print(dd)
