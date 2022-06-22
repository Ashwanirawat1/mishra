# Write a lambda function to get square of given number

def square(num):
    return num**2
res = square(2)
print (res)

# Lambda Expression

square = lambda num : num**2
res = square(4)
print(res)


l = [1,2,3,4,5]
square = lambda num : num**2
op = []
for number in l:
    res : square(number)
    op.append(res)
print(op)

# Map classh
res = map(square, l)
print(list(res))