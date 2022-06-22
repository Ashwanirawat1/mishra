# find longest non repeted word

sentence = "python is a programing language and programing is fun"

longest = " "
words = sentence.split()
for word in words:
    if len(word) > len(longest) and words.count(word) == -1:
        longest = word
print(longest)