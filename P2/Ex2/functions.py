#Returns True if number is prime, otherwise returns false
def isPrime(number):
    print('\nChecking if '+str(number)+' is prime')

    #the following line needs the upper bound to be round(number/2)+1 only for the case when we are checking the number 4 
    for i in range(2, round(number/2)+1):
        if number%i == 0:
            print(str(number)+' is not prime, it is divisible by ' + str(i))
            return False

    return True