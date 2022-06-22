# replace all repeted char with '_'

def repeted (string):
    res = " "
    for char in string:
        if string.count(char) > 1:
            res += "_"
        else:
            res += char
    return res
print(repeted('ashwani'))