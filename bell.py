import RPi.GPIO as GPIO
import time
import os
import glob
import smtplib
from picamera import PiCamera
#GPIO SETUP
GPIO.setmode(GPIO.BCM)
Button = 21
n = 1
GPIO.setup(Button,GPIO.IN)


#loop
print("Program Berjalan")
while 1 == 1:#looping sampai menekan (ctr + C) keyboard 
  if GPIO.input(Button) == False:#Ketika tombol ditekan
    print("Bell ditekan")
    
    #    ------|    photo & Bell    |------ #
    #mengambil nama file
    date_str = time.strftime("Tanggal %d-%m-%y_Jam %H:%M.jpg")

    print("Bel Berbunyi..")
    os.system('mpg123 -q DBSE.mp3 &')
   
    command = 'python camera.py'      
    #run command
    os.system(command)
    
    
    print("Foto berhasil diambil")
    print("Nama File :", date_str)
  
  
    # ----| Email     |---- #
    print("Mengirim Gmail")#email
    emailcommand = 'python sendgmail.py' 
    os.system(emailcommand)

    
    # -- Akhir program
    print("Proses Selesai")
    # -- Program berjalan kembali dari awal
    print("")
    print("")
    print("Program Berjalan Kembali")

