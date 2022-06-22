# WAF to print the below output
# func("TRACXN", 0) # should print RCN
# func("TRACXN", 1) # should print TAX


def func(string, value):
    if value == 0:
        return(string[1::2])
    elif value == 1:
        return(string[::2])

print(func("TRACXN", 0))
print(func("TRACXN", 1))


