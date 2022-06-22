# String Palindrome

string = {"mom", "malayalam", "gmail", "madam", "apple", "dad", "wow", "google" }

palindrome = lambda string : f"{string} is palindrome" if string == string[::-1] else f"{string} is not palindrome"

print(list(map(palindrome, string)))