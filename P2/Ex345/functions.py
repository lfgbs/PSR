from math import sqrt
import readchar

#prints all chars up to the given stop_char, according to the ascii table
def printAllPreviousChars():
    print("Press the desired stop_char")
    stop_char = readchar.readchar()
    for i in range (ord(' '), ord(stop_char)+1):
        print(chr(i))

#receives a stop_char and will then accept chars until one of them matches stop_char
def printAllCharsUpTo(stop_char):
    print("The stop_char chosen was " + str(stop_char))
    pressed_keys=''

    pressed_key=readchar.readchar()

    while ord(pressed_key)!=ord(stop_char):
        if pressed_keys=='':
            pressed_keys=pressed_key
        else:
            pressed_keys=pressed_keys+pressed_key

        pressed_key=readchar.readchar()

    print(pressed_keys)


#receives a stop_char and will then accept chars until one of them matches stop_char, it will then return the number of numerical chars and non-numerical chars
def countAllNumbersUpTo(stop_char):
    print("The stop_char chosen was " + str(stop_char))

    pressed_keys=[]
    
    pressed_key=readchar.readchar()

    while ord(pressed_key)!=ord(stop_char):
        pressed_keys.append(pressed_key)
       
        pressed_key=readchar.readchar()

    pressed_numerical_keys=[x for x in pressed_keys if x.isdigit()]

    print(pressed_numerical_keys)
    pressed_numerical_keys.sort()
    print(pressed_numerical_keys)


    print("You entered " + str(len(pressed_numerical_keys)) + " numerical keys")
    print("You entered " + str(len(pressed_keys)-len(pressed_numerical_keys)) + " non-numerical keys")




#Returns True if number is prime, otherwise returns false. The calculations are improved by reducing the upper bound in testing from number/2 to the square root of number
def isPrime(number):
    print('\nChecking if '+str(number)+' is prime')

    for i in range(2, int(sqrt(number))+1):
        if number%i == 0:
            print(str(number)+' is not prime, it is divisible by ' + str(i))
            return False

    return True