# convert string to comma seprated word

s = "hello welcome to python's world"

# replace

print(s.replace(" ", ","))

# split,join

word = s.split()
print(",".join(word))

# list()

char = list(s)
print(",".join(char))
