# Example1


'''class MyClass:
    def myfun(self):
        pass

    def diss(self,name):
        print(name)


mc1=MyClass()
mc2=MyClass()
mc1.myfun()
mc2.diss("siva")
print(mc1)
print(mc2)
print(mc1.myfun())
print(mc2.diss("siva vallabhasetti"))'''

# Example2

'''class MyClass:
    def m1(self):
        print("this is instance method")

    @staticmethod
    def m2(num):
        print(num)


mc = MyClass()
mc.m1()
mc.m2(100)
MyClass.m2(200)  

x, y = 10, 20


class MyClass:
    a, b = 100, 200

    def add(self, i, j):
        print(self.a + self.b)
        print(i+j)
        print(x+y)


mc= MyClass
mc1=mc()
mc1.add(50, 60)
print(mc1)'''

'''x, y = 10, 20


class MyClass:
    x, y = 100, 200

    def add(self, x, y):
        print(self.x + self.y)
        print(x+y)
        print(globals()['x']+globals()['y'])


mc = MyClass()
mc.add(50,60)'''

# method we can give any name
# method can take the arguments
# method can return the value
# we have to call the method using object


'''class MyClass:
    def __init__(self):
        print("this is constructor")
    @staticmethod
    def m1(self):
        print("hello")


#mc = MyClass()
print(MyClass.m1(100))


class MyClass:
    name = "siva"

    def __init__(self, name):
        print(name)
        print(self.name)


mc = MyClass("vallabhasetti")'''

# Example9
'''class Emp:
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def dispaly(self):
        print(self.eid, self.name, self.sal)


empployee = Emp(100, 'siva', 5000)
empployee.dispaly()'''


# Example10
class Emp:
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def __str__(self):
        return self.name

    def __int__(self):
        return self.eid


empployee = Emp(100, 'siva', 5000)

print(empployee)
