from colorama import Fore, Back, Style
import readchar
import time
import random
from collections import namedtuple

#Stores information for key requested, key received, duration of attempt and if it was correct(this one is just for ease of use)
class Input:
    def __init__(self, requested, received, duration, correct):
        self.requested=requested
        self.received=received
        self.duration=duration
        self.correct=correct

    def __repr__(self):
        if self.correct:
            return "Input(requested='"+str(self.requested)+"', received='"+str(self.received)+"' duration="+str(self.duration)+")"
        return Fore.RED + Back.YELLOW + Style.BRIGHT+"Input(requested='"+str(self.requested)+"', received='"+str(self.received)+"' duration="+str(self.duration)+")" + Style.RESET_ALL

    def __str__(self):
        return "Input(requested='"+str(self.requested)+"', received='"+str(self.received)+"' duration="+str(self.duration)+")"

#receives the signal that the test should start, returns test start time
def waitForTestStart():
    print("Press any key to start the test")
    readchar.readchar()
    return time.time()

#generates and presents the key to the User between the values of 97(a) and 122(z)
def generateKey():
    return waitForKeyPress(random.randrange(97, 122))

#Waits for the users key press and creates an Input object
def waitForKeyPress(key_code):
    requested = chr(key_code)
    print("Type the letter " + Fore.BLUE + requested + Style.RESET_ALL)
    attempt_start_time=time.time()
    received=readchar.readchar()
    attempt_finish_time=time.time()
    correct = True if requested==received else False
    if correct:
        print("You typed the letter "+ Fore.GREEN + received + Style.RESET_ALL)
    else:
        print("You typed the letter "+ Fore.RED + received + Style.RESET_ALL)
    return Input(requested, received, attempt_finish_time-attempt_start_time, correct)

def calcStats(test_start_time, test_end_time, input_list):

    total_hit_time=0
    total_miss_time=0

    correct_list=[input for input in input_list if input.correct==True]
    incorrect_list=[input for input in input_list if input.correct==False]

    for input in correct_list:
        total_hit_time+=input.duration

    for input in incorrect_list:
        total_miss_time+=input.duration    

    stats_dict={
        'accuracy':len(correct_list)*100/len(input_list),
        'inputs':input_list,
        'number_of_hits':len(correct_list),
        'number_of_types':len(input_list),
        'test_duration': test_end_time-test_start_time,
        'test_start_time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(test_start_time)),
        'test_end_time':time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(test_end_time)),
        'type_avg_duration':(total_hit_time+total_miss_time)/len(input_list),
        'type_hit_avg_duration':total_hit_time/len(input_list),
        'type_miss_avg_duration':total_miss_time/len(input_list)
    }

    return stats_dict