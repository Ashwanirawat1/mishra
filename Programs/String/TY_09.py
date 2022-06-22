# Reverse  the string Without Inbuilt Method

s = "hello world"

# Slicing
print(s[::-1])

# range()

for i in range(-1, -len(s)-1, -1):
    print(s[i], end="")

print()
# Concatation

res = ""
for char in s:
    res = char + res

print(res)