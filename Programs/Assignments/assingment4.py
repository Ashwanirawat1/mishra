# 1-: Write a function to check if the number is prime

def prime(num):
    if num>1:
        for i in range(2,num):
            if num%2 == 0:
                print(f"{num} is not prime")
                break
        else:
            print(f"{num} is prime")

prime(5)


# 2-: Write a method that return the last digit of an integer.
# Example --> the call of get_last_digit (3572) should return 2


num = 3572
def last_digit(num):
    return num%10
print(last_digit(3572))


# 3-: Make a function named tail that takes a squence(like a list, string, or tuple) and a number n nad return the last n element from the given sequence , as a list

def tail(sequence, n):
    return list(sequence[-n:])
print(tail("hello", 1))

 # 4-: write function named is _perfect_square that accept a number and return True if it's a perfect square and False if it's not.

import math

def _perfect_square(num):
    if num>=0:
        square = int(math.sqrt(num))
        if (square*square == num):
            print(f"{num}  is perfect square")
        else:
            print(f"{num} is not perfect square")

_perfect_square(24)

# or

def perfect_square(int):
    return math.isqrt(int)**2 == int
print(perfect_square(36))

 # 5-: write a function which returns the sum of lengths of all the iterables

l = [1, 2, 3, 4]
t = [4, 5, 6]
def func(l1, t1):
    return(len(l1)+len(t1))
print(func(l, t))



#How to check if a given number is Fibonacci number

def fibo(int):
    a = 0
    b = 1
    while(a<=int):
        if a == int:
            return f"{int} is a fibonacci series"
        c = a+b
        a,b = b,c
    else:
        return f"{int} is not a fibonacci series"
print(fibo(5))