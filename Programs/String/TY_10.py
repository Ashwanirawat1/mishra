# replace one string to another

s = 'hello world'
words = s.split()
old_word = 'world'
new_word = 'universe'
res = ''

for word in words:
    if word == old_word:
        res += new_word
    else:
        res += word + ' '
print(res)