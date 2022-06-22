# write Dictonary comprihension to find the longest word in the string

sentence = "python is a programing language and programing is fun"
words = sentence.split()
print(words)

d = {word : len(word) for word in words}

res = sorted(d.items() , key  = lambda item : item[-1])[-1]
print(res)