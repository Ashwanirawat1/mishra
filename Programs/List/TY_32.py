# print all maximum no present in list

number = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]

max_num = max(number)

for num in number:
    if num == max_num:
        print(num)


words = ['apple', 'walmart', 'flipkart', 'apple', 'walmart']

max_len = max(words, key=len)
for word in words:
    if len(max_len) == len(word):
        print(word)