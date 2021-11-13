#!/usr/bin/
from functions import * 

#creates the complex numbers and calls addComplex, multiplyComplex and printComplex() from the functions module 
def main():

    c1=Complex(5,3)
    c2=Complex(i=-1,r=1)

    c3 = addComplex(c1, c2)
    printComplex(c3)
    printComplex(multiplyComplex(c1,c2))

if __name__ == "__main__":
    main()