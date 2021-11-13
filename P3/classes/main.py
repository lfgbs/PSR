#!/usr/bin/
from collections import namedtuple

class Complex:
    def __init__(self, r, i):
        self.r=r
        self.i=i


    #receives two complex numbers ( a+bi and c+di ) and performs the sum
    def addComplex(self,x):

        #parte real - (a+c)
        #parte imaginária - (b+d)
        
        complex_sum=Complex(self.r+x.r,self.i+x.i)

        return complex_sum

    #receives two complex numbers ( a+bi and c+di ) and performs the multiplication
    def multiplyComplex(self,x):
        
        #parte real - (ac-bd)
        #parte imaginária - (ad+bc)
        
        complex_multiplication=Complex(self.r*x.r-self.i*x.i,self.r*x.i+self.i*x.r)

        return complex_multiplication

    #receives a tuple representing a complex number and prints it out in the a+bi form
    def printComplex(self):
        if int(self.i)<0:
            print(self.r,self.i,"i")
            return
        if int(self.i)>0:
            print(self.r,"+",self.i,"i")
            return
        
        print(self.r)

    #receives a tuple representing a complex number and prints it out in the a+bi form
    def __str__(self):
        if int(self.i)<0:
            return str(self.r)+str(self.i)+"i"
            
        if int(self.i)>0:
            return str(self.r)+"+"+str(self.i)+"i"
           
        return str(self.r)

#creates the complex numbers and calls addComplex, multiplyComplex and printComplex() from the functions module 
def main():

    c1=Complex(5,3)
    c2=Complex(i=-1,r=1)

    c3 = c1.addComplex(c2)
    print(c3)
    c4=c1.multiplyComplex(c2)
    c4.printComplex()

if __name__ == "__main__":
    main()