import numpy as np
import pandas as pd
import glob
import cv2

for i in glob.glob("D:\\yolov5\\yolov5\\thermal_dataset\\labels\\val\\*txt"):
    z = pd.read_csv(i, delimiter=" ", header=None)
    z.iloc[:, 0] = 0
    np.savetxt(i, z)
    print(z.iloc[:, 0])

# z = pd.read_csv(
#     "D:\\yolov5\\yolov5\\thermal_dataset\\labels\\train\\image_0_37.txt", delimiter=" ", header=None)
# print(z.iloc[:, 0])
