#!/usr/bin/python3

#-------------------------------------------
#A program to calculate up to a given number
#Luís Silva, nmec 88888 
#PSR 2021/2022- UA
#------------------------------------------

from colorama import Fore, Back, Style

#As of right now, the number is hard coded and not taken in as a parameter
maximum_number = 500

#This function returns True if the parameter received is a perfect number and False if it is not 
def isPerfect(number):
    print('\nChecking if '+str(number)+' is perfect..')

    #divisor_sum is used to add up a numbers divisors as we come across them
    divisor_sum=0

    #The maximum divisor a number can have is number/2 and so thats where we stop our testing
    #the following line needs the upper bound to be round(number/2)+1 only for the case when we are checking the number 4 
    for i in range(1, round(number/2)+1):
        #if the number is divisible by i, then thee value i is added to divisor_sum 
        if number%i == 0:
            divisor_sum+=i
            #if at any point divisor_sum is greater than number, then we know that number is not a perfect number and we can return False
            if divisor_sum > number:
                return False
            
    #If after all the values of i have been tested divisor_sum is equal to number, then number is a perfect number. Otherwise it is not
    if divisor_sum==number:
        return True
    else:
        return False
   
#calls isPerfect()
def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print(Fore.RED + Back.YELLOW + Style.BRIGHT+'Number ' + Fore.LIGHTYELLOW_EX + Back.GREEN + Style.BRIGHT + str(i) + Fore.RED + Back.YELLOW + Style.BRIGHT + ' is perfect.' + Style.RESET_ALL)


if __name__ == "__main__":
    main()