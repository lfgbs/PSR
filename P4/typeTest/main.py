#!/usr/bin/python3
from functions import *
from pprint import pprint
import argparse

parser = argparse.ArgumentParser(description='Typing Test Option Parser')
parser.add_argument('--maximum_number', type=int, help='sets the maximum number of letters asked ')
parser.add_argument('--utm', type=int, help='sets maximum test duration (in seconds)if not specified this value will be 20')
args = parser.parse_args()

def main():

    #this value will be used if no limit is set by the user
    maximum_attempts=1000000000000000
    #this value will be used if no timeframe is provided by the user
    maximum_time=20

    if args.maximum_number!=None:
        maximum_attempts=args.maximum_number
    if args.utm!=None:
        maximum_time=args.utm

    elapsed_time=0
    attempts=0

    inputs=[]

    print("This test will have a duration of", maximum_time ," seconds and a maximum number of attempts of", maximum_attempts)

    test_start_time=waitForTestStart()

    while attempts<maximum_attempts and elapsed_time<maximum_time:
        inputs.append(generateKey())
        attempts+=1
        elapsed_time=time.time()-test_start_time

    test_end_time=time.time()
    
    pprint(calcStats(test_start_time, test_end_time, inputs))
    

if __name__ == "__main__":
    main()
