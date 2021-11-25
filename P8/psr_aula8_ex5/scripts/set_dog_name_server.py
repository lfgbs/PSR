#!/usr/bin/env python3

from __future__ import print_function
import re
import rospy
from psr_aula8_ex5.msg import Dog
from psr_aula8_ex5.srv import SetDogName, SetDogNameResponse


def handle_set_dog_name(req):
    try:
        print("Changing %s's name to %s"%(req.dog, req.new_name))
        req.dog.name=req.name
        return SetDogNameResponse(True)
    except:
        return SetDogNameResponse(False)

def set_dog_name():
    rospy.init_node('set_dog_name_server')
    s = rospy.Service('set_dog_name', SetDogName, handle_set_dog_name)
    print("Ready to set dog's name")
    rospy.spin()

if __name__ == "__main__":
    set_dog_name()