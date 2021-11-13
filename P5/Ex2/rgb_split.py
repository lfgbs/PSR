#!/usr/bin/python3
import cv2
import argparse

parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
parser.add_argument('--image', type=str, required=True, help='Full path to the image')
args = parser.parse_args()

def main():

    image = cv2.imread(args.image, cv2.IMREAD_COLOR) # Load an image 

    b,g,r=cv2.split(image)

    _, b_processed = cv2.threshold(b, 50, 255, cv2.THRESH_BINARY)
    _, g_processed = cv2.threshold(g, 100, 255, cv2.THRESH_BINARY)
    _, r_processed = cv2.threshold(r, 150, 255, cv2.THRESH_BINARY)

    new_image_rgb = cv2.merge((b_processed, g_processed, r_processed))

    cv2.imshow('original', image)  # Display the image
    cv2.imshow('blue', b_processed)  # Display the image
    cv2.imshow('green', g_processed)  # Display the image
    cv2.imshow('red', r_processed)  # Display the image
    cv2.imshow('new_image_rgb' , new_image_rgb)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

if __name__ == '__main__':
    main()