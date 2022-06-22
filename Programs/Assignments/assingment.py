# 1. "Write a Program to print the sum of entire list and sum of only internal list

# 	l = [[1,2,3],[4,5,6],[7,8,9]]




# 2. Write a list comprehension to get a list of even numbers from 1-50

l = [num for num in range(1, 51) if num % 2 ==0]
print (l)

# 3. "Write a program to find the duplicate elements in the list without using inbuilt functions

names = ['apple', 'google', 'apple', 'yahoo', 'google']
d = {}
for name in names:
    if name not in d:
        d[name] = 1
    else:
        d[name] += 1

for name, value in d.items():
    if value > 1:
        print(name, value)



# 4. "Write a program to count the number occurrences of each item in the list without using any inbuilt functions


names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']

d = {}

for name in names:
    if name not in d:
        d[name] = 1
    else:
        d[name] += 1
print(d)


# 5. "Write a program to find most common words in a given list.

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', 
            "don't", 'look', 'around', 'the', 'eyes', 'look', 'into','my', 'eyes', "you're", 'under']

d = {}
for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

n = sorted(d.items(), key = lambda item : item[-1])
print(n[-1:])
