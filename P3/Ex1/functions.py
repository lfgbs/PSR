import time
from math import sqrt

def timeElapsed50MillionSquareRootCalc():
    start_time=time.time()

    for i in range(1, 50000000):
        square_root=sqrt(i)
    end_time=time.time()

    print("The elapsed time was ", end_time-start_time, "seconds")