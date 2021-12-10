import cv2
import sys
import os
import numpy as np
from numpy import savetxt
import pandas as pd

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

if __name__ == '__main__':

    # Set up tracker.
    # Instead of MIL, you can also use
    column_name = ['filename', 'width', 'height',
                   'class', 'xmin', 'ymin', 'xmax', 'ymax']
    column_name1 = ['class', 'x_center', 'y_center', 'width', 'height']
    tracker_types = ['BOOSTING', 'MIL', 'KCF',
                     'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']
    tracker_type = tracker_types[5]

    if int(minor_ver) < 3:
        tracker = cv2.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == 'CSRT':
            tracker = cv2.TrackerCSRT_create()
        if tracker_type == 'MOSSE':
            tracker = cv2.TrackerMOSSE_create()

    # Read video
    cap = cv2.VideoCapture("./video/video8.mov")
    #cap = cv2.VideoCapture(0)
    # Exit if video not opened.
    #if not video.isOpened():
    #    print("Could not open video")
    #    sys.exit()

    # Read first frame.
    # for z in range(100):
    ok, frame = cap.read()
    frame = cv2.resize(frame, (320, 640))

    if not ok:
        print('Cannot read video file')
        sys.exit()

    # Define an initial bounding box
    bbox = (0, 0, 0, 0)

    # Uncomment the line below to select a different bounding box
    bbox = cv2.selectROI(frame, False)

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)

    #file2write=open("D:\\flynovate\\SolarPanelSoilingImageDataset\\bottle\\target.txt",'a')
    i = 0
    q = 0
    data = []
    data1 = []
    while True:
        if i == 200:
            break
        # Read a new frame
        ok, frame = cap.read()
        if not ok:
            break

        # Start timer
        frame = cv2.resize(frame, (320, 640))
        cv2.imwrite(os.path.join(
            'D:\\yolov5\\yolov5\\dataset\\images\\val\\', "img"+str(i+q)+".jpg"), frame)
        #cv2.imwrite(os.path.join('D:\\yolov5\\yolov5\\dataset\\images\\val\\' , "img"+str(i)+".jpg"), frame)

        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(frame)

        #file2write.write(''.join(str(bbox)))
        #file2write.write("\n")
        values = ('img'+str(i+q)+'.jpg', int(bbox[2]), int(bbox[3]), 'face', int(
            bbox[0]), int(bbox[1]), int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        data.append(values)
        print(((float(bbox[2])/2+float(bbox[0])))/320.0)
        values1 = (0, (float(bbox[2])/2+float(bbox[0]))/320.0, (float(bbox[3])/2+float(
            bbox[1]))/640.0, (float(bbox[2]))/320.0, (float(bbox[3]))/640.0)
        #data1.append(values1)

        xml_df = pd.DataFrame([values1], columns=column_name1)
        np.savetxt(r'D:\yolov5\yolov5\dataset\labels\val\img'
                   + str(i+q)+'.txt', xml_df.values, fmt='%f')
        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        # Display result
        cv2.imshow("Tracking", frame)
        i = i+1
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break

    #
    # xml_df = pd.DataFrame(data, columns=column_name)
    # xml_df.to_csv(('train_labels.csv'), index=None)
    # xml_df = pd.DataFrame(data1, columns=column_name1)
    # np.savetxt(r'train.txt', xml_df.values, fmt='%f')
