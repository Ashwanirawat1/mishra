# check string is palindrome or not

str1 = "malayalam"

# using slicing
def palindrome(str1):
    res = ""
    for char in str1:
        res = char + res

    if res == str1:
        return True
print(palindrome("malayalam"))
    # return f"{string} is not a palindrome"
