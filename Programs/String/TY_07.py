## create a list of name starting with vowels

names = ['steve', 'eve', 'alex', 'john', 'alexa']

vowels = lambda name:name[0].lower() in "aeiou"
print(list(filter(vowels, names)))