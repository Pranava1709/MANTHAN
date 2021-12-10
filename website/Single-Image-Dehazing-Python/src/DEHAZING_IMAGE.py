
import cv2
import numpy as np

from Airlight import Airlight
from BoundCon import BoundCon
from CalTransmission import CalTransmission
from removeHaze import removeHaze
import glob


def dehazing():
    #images = input("Upload your images or images folder path: ")
    #images = ""
    # print(images)
    img = "C:\\Users\\gbans\\Desktop\\final\\website\\website\\uploaded_image"
    path1 = "C:\\Users\\gbans\\Desktop\\final\\website\\website\\yolov5\\images_to_be_processed\\"
    image_paths = list(glob.glob(img))
    print(image_paths)
    # enumerate(image_paths)
    c = 0
    i = 0
    for path in glob.glob("C:\\Users\\gbans\\Desktop\\final\\website\\website\\uploaded_image\\*.jpg"):
        print("In the loop")
        HazeImg = cv2.imread(path)
        # cv2.imshow("as0", HazeImg)
        # cv2.waitKey(0)
        HazeImg = np.array(HazeImg)
        windowSze = 15
        AirlightMethod = 'fast'
        A = Airlight(HazeImg, AirlightMethod, windowSze)

    # Calculate Boundary Constraints
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
        # cv2.waitKey(0)

        cv2.imwrite(path1 + f'{str(i)}.png', HazeCorrectedImg)
        i = i+1
