from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from smtplib import SMTP
import smtplib
import sys
import time


dari = "" #Email dari siapa
kepada = "" #Email untuk siapa

msg = MIMEMultipart()

msg['From'] = dari
msg['To'] = kepada
msg['Subject'] = "Anda kedatangan tamu di depan rumah.."

body = "Berikut ini adalah lampiran dari foto tamu"

msg.attach(MIMEText(body, 'plain'))

date_str = time.strftime("Grayscale - Tanggal %d-%m-%y_Jam %H:%M.jpg")
filename = date_str
attachment = open("/home/pi/FaceRecog_dbell/photos/" + date_str, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(dari, "") #isi password dari email From
text = msg.as_string()
server.sendmail(dari, kepada, text)
server.quit()
