import picamera
import time
import cv2
import numpy
import matplotlib
from subprocess import call
from datetime import datetime
from time import sleep

deteksi = cv2.CascadeClassifier("/home/pi/FaceRecog_dbell/haarcascade_frontalface_default.xml")

filePath = "/home/pi/FaceRecog_dbell/photos/"

currentTime = datetime.now()
picTime = currentTime.strftime("Tanggal %d-%m-%y_Jam %H:%M")
picName = picTime + '.jpg'
completeFilePath = filePath + picName

print("Mengambil Foto..")

with picamera.PiCamera() as camera:
    camera.resolution = (960, 720)
    camera.brightness = 55
    sleep(1)
    camera.capture(completeFilePath)

image = cv2.imread(completeFilePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayscaleFileCrop = 'Grayscale_Crop - ' + picName
grayscaleFilePathCrop = filePath + grayscaleFileCrop

faces = deteksi.detectMultiScale(gray, 1.1, 5)
try:
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)    
    cv2.imwrite(grayscaleFilePathCrop, gray[y:y+h,x:x+w])
except Exception:
    print ('Wajah tidak terdeteksi')

image1 = cv2.imread(completeFilePath)
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
grayscaleFile = 'Grayscale - ' + picName
grayscaleFilePath = filePath + grayscaleFile
cv2.imwrite(grayscaleFilePath, gray1)
