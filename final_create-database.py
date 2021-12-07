# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera
import time
import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

frames = 20
detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
Id=raw_input("enter your id : ")
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
print 'mengambil 20x gambar'

# allow the camera to warmup
time.sleep(1.25)
start = time.time()
camera.capture_sequence([
        "dataset/User." + Id + ".%d.jpg" % i
        for i in range(frames)
        ], use_video_port=True)
finish = time.time()

Num = 0
for Num in range(20):
        Num = str(Num)
        img = cv2.imread("dataset/User." + Id + "." + Num + ".jpg")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.2, 5)
        if(len(faces)!=0):
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.imwrite("dataset/User." + Id + "." + Num + ".jpg", gray[y:y+h,x:x+w])
                Num = int(Num)
                Num=Num+1
            
print('Captured %d frames at %.2ffps' % (
    frames,
    frames / (finish - start)))
