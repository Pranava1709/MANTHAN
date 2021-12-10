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
from frameextraction import frameextraction
import glob


def dehaze_video():
    video = "C:\\Users\\gbans\\Desktop\\final\\website\\website\\uploaded_image\\"
    for f in os.listdir("C:\\Users\\gbans\\Desktop\\final\\website\\website\\uploaded_image"):
        print(f)
        video = video+str(f)
    z = 0
    # video = input("Upload your video: ")
    print(video)
    cap = cv2.VideoCapture(video)
    currentFrame = 0

    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')

    currentFrame = 0

    while(z < 3):
        z = z+1
        # Capture frame-by-frame
        try:
            if not os.path.exists('data'):
                os.makedirs('data')
        except OSError:
            print('Error: Creating directory of data')

        ret, frame = cap.read()

    # Saves image of the current frame in jpg file
        name = 'C:/Users/gbans/Desktop/final/website/website/yolov5/data_saved/frame' + \
            str(currentFrame) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)
        currentFrame += 1

    # To stop duplicate images

        path = "C:/Users/gbans/Desktop/final/website/website/yolov5/data_saved/*"
        path1 = "C:/Users/gbans/Desktop/final/website/website/yolov5/images_to_be_processed/"
        image_path = list(glob.glob(path))
        c = 0
        for i, img in enumerate(image_path):
            HazeImg = cv2.imread(img)

    # Resize image

            #Channels = cv2.split(HazeImg)
            #rows, cols = Channels.shape[0]
            #HazeImg = cv2.resize(HazeImg, (int(0.4 * cols), int(0.4 * rows)))

    # Estimate Airlight
            windowSze = 15
            AirlightMethod = 'fast'
            A = Airlight(HazeImg, AirlightMethod, windowSze)

    # Calculate      Boundary Constraints
            windowSze = 3
            C0 = 20         # Default value = 20 (as recommended in the paper)
            C1 = 300        # Default value = 300 (as recommended in the paper)
            # Computing the Transmission using equation (7) in the paper
            Transmission = BoundCon(HazeImg, A, C0, C1, windowSze)

    # Refine estimate of transmission
            # Default value = 1 (as recommended in the paper) --> Regularization parameter, the more this  value, the closer to the original patch wise transmission
            regularize_lambda = 1
            sigma = 0.5
            # Using contextual information
            Transmission = CalTransmission(
                HazeImg, Transmission, regularize_lambda, sigma)

    # Perform DeHazing
            HazeCorrectedImg = removeHaze(HazeImg, Transmission, A, 0.85)

            # cv2.imshow('Original', HazeImg)
            # cv2.imshow('Result', HazeCorrectedImg)
            # cv2.waitKey(10)
            cv2.imwrite(path1 + f'{str(i)}.jpg', HazeCorrectedImg)

            # k = cv2.waitKey(1000)
            # if k == 27:
            #     # cv2.destroyAllWindows()
            #     print(
            #         "Break--------------------------------------------------------------------------------->")
            #     break

            # cv2.imwrite(path1 + f'{str(i)}.jpg', HazeCorrectedImg)

        # cv2.destroyAllWindows()
