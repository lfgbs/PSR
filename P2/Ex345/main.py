#!/usr/bin/python3
from colorama import Fore, Back, Style
from functions import *
import argparse
import readchar

parser = argparse.ArgumentParser(description='PSR argparse example.')
parser.add_argument('--maximum_number', type=int, help='The Script will search for primes up to this number(included)')
args = parser.parse_args()


#calls isPrime() and now receives an argument representing the maximum_number, calls printAllPreviousChars, printAllCharsUpTo and countNumbersUpTo()
def main():
    #Ex3
    """
    print('Checking numbers 2 through ' + str(args.maximum_number))

    for i in range(2, args.maximum_number+1):
        if isPrime(i):
             print(Fore.RED + Back.YELLOW + Style.BRIGHT+str(i)+' is prime!'+ Style.RESET_ALL)
    

    #Ex4a
    print(Fore.RED + Back.YELLOW + Style.BRIGHT+'Ex4a'+ Style.RESET_ALL)
    printAllPreviousChars()

    #Ex4b
    print(Fore.RED + Back.YELLOW + Style.BRIGHT+'\nEx4b'+ Style.RESET_ALL)
    print("Press the desired stop_char")
    stop_char = readchar.readchar()
    printAllCharsUpTo(stop_char)
    """

    #Ex4cAnd5e
    print(Fore.RED + Back.YELLOW + Style.BRIGHT+'\nEx4c'+ Style.RESET_ALL)
    print("Press the desired stop_char")
    stop_char = readchar.readchar()
    countAllNumbersUpTo(stop_char)

    

if __name__ == "__main__":
    main()
