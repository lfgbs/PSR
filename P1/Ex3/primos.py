#!/usr/bin/python3
from colorama import Fore, Back, Style

maximum_number=100

def is_Prime(number):
    print('\nChecking if '+str(number)+' is prime...')

    count=0

    #the following line needs the upper bound to be round(number/2)+1 only for the case when we are checking the number 4 
    for i in range(2, round(number/2)+1):
        if number%i == 0:
            count+=1
            print(str(number)+' is not prime, it is divisible by ' + str(i))
            
    if count == 0:
        return True
    else:
        return False

def main():
    print('Checking numbers 2 through ' + str(maximum_number))

    count=0 

    for i in range(2, maximum_number+1):
        if is_Prime(i):
            count+=1
            print(Fore.RED + Back.YELLOW + Style.BRIGHT +  'Number ' + Fore.LIGHTYELLOW_EX + Back.GREEN + Style.BRIGHT
               + str(i) + Fore.RED + Back.YELLOW + Style.BRIGHT + ' is prime.' + Style.RESET_ALL )

    print(Fore.BLUE + Back.WHITE + '\nBetween 1 and ' + str(maximum_number) + ' there are ' + Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT + str(count) +
         Fore.BLUE + Back.WHITE + ' prime numbers' + Style.RESET_ALL)
if __name__ == "__main__":
    main()
