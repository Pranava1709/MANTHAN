import os 
import cv2
import numpy as np
import glob

if __name__ == '__main__':
    video = input("Upload your video: ")
   
    cap = cv2.VideoCapture(video)
    currentFrame = 0

    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print ('Error: Creating directory of data')

    currentFrame = 0

    while(True):

    # Capture frame-by-frame
        try:
            if not os.path.exists('data'):
                os.makedirs('data')
        except OSError:
            print ('Error: Creating directory of data')

    
        ret, frame = cap.read()

    # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        currentFrame += 1

    # To stop duplicate images
            
        path = "data/*"
        path1 = "results/"
        image_path = list(glob.glob(path)) 	
        c= 0 
        for i, img in enumerate(image_path):
        	image_read = cv2.imread(img)
			c = cv2.cvtColor(image_read ,cv2.COLOR_BGR2RGB)
			median = cv2.medianBlur(c,5)
			bilateral = cv2.bilateralFilter(c, 21,51,51)
			#cv2.imshow("Final_img",median)
			cv2.waitKey(1000)
	
			cv2.imwrite(path1 + f'{str(i)}.png',median)
			cv2.imwrite(path3 + f'{str(i)}.png',bilateral)
			cv2.destroyAllWindows()