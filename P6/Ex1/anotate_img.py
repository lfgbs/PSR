#!/usr/bin/python3
import cv2
import argparse
from functools import partial
from colorama import Fore, Back, Style

parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
parser.add_argument('--image', type=str, required=True, help='Full path to the image')
args = parser.parse_args()

def onMouse(event, x, y, flags, params, w_name, img):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 10, color)
        cv2.imshow(w_name, img)

    if event==cv2.EVENT_RBUTTONDOWN:
        cv2.putText(img, "Printing!", (x,y), cv2.FONT_HERSHEY_PLAIN, 1, color)
        cv2.imshow(w_name, img)

def main():

    parser = argparse.ArgumentParser(description='Typing Test Option Parser')
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = parser.parse_args()

    window_name='Anotação'
    global color
    color=(0,0,255)
    image = cv2.imread(args.image, cv2.IMREAD_COLOR) # Load an image 

    cv2.imshow(window_name, image)

    cv2.setMouseCallback(window_name, partial(onMouse, w_name=window_name, img=image))
    
    while(True):

        key=cv2.waitKey(20)

        if key != -1:
            if key == ord('r'):
                color=(0,0,255)
                print("Circle color was changed to"+ Fore.RED + " red" + Style.RESET_ALL)
            if key == ord('g'):
                color=(0,255,0)
                print("Circle color was changed to"+ Fore.GREEN + " green" + Style.RESET_ALL)
            if key == ord('b'):
                color=(255,0,0)
                print("Circle color was changed to"+ Fore.BLUE + " blue" + Style.RESET_ALL)
            if key == ord('q'):
                break
   

if __name__ == '__main__':
    main()