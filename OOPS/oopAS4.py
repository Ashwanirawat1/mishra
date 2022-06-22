from multiprocessing.sharedctypes import Value


class Parent:
    def __init__(self, value):
        self.value = value
    
    def apple(self):
        print(f"Executing Parent Apple {self.value}")
    
    def google(self):
        print(f"Executing Parent Google")
        self.apple()

p = Parent(10)
#p.apple()
#p.google()



class child1(Parent):
    def __init__(self, value):
        super().__init__(value)

    def yahoo(self):
        print("Child1 Yahoo")

c = child1(10)
#c.yahoo()
#c.apple()
#c.google()

class child2(Parent):
    def __init__(self, value):
        super().__init__(value)
    
    def apple(self):
        print(f"Execting child2 Apple {self.value}")
    
c = child2(10)
#c.apple()
#c.google()

class child3(Parent):
    def __init__(self, value):
        super().__init__(value)

    def apple(self):
        print("Executing child3 Apple")
        super().apple()
    
c=child3(10)
#c.apple()

class child4(Parent):
    def __init__(self, value, extra_value):
        super().__init__(value)
        self.extra_value = extra_value

c = child4(10,20)
c.value
c.extra_value
c.apple()
c.google()

class Parent2:
    def __init__(self, a):
        self.a = a
    
    def facebook(self):
        print("Executing Parent2 Facebook")

class child5(Parent, Parent2):
    def __init__(self, x, y):
        Parent.__init__(self, x)
        Parent2.__init__(self, y)

    def whatsapp(self):
        print("Executing Child5 Whatsapp")

c = child5(10,20)
c.facebook()
c.apple()

class A:
    def demo(self):
        print ("a")
    
class B(A):
    def demo(self):
        print("B")
        A.demo(self)
    
class C(B):
    def demo(self):
        print("C")
        B.demo(self)

d = C()
d.demo()

class Parent:
    def spam(self):
        print("Parent Spam")

class Child1(Parent):
    def spam(self):
        print("Child1 Spam")
        super().spam()
    
class Child2(Parent):
    def spam(self):
        print("Child2 Spam")
        super().spam()
class Child3(Child1, Child2):
    pass

e = Child3()
e.spam()
Child3.__mro__

class Spam:
    a = 10
    def apple(self):
        print(f"Spam Apple {self.__class__.a}")

class Demo(Spam):
    a = 20
    def google(self):
        print("Google")

f = Demo()
f.apple()


