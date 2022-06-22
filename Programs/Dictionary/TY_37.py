# Group file with same extensions

file = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']

d = {}
for item in file:
    name, grp = item.split('.')
    if grp not in d:
        d[grp] = [name]
    else:
        d[grp].append(name)

print(d)
