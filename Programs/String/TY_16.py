# replace all the vowels in the given string with *

string = "hello world"

def vowels(str1):
    res = ""
    for char in str1:
        if char.lower() in "aeiou":
            res = res + "*"
        else:
            res += char
    return res
print(vowels(string))