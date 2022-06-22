# group animal and flower in list 

items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']

d ={}
for item in items:
    name, grp = item.split('-')
    if grp not in d:
        d[grp] = [name]
    else:
        d[grp].append(name)

print(d)