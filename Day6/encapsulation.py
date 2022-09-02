'''class myClass:
    __a = 10

    def disp1(self):
        print(self.__a)


obj = myClass()
obj.disp1()'''

'''class myClass:
    def __disp1(self):
        print("this is display1 method")

    def disp2(self):
        print("this is display2 method")
        self.__disp1()


obj = myClass()
obj.disp2()'''

'''class myClass:
    def disp1(self):
        print("this is firsst method")
    @staticmethod
    def disp2(self):
        print("this is second method")


myClass.disp2("siva vallabhasetti")'''


class A:
    def __dis1(self):
        print("this class a method1")

    def dis2(self):
        print("this is class a method2")


class B(A):
    def dis3(self):
        print("this is class b method 1")

    def dis4(self):
        print("this is class b method2")
        self.dis3()
        self.dis2()
        self._A__dis1()


obj = B()
obj.dis4()



