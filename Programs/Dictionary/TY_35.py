# Replace value present in nested dictonary

d = {'a':100, 'b':{'m': 'man', 'n':'nose', 'a':'ox', 'c':'cat'}}
old_ = 'nose'
new_ = 'net'
def replace_dict(dict_, old_, new_):
    for key, value in d.items():
        if isinstance (value,dict):
            for k,v in value.items():
                if v == old_:
                    value[k] = new_
    return dict_
print(d)