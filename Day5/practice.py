class A:

    def __init__(self):
        self.a = 2


class B(A):

    def __init__(self):
        A.__init__(self)
        print("calling member of protected class :", self.a)
        self.a = 3
        print(self.a)


obj1 = B()
obj2 = A()
print(obj1.a)
print(obj2.a)
