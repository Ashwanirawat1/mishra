import re


a = [1,2]
b = [3,4]

total = a[0] + a[1]
#print(total)

a[0] = a[0]+0.5
a[1] = a[1] + 0.5
#print(a[0])
#print(a[1])

x = a[0]
y = a[1]
a[0] = y
a[1] = x
#print(a)

a[0] = 0
a[1] = 0
#print(a)

class point:
    def __init__(self,a ,b):
        self.a = a
        self.b = b
    
    def move(self,dx,dy):
        self.a = self.a + dx
        self.b = self.b + dy

    def reset(self):
        self.a = 0
        self.b = 0
    
    def sort(self):
        if self.a > self.b:
            temp = self.a
            self.a = self.b
            self.b = temp

    def total(self):
        return self.a + self.b

p1 = point(1,2)
p2 = point(3,4)
p3 = point(5,6)

p1.move(0.1,0.1)
p2.move(0.5,0.5)
p3.move(1,2)

#print(p1.__dict__)
#print(p2.__dict__)
#print(p3.__dict__)

class calulator:
    def __init__(self, a,b) -> None:
        print(f"Calling __init__ method & saving {a} & {b}")
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b

c1 = calulator(10,20)
c2 = calulator(1,2)
c3 = calulator(15,25)

e1 = {"fname":"Steve", "lname":"Jobs","pay":1000}
e2 = {"fname":"Bill","lname":"Gates","pay":2000}

class Employee:
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    def email(self):
        return f"{self.fname}.{self.lname}@company.com"

    def pay_hike(self,percentage_hike):
        hike_amount = self.pay*percentage_hike
        self.pay = self.pay + hike_amount
        

e1 = Employee("Steve","Jobs",1000)
e2 = Employee("Bill","Gates",2000)

e1.pay_hike(0.1)
e2.pay_hike(0.05)
#print(e1.__dict__)
#print(e2.__dict__)


class point:
    def __init__(self, a=0, b=0, c=0) -> None:
        self.a =a
        self.b = b
        self.c = c

p1 = point()
p2 = point(1)
p3 = point(1, 2)
p4 = point(1, 2, 3)
p5 = point(a=10, b=20, c=30)
p6 = point(10, 20, c=30)
#print(p1.__dict__)
#print(p2.__dict__)
#print(p3.__dict__)
#print(p4.__dict__)
#print(p5.__dict__)
#print(p3.__dict__)

class point:
    def __init__(self, a=0, b=0,  c=0):
        self.a = a
        self.b = b
        self.c = c
    
    def __init__(self,a,b):
        self.a = a
        self.b = b

def add(a,b):
    return a+b

def add(a,b,c):
    return a+b+c
    
p1 = point()
p2 = point(1)
p3 = point(1,2)
p4 = point(1,2,3)

print(p4.__dict__)

