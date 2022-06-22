#check the data type is string or not


def check_string(string):
    if isinstance(string, str):
        return True
    return False

print(check_string("hello"))

############# OR #######################

def check_string_(string):
    return isinstance(string,str)

print(check_string_("hello"))