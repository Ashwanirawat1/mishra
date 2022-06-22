# print the longest word in the sentence

sentence = "Python is a Prgraming Language"
words = sentence.split()

# sorted()
res  = sorted(words, key = len)
print(res[-1])

# normal programe

longest =" "
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)