# WA function to check if the number is prime

def prime(num):
    if num>1:
        for i in range(2,num):
            if num%2 == 0:
                print(f"{num} is not prime")
                break
        else:
            print(f"{num} is prime")

prime(5)