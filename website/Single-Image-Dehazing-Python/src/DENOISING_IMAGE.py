import numpy as np
import cv2
import glob
import os


from matplotlib import pyplot as plt


def denoising():
	# images  = input("Upload your image or folders:")
	img = "C:\\Users\\gbans\\Desktop\\final\\website\\website\\uploaded_image"
	path1 = "C:\\Users\\gbans\\Desktop\\final\\website\\website\\yolov5\\result\\"
	#path3 = "C:\\Users\\gbans\\Desktop\\final\\website\\website\\yolov5\\result\\result2\\"
	image_paths = list(glob.glob(img))
	c = 0
	i = 0
	for path in glob.glob("C:\\Users\\gbans\\Desktop\\final\\website\\website\\uploaded_image\\*.jpg"):
		image_read = cv2.imread(path)
		c = cv2.cvtColor(image_read, cv2.COLOR_BGR2RGB)
		median = cv2.medianBlur(c, 5)
		bilateral = cv2.bilateralFilter(c, 21, 51, 51)
		#cv2.imshow("Final_img",median)
		cv2.waitKey(1000)

		cv2.imwrite(path1 + f'{str(i)}.png', median)
		#cv2.imwrite(path3 + f'{str(i)}.png', bilateral)
		i = i+1
		cv2.destroyAllWindows()
