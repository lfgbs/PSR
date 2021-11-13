#!/usr/bin/python3
from colorama import Fore, Back, Style
from functions import *

maximum_number=10000

#calls isPrime()
def main():
    print('Checking numbers 2 through ' + str(maximum_number))

    for i in range(2, maximum_number+1):
        if isPrime(i):
             print(Fore.RED + Back.YELLOW + Style.BRIGHT+str(i)+' is prime!'+ Style.RESET_ALL)

if __name__ == "__main__":
    main()
