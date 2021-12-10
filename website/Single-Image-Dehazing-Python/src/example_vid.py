"""
Created on Thursday June 11 16:38:42 2020
@author: Utkarsh Deshmukh
"""
import cv2
import numpy as np
import os

from Airlight import Airlight
from BoundCon import BoundCon
from CalTransmission import CalTransmission
from removeHaze import removeHaze
cap = cv2.VideoCapture('video.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1


if __name__ == '__main__':
    path = "data/"
    path1 = "results/"
    image_path = list(glob.glob(path)) 	
    c= 0 
    for i, img in enumerate(image_path):
        HazeImg = cv2.imread(img)


    # Resize image
    
        Channels = cv2.split(HazeImg)
        rows, cols = Channels[0].shape
        HazeImg = cv2.resize(HazeImg, (int(0.4 * cols), int(0.4 * rows)))
    

    # Estimate Airlight
        windowSze = 15
        AirlightMethod = 'fast'
        A = Airlight(HazeImg, AirlightMethod, windowSze)

    # Calculate Boundary Constraints
        windowSze = 3
        C0 = 20         # Default value = 20 (as recommended in the paper)
        C1 = 300        # Default value = 300 (as recommended in the paper)
        Transmission = BoundCon(HazeImg, A, C0, C1, windowSze)                  #   Computing the Transmission using equation (7) in the paper

    # Refine estimate of transmission
        regularize_lambda = 1       # Default value = 1 (as recommended in the paper) --> Regularization parameter, the more this  value, the closer to the original patch wise transmission
        sigma = 0.5
        Transmission = CalTransmission(HazeImg, Transmission, regularize_lambda, sigma)     # Using contextual information

    # Perform DeHazing
        HazeCorrectedImg = removeHaze(HazeImg, Transmission, A, 0.85)

        cv2.imshow('Original', HazeImg)
        cv2.imshow('Result', HazeCorrectedImg)
        cv2.waitKey(0)

        cv2.imwrite(path1 + f'{str(i)}.png', HazeCorrectedImg)
        cv.destroyAllWindows()
