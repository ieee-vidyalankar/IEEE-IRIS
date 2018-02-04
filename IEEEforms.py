#NishantJadhav
#IEEE-VIT Web-TechTeam
#CMPN-A  #####UPDATED FILE BUGS FIXED###

import csv
from PIL import Image,ImageDraw,ImageFont
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
import shutil

with open('IEEE-form.csv','r') as file:
    x = csv.DictReader(file)
    for row in x:
        
        logo = Image.open('iris.jpg')
        logo1 =logo.resize((500,500))
        image = Image.open('image.jpg')
        large_font = ImageFont.truetype('arial.ttf',125)
        small_font = ImageFont.truetype('arial.ttf',60)
        big_font = ImageFont.truetype('arial.ttf',90)
        

        draw = ImageDraw.Draw(image)
        draw.text(xy=(250,600),text=row['Full Name'],fill=(0,0,0),font = small_font)
        draw.text(xy=(250,750),text=row['Email ID '], fill=(0,0,0),font = small_font)
        draw.text(xy=(2000,1250),text=row['Serial no.'],fill=(0,0,0),font = big_font)
        draw.text(xy=(500,250),text="Welcome to IRIS!!",fill=(0,0,0),font=large_font)

        image.paste (logo1,(2000,150))
        #image.show()
        image.save('passes.jpg')
        shutil.copy('passes.jpg','{}.jpg'.format(row['Full Name']))

        #Text ATTACHTMENT
        email_sender='email@gmail.com'
        email_receiver=row['Email ID ']
        subject='IEEE- IRIS PASS'

        msg=MIMEMultipart()
        msg['From']= email_sender
        msg['to']= email_receiver
        msg['subject']= subject

        body="Here is your  IRIS Pass"
        msg.attach(MIMEText(body,'plain'))
        #Image ATTACHMENT
        filename ='{}.jpg'.format(row['Full Name'])
        attachment = open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)       
        part.add_header('Content-Disposition',"attachment; filename ="+filename)  

        msg.attach(part)
        text = msg.as_string()

        #EMAIL ONLY
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.ehlo()
        server.login(email_sender,'*****') #PASSWORD

        server.sendmail(email_sender,email_receiver,text)
        server.close()




















