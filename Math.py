def power(x,y):
    i = 0
    s = 1
    while i < y:
        s = s* x
        i+=1
    print (s)

def tavan (x,y):
    power(x,y)


def times(x,y):
    return x* y
        
def divided(x,y):
    return x/y

def plus(x,y):
    return x+y

def minus(x,y):
    return x-y

def square(x):
    i = 2
    j = 0
    while i <= 10:
        if i*i == x:
            print(i)
            break
        else :
            i+=1
            
    if i > 20:
        while j < 100:
            if j*j > x:
                print(j)
                break
            else :
                j+=0.001
def radikal(x):
    square(x)

def jazr(x):
    square(x)
