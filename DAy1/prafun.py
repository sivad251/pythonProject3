'''def func():
    print("hello")


func()
print(func())


def func1(a,b):
    print(a,b)


func1(10,20)
print(func1(30,40))


def func(a, b):
    return a + b


func(10, 20)
print(func(10, 20))

global_var = 100


def func1():
    local_var = 200
    print(local_var)
    return local_var


func1()
print(func1())


xy = 200


def func():
    xy = 100
    print(xy)

func()
print(func())
print(xy) ### it is global variable because we can acc any where inside function and outside function'''

xy = 100


def func():
    global xy
    xy = 200
    print(xy)


func()
print(xy)  ### global variable is updated with the local variable bcz we mentioned global keyword


def func1(a, b, c):
    print(a, b, c)


func1(10, 20, 30)
func1(50, 60, 70)
func1(a=100, b=200, c=300)
func1(200, 300, c=400)
