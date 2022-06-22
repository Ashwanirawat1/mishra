# swap the case of given character

char = 'A'

def swap(char):
    if char.lower():
        return char.upper()
    elif char.isupper():
        return char.lower()
print(swap('A'))

# without Inbuilt

def swap_case(char):
    if ord ("a") <= ord ("z"):
        print(char(ord(char)-32))
    elif ord("A") <= ord("Z"):
        print(char(ord(char)+32))