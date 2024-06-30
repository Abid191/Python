def first_function() : 
    print('welcome to our first function')

first_function()  

def addition(x,y): 
    c = x+y 
    print(c)

addition(10,9)    


def calculate(x,y):
    a=x+y 
    b=x-y 
    c=x*y 
    d=x/y 
    return a,b,c,d 

sum,sub,mul,div = calculate(10,5) 
print('sum: ',sum, 'sub :',sub, 'mul :',mul,'div :',div)

