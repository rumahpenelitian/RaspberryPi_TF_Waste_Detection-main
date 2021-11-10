import os
import argparse
import cv2
import numpy as np
import sys
import importlib.util

# video = cv2.VideoCapture('test.avi')
video = cv2.VideoCapture('test.avi')

vid_name = 'output.avi'
vid = cv2.VideoWriter(vid_name, cv2.VideoWriter_fourcc(*'MJPG'), 20, (640,480))

while (video.isOpened()):
    ret, frame = video.read()
    if not ret:
      print('Reached the end of the video!')
      break

    cv2.imshow('frame', frame)
    frame = cv2.flip(frame, 0)
    vid.write(frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()