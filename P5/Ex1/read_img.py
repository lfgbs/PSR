#!/usr/bin/python3
import cv2
import argparse

parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
parser.add_argument('--image', nargs='+', required=True, help='Full path to the image. If more than one path is specified than the images will be displayed in a carrousel fashion')
args = parser.parse_args()

def main():

    index=0

    #There is a stable version/example of loading a single image in Ex2 
    #Trouble with closing the window, right now requires keyboard interruption
    while True:

        image = cv2.imread(args.image[index], cv2.IMREAD_COLOR) # Load an image

        cv2.imshow('window', image)  # Display the image
        cv2.waitKey(3000) # wait for a key press before proceeding

        index=(index+1)%len(args.image)


if __name__ == '__main__':
    main()