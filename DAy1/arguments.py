# example1

'''def func(i,j):
    print(i,j)


func(10,20) # postional arguments
func(j=10,i=20)  #  keyword arguemnts  we are explicitly giving the arguments'''


'''# Example2 # defaullt values assigned to postional arguments



def func(i=10, j=30):
    print(i, j)


func()
func(50,20)'''


# Example3 keyword arguemtns

#def greetings(name,greetmsg):
 #   print(greetmsg+"   "+name)


#greetings(name="siva",greetmsg="hello")


# Example4
def func(a,b,c):
    print(a,b,c)


func(10,20,30)
func(a=100,b=200,c=300)
func(10,20,c=30) ## thhis is logical error
#func(a=20,10,30  ## its invaild bcz keyword arguemetns only accesa after postional arguments
