# check no is prime or not

num = 5
if num>1:
    for i in range(2, num):
        if num % i == 0:
            print( f"{num} is not prime no")
            break
    else:
        print(f"{num} is prime")



# in Range
for num in range(1, 10):
    if num>1:
        for i in range (2, num):
            if num % i == 0:
                break
        else:
            print(num)
        