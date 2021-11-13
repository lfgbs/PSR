#!/usr/bin/python3
from colorama import Fore, Back, Style
maximum_number = 500

def isPerfect(number):
    print('\nChecking if '+str(number)+' is perfect..')

    divisor_sum=0

    #the following line needs the upper bound to be round(number/2)+1 only for the case when we are checking the number 4 
    for i in range(1, round(number/2)+1):
        if number%i == 0:
            divisor_sum+=i
            if divisor_sum > number:
                return False
            
    if divisor_sum==number:
        return True
    else:
        return False
   
def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print(Fore.RED + Back.YELLOW + Style.BRIGHT+'Number ' + Fore.LIGHTYELLOW_EX + Back.GREEN + Style.BRIGHT + str(i) + Fore.RED + Back.YELLOW + Style.BRIGHT + ' is perfect.' + Style.RESET_ALL)


if __name__ == "__main__":
    main()