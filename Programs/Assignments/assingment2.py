# list Comprehensions

# 1. Square Numbers in the list. Using List 4_Comprehensions

nums = [1, 2, 3, 4, 5, 6, 7]

square = [num**2 for num in nums ]
print(square)


# 2. List of even numbers between range 1-50

l = [num for num in range(1, 51) if num%2 ==0 ]
print (l)

# 3. Returns a list names starting with vowels in the given string
names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']

vowel = [name for name in names if name[0] in 'aeiou']
print(vowel)

# 4. Filtering all the languages which starts with 'p'
languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']

startP = [language for language in languages if language[0] is 'P']
print(startP)

# 5. Names starting with consonants in list 
names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']
conso = [name for name in names if name[0] not in 'aeiou']
print(conso)

# 6. Filtering out those names which are less than 6 characters
names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']
less = [name for name in names if len(name)<6]
print(less)

# 7. Raise to the power of list index
a = [1, 2, 3, 4, 5]
power = [num**index for index, num in enumerate(a)]
print(power)

# 8. Build a list of tuples with string and its length pair
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

list_ = [(name,len(name))for name in names ]
print(list_)

# 9. Build a list with only with even length string
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
even = [name for name in names if len(name)%2 == 0]
print(even)

# 10. List comprehension to sum the factorial of numbers from 1-5
from math import factorial
fact = [factorial(num) for num in range(1,6)]
print(fact)

ct = [factorial(num) for num in range(1,6)]
print(sum(ct))

# 11. Reverse the item of a list if the item is of odd length string
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
odd = [name[::-1]for name in names if len(name)%2 ==1 ]
print(odd)

# 12. Reverse the item of a list if the item is of odd length string otherwise keep the item as is!.
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
rev = [name[::-1] if len(name)%2 == 1 else name for name in names]
print(rev)
