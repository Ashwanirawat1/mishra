# Create a dictonary of first char & the word starting with that first char pare in given sentence

Sentence = "Python is a programing language"

# Without Inbuilt

words = Sentence.split()
d = {}

for word in words:
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]] += [word]
print(d)

# DefaultDict

from collections import defaultdict

dd = defaultdict(list)
words = Sentence.split()
for word in words:
    dd[word[0]].append(word)

print(dd)