# 1. "Building a dict of word and length pair

from audioop import add
import numbers


words = "This is a bunch of words"

d = {word: len(word) for word in words.split()}
print(d)


    

# 2. Flipping keys and values of the dictionary using dict comprehension
d = {'a': 1, 'b': 2, 'c': 3}

dd = {value:key for key,value in d.items()}
print(dd)

# normal
d1 = {}
for key,value in d.items():
    d1[value] = key
print(d1)



# 3. Counting the number of each character in a String
my_string = 'guido van rossum'
d = {char : my_string.count(char) for char in my_string}
print(d)

# normal

di = {}
for char in my_string:
    if char not in di:
        di[char] = 1
    else:
        di[char] += 1
print(di)

# default dict
from collections import defaultdict

dd = defaultdict(int)
for word in my_string:
    dd[word] += 1
print(dd)



# 4. Counting the number of each character in a String
sentence = "hello world welcome to python hello hi world welcome to python"

# Comprihension

d = {char: sentence.count(char) for char in sentence}
print(d)

# Normal

de = {}
for char in sentence:
    if char not in de:
        de[char] = 1
    else:
        de[char] += 1
print(de)



# 5. Dictionary of character and ascii value pairs
s = 'abcABC'
d = {char: ord(char) for char in s}
print(d)

dic = {}
for char in s:
    dic[char] = ord(char)
# retrun(dict_)
print(dic)

# 6. Creating Dictionary of city and population pairs using Dict Comprehension

cities = ['Tokyo','Delhi','Shanghai','Sao Paulo','Mumbai']

population = ['38,001,000','25,703,168','23,740,778','21,066,245','21,042,538']

dict_ = {(citie, populations) for citie, populations in zip(cities, population)}
print(dict_)

# normal
# di = {}
# for city , populations in cities,population:
#     if city populations not in di:
#         di = zip(cities,population)
# print(di)


# 7. Create a dictionary of dialcode and country from the following list

dial_codes = [(86, 'China'),(91, 'India'),(1, 'United States'),(62, 'Indonesia'),(55, 'Brazil'),(92, 'Pakistan'),(880, 'Bangladesh'),(234, 'Nigeria'),(7, 'Russia'),(81, 'Japan')]

# Dictionary

d = {key :value for key, value in dial_codes}
print(d)

# normal
d1 = {}
for item in dial_codes:
        key, value = item
        d1[key] = value
print(d1)


# 8. 
#     1
#    12
#   123
#  1234
# 12345

pat = ""
for row in range(1, 6):
    pat = pat + str(row)
    print(f"{pat:>5}")
print()

# 9. 
#        1
#       12
#      123
#     1234
#    12345






# 10. 

# * 
# * * 
# * 
# * * * 
# * 
# * * * * 
# * 
# * * * * *

for row in range(2,6):
    print('*')
    print('* '*row)






# 11.

# 1 2 3 *
# 1 2 * 4
# 1 * 3 4
# * 2 3 4


l = ''
for j in range(1,5):
    for i in range(1,5):
        if i == 5-j:
            l = l+ ' *'
        else:
            l = l+ " " + str(i)
count = 0
for k in range(len(l)-1):
    print(l[0+count:8+count])
    count += 8

# second Way
i = 4
for row in range(1, 5):
    pat =''
    for j in range(1, 5):
        if j == i:
            pat = pat + " " + '*'
            i -= 1
        else:
            pat = pat+" "+ str(j)
    print(pat)



# Third Way

for i in range(1, 5):
    for j in range(1, 5):
        if i+j == 5:
            print("*", end ="")
        else:
            print(j, end ="")
    print()










# string = "Milan1 koliya2 Tester3"
# words = string.split()
# for char in words:
#     if numbers :
#         #num = numbers
#         print(sum(numbers))
