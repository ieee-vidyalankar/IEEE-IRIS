# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:01:40 2018

@author: Saurabh
"""
import os
from os import listdir
import csv
from PIL import Image,ImageDraw,ImageFont
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sending_email(from_address, to_address, names, password):
        msg = MIMEMultipart() 
        msg['From'] = from_address 
        msg['To'] = to_address 
        msg['Subject'] = "IEEE PRE-IRIS 2018 PASS"
        body = """Greetings %s!
Kindly find your E-Certificate for the same, attached along with this mail.""" %names
        msg.attach(MIMEText(body, 'plain')) # attaching the body with the msg instance
          
        filename = "%s.jpg" %names # opening the file to be sent
        attachment = open(r"C:\Users\Saurabh\Desktop\Misc\IEEE-VIT\Certificate Automation\certificates\%s.jpg" %names, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())

        encoders.encode_base64(p)
          
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                 
        msg.attach(p) # attach the instance 'p' to instance 'msg'        

        session = smtplib.SMTP('smtp.office365.com', 587) # creates SMTP session         
        session.starttls()         
        session.login(from_address, password)# Authentication         
        text = msg.as_string()# Converts the Multipart msg into a string        
        session.sendmail(from_address, to_address, text)         
        session.quit()

def generating_certificate(filename, certificate, textfont):
    with open(filename, newline='') as csvfile:
        read = csv.reader(csvfile,delimiter='`', quotechar='|')
        read = csv.DictReader(csvfile)
        for row in read:
            names = row['FULL NAME']
            print(names)
            image = Image.open(certificate)
            x,y = image.size
            font_type = ImageFont.truetype(textfont,40)
            font_type1 = ImageFont.truetype("arial.ttf",35)
            draw = ImageDraw.Draw(image)
            a,b = font_type.getsize(names)
            draw.text(xy = (230,360),text = names, fill=(255,0,0),font = font_type)
            draw.text(xy = (230,410),text = "IRIS-00"+row['SERIAL'], fill=(0,0,0,255), font = font_type1)
            image.save(os.path.join('certificates' , names +'.jpg'))
            to_address = row['EMAIL ID']
            print(to_address)
            sending_email('ieee@vit.edu.in', to_address, names, 'password')

os.makedirs('certificates',exist_ok=True)
generating_certificate('responses1.csv', 'TICKET.jpg', 'DobkinScript.ttf')




    
        


