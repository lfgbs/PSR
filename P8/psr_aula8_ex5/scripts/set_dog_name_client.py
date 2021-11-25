#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from psr_aula8_ex5.msg import Dog
from psr_aula8_ex5.srv import SetDogName

def set_dog_name_client(dog, name):
    rospy.wait_for_service('set_dog_name')
    try:
        set_dog_name = rospy.ServiceProxy('set_dog_name', SetDogName)
        resp1 = set_dog_name(dog, name)
        return resp1.result
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s <dog name>"%sys.argv[0]

if __name__ == "__main__":

    dog1=Dog("bobby", "golden", 3)

    print(dog1)

    if len(sys.argv) == 2:
        new_name = sys.argv[1]
    else:
        print(usage())
        sys.exit(1)
    print("Changing %s's name to %s"%(dog1,new_name))
    print(set_dog_name_client(dog1, new_name))