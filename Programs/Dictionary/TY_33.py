# write program to get word as a key and similar value

sentence = "hello world welcome to python programming hi there"

d = {}
words = sentence.split()

for word in words:
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]].append(word)
print(d)

# default dict

from collections import defaultdict
dd = defaultdict(list)
for word in sentence.split():
    dd[word[0]].append(word)
print(dd)