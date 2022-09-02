'''gloabal_var = 20


def func():
    local_var = 10
    print(local_var)
    print(gloabal_var)


func()
#print(local_var)  ## it is invalid because its local variable we can acces only inside of the function
print(gloabal_var)  ### it is valid global variables can acces within the func and outside of the function'''


#example2 :

'''xy = 200


def cool():
    global xy
   # global xy = 100   it is invalid syntax
    xy=100
    print(xy)


cool()  ### if name of the golbal and local variable are same function will call onely local variable not global variable
print(xy)'''


# Example4  gobal vaiable we can create inside the functiona and outside the function

def cool():
    global x
    x= 100
    print(x)


cool()
print(x)   ## we can get the global variable inside the function also










