# Build a list with only item having even no of character

names = ['amazon', 'gmail', 'walmart', 'flipkart', 'rediff']

for name in names:
    if len(name)%2 == 0:
        print([name ], end="")
print()

res = [name for name in names if len(name)%2 == 0]
print(res)