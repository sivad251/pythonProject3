class A:
    def m1(self):
        print("this is m1 method from class A ")


class B(A):
    def m1(self):
        print("this is m1 method from the class B")
        super().m1()


obj = B()
obj.m1()
