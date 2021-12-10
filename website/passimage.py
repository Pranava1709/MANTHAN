import os

import sys


def detect():
    os.system(
        "python website\\yolov5\\detect.py --source website\\yolov5\\images_to_be_processed\\ --weight yolov5s.pt")


def detectdenoise():
    os.system(
        "python website\\yolov5\\detect.py --source website\\yolov5\\result\\ --weight yolov5s.pt")


# def generate_frame():
#     os.system(
#         "python website\\yolov5\\detect.py --source website\\yolov5\\result\\ --weight yolov5s.pt")
