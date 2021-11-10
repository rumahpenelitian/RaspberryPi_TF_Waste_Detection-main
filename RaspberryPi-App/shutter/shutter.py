import time
import cv2
import datetime
from gpiozero import Button
from time import sleep

buttonPhoto = Button(15)
buttonVideo = Button(23)

cap = cv2.VideoCapture(0)
vid = 0

rec = False

while (True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        print('ESC...')
        break

    if buttonPhoto.is_pressed: 
        format = datetime.datetime.now()
        img_name = format.strftime('%d%m%y-%H%M%S.jpg')
        cv2.imwrite(img_name, frame)
        print('Photo Captured as '+ img_name)

    if buttonVideo.is_pressed:
        start = time.time()
        while time.time() - start < 1:
            pass

        format = datetime.datetime.now()
        vid_name = format.strftime('%d%m%y-%H%M%S.avi')
        # cv2.imwrite(img_name, frame)
        if rec == False:
            vid = cv2.VideoWriter(vid_name, cv2.VideoWriter_fourcc(*'MJPG'), 20, (640,480))
            rec = True
            print('recording..')
        else :
            rec = False
            vid.release()
            print('stop recording..')
    
    if rec == True :
        # frame = cv2.flip(frame, 0)
        vid.write(frame)

cap.release()
vid.release()
cv2.destroyAllWindows()
