import os
import cv2
import numpy as np
import glob


def denoise_video():
    video = "C:\\Users\\gbans\\Desktop\\final\\website\\website\\uploaded_image\\"
    for f in os.listdir("C:\\Users\\gbans\\Desktop\\final\\website\\website\\uploaded_image"):
        print(f)
        video = video+str(f)
    cap = cv2.VideoCapture(video)
    currentFrame = 0
# try:
# 	if not os.path.exists('data'):
# 		os.makedirs('data')
# except OSError:
# 	print('Error: Creating directory of data')
    z = 0
    currentFrame = 0
    while(z < 3):

        z = z+1
        # 	# Capture frame-by-frame
	# try:
	# 		if not os.path.exists('data'):
	# 			os.makedirs('data')
	# 	except OSError:
	# 		print('Error: Creating directory of data')

        ret, frame = cap.read()
        name = 'C:/Users/gbans/Desktop/final/website/website/yolov5/data_saved/frame' + \
            str(currentFrame) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)
        currentFrame += 1
        path = "C:/Users/gbans/Desktop/final/website/website/yolov5/data_saved/*"
        path1 = "C:/Users/gbans/Desktop/final/website/website/yolov5/images_to_be_processed/"
        path3 = "results5/"
        image_path = list(glob.glob(path))
        for i, img in enumerate(image_path):
	        image_read = cv2.imread(img)
	        c = cv2.cvtColor(image_read, cv2.COLOR_BGR2RGB)
	        median = cv2.medianBlur(c, 5)
	        bilateral = cv2.bilateralFilter(c, 21, 51, 51)
	        #cv2.imshow("Final_img",median)
	        cv2.waitKey(10)

	        cv2.imwrite(path1 + f'{str(i)}.jpg', median)
	        # cv2.imwrite(path3 + f'{str(i)}.png', bilateral)
	        # cv2.destroyAllWindows()
