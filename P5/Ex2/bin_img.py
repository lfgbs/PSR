#!/usr/bin/python3
import cv2
import argparse

parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
parser.add_argument('--image', type=str, required=True, help='Full path to the image')
args = parser.parse_args()

def main():

    image = cv2.imread(args.image, cv2.IMREAD_COLOR) # Load an image 
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert to gray

    retval, grayimage_thresholded = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
    retval, image_thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)


    cv2.imshow('binary', grayimage_thresholded)  # Display the image
    cv2.imshow('gray', image_gray)  # Display the image
    cv2.imshow('original', image)  # Display the image
    cv2.imshow('estourada', image_thresholded)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

if __name__ == '__main__':
    main()