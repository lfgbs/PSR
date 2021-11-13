from collections import namedtuple

Complex=namedtuple('Complex', ['r', 'i'])

#receives two complex numbers ( a+bi and c+di ) and performs the sum
def addComplex(x,y):

    #parte real - (a+c)
    #parte imaginária - (b+d)
    
    complex_sum=Complex(x.r+y.r,x.i+y.i)

    return complex_sum

#receives two complex numbers ( a+bi and c+di ) and performs the multiplication
def multiplyComplex(x,y):
    
    #parte real - (ac-bd)
    #parte imaginária - (ad+bc)
    
    complex_multiplication=Complex(x.r*y.r-x.i*y.i,x.r*y.i+x.i*y.r)

    return complex_multiplication

#receives a tuple representing a complex number and prints it out in the a+bi form
def printComplex(x):
    if int(x.i)<0:
        print(x.r,x.i,"i")
        return
    if int(x.i)>0:
        print(x.r,"+",x.i,"i")
        return
    
    print(x.r)