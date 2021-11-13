import argparse
from functools import partial
import numpy as np
import json
import cv2

def onTrackBar(value, channel, min_max, w_name, img, ranges):
    ranges[channel][min_max]=value

     # Processing
    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    mask = cv2.inRange(img, mins, maxs)

    image_processed=img.copy()
    image_processed[mask == 0] = (0, 0, 0)

    cv2.imshow(w_name, image_processed)

def onMouse(event, x, y, flags, params):
   if event == cv2.EVENT_LBUTTONDOWN:
       print('x = %d, y = %d'%(x, y))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = parser.parse_args()

    window_name = 'window - Ex3a'

    ranges={'b':{'min':0, 'max':255},
            'g':{'min':0, 'max':255},
            'r':{'min':0, 'max':255}
    }

    image = cv2.imread(args.image, cv2.IMREAD_COLOR)  # Load an image
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)

    # add code to create the trackbar ...
    cv2.createTrackbar('MinB', window_name , 0, 255, partial(onTrackBar, channel='b', min_max='min', w_name=window_name, img=image, ranges=ranges))
    cv2.createTrackbar('MinG', window_name , 0, 255, partial(onTrackBar, channel='g', min_max='min', w_name=window_name, img=image, ranges=ranges))
    cv2.createTrackbar('MinR', window_name , 0, 255, partial(onTrackBar, channel='r', min_max='min', w_name=window_name, img=image, ranges=ranges))
    cv2.createTrackbar('MaxB', window_name , 0, 255, partial(onTrackBar, channel='b', min_max='max', w_name=window_name, img=image, ranges=ranges))
    cv2.createTrackbar('MaxG', window_name , 0, 255, partial(onTrackBar, channel='g', min_max='max', w_name=window_name, img=image, ranges=ranges))
    cv2.createTrackbar('MaxR', window_name , 0, 255, partial(onTrackBar, channel='r', min_max='max', w_name=window_name, img=image, ranges=ranges))

    cv2.setTrackbarPos('MaxB', window_name, 255)
    cv2.setTrackbarPos('MaxG', window_name, 255)
    cv2.setTrackbarPos('MaxR', window_name, 255)

    cv2.setMouseCallback(window_name, onMouse)

    cv2.waitKey(0)

    file_name = 'ranges.json'
    with open(file_name, 'w') as file_handle:
        print('writing ranges to file ' + file_name)
        json.dump(ranges, file_handle)

if __name__ == '__main__':
    main()
