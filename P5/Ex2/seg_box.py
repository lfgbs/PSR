#!/usr/bin/python3
import cv2
import argparse

parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
parser.add_argument('--image', type=str, required=True, help='Full path to the image')
args = parser.parse_args()

def main():

    image = cv2.imread(args.image, cv2.IMREAD_COLOR) # Load an image 
    hsv= cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # Convert to Hsv

    #fica a branco o que pertence ao range e a preto o que não pertence
    mask_green = cv2.inRange(hsv, (40, 100, 20), (75, 255,255))
    
    #este bitwise_and entre a imagem e a máscara faz com que o que estiver no range fique com a cor da imagem em vez de ficar a preto e branco
    target = cv2.bitwise_and(hsv,hsv, mask=mask_green)

    cv2.imshow('original', image)  # Display the image
    cv2.imshow('filtro verde', mask_green)  # Display the image
    cv2.imshow('filtro verde bitwise_and', target)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

if __name__ == '__main__':
    main()