# Get the Elements that are in List B but not in List A

a = [1, 2, 3, 4]
b = [1, 2, 3, 5]

for item in b:
    if item not in a:
        print(item, end="")