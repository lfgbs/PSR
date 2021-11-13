#!/usr/bin/python3
#os prints estão comentados apenas para não interferirem no wc pruposto no final do exercício 2
maximum_number=10000

def is_Prime(number):
    #print('\nChecking if '+str(number)+' is prime')

    #the following line needs the upper bound to be round(number/2)+1 only for the case when we are checking the number 4 
    for i in range(2, round(number/2)+1):
        if number%i == 0:
            #print(str(number)+' is not prime, it is divisible by ' + str(i))
            return False

    #print(str(number)+' is prime!')
    return True

def main():
    print('Checking numbers 2 through ' + str(maximum_number))

    for i in range(2, maximum_number+1):
        if is_Prime(i):
            print(str(i)+' is prime!')

if __name__ == "__main__":
    main()
