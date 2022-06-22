# write a function that takes veriable no of positional arguments as input, how to check that arguments that has to be passed are more than 5.

def func(*args):
    if len(args) > 5:
        return f"the pos arguments are {len(args)}"
    else:
        print("the pos argumrnts are less then 5")
print(func(1, 2, 3, 4, 5, 6))

