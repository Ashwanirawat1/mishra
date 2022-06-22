# Create a list Comprihension to check no is prime or not

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

num = 8
for i in range(2, num):
    if num % i == 0 :
        l.append(False)
    else:
        l.append(True)

res =[]
for i in range(2, num):
    res.append(num%i)
print(res)


# without inbuilt

for i in l:
    sum_internal = 0
    for j in i :
        sum_internal += j
    res.append(sum_internal)
print(res)

# inbuilt
for i in l:
    res.append(sum(i))
print(res)

#  Using list comprehension
res = [sum(i) for i in l]
print(res)

# adding entire list

# for i in l:
#     for j in i:
#         sum_external += j
# print(sum_external)


# sum

res = sum([sum(i) for i in l])
print(res)