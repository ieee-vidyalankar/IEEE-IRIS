#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:41:42 2018

__author__ = "PREETAM RANE"
__copyright__ = "Copyright 2007, IEEE-VIT STUDENT BRANCH"
__credits__ = ["PRATIK BHURAN", "NISHANT JADHAV", "HEMANT SIRSAT"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "IEEE-VIT TECH-WEB TEAM"
__email__ = "ieee@vit.edu.in"
__status__ = "Production"
"""
#import os
#from os import listdir
import csv
from PIL import Image,ImageDraw,ImageFont
import smtplib
import qrcode
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from email.mime.base import MIMEBase
#from email import encoders
from email.mime.image import MIMEImage
import shutil


def sending_mail(email_sender, email_receiver, names, password):
    subject='certificate'
    msg=MIMEMultipart()
    msg['From']= email_sender
    msg['to']= email_receiver
    msg['subject']= subject
    body = """body captions and descriptions type here %s"""%names #add name of person for greetings
    msg.attach(MIMEText(body,'plain'))
    img_data = open('{}.jpg'.format(names), 'rb').read()
    html_part = MIMEMultipart(_subtype='related')
    body = MIMEText('<img src="cid:myimage" />', _subtype='html')#embed image
    html_part.attach(body)
    img = MIMEImage(img_data, 'jpg')
    img.add_header('Content-Id', '<myimage>')
    img.add_header("Content-Disposition", "inline", filename="{}.jpg".format(names))#include image attachment
    html_part.attach(img)
    msg.attach(html_part)
    text = msg.as_string()
    session = smtplib.SMTP('smtp.gmail.com', 587)        
    session.starttls()         
    session.login(email_sender, password)        
    session.sendmail(email_sender, email_receiver, text)         
    session.quit()

def passes(file,img):
    with open(file,'r') as csv_file:
        x=csv.reader(csv_file)
        x=csv.DictReader(csv_file)
        
        for row in x:
            qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_L,
			box_size=3,
			border=3,
			)
            qr.add_data(row['serial'])
            qr.make(fit=True)
            img = qr.make_image()
            image1=Image.open(img).convert('RGBA')
            names=row['FULL NAME']
            email_receiver=row['email']
            txt = Image.new('RGBA', image1.size, (255,255,255,0))
            #fnt=ImageFont.truetype('/Users/preetam/Desktop/python/DobkinScript.ttf',40)
            #fnt1=ImageFont.truetype('/Users/preetam/Desktop/python/DobkinScript.ttf',80)
            fnt2=ImageFont.truetype('/Users/preetam/Desktop/python/DobkinScript.ttf',120)
            d=ImageDraw.Draw(txt)
            d.text((800,1750),row['FULL NAME'], font=fnt2, fill=(0,0,0,255))
            #d.text((230,410),"IRIS#000"+row['serial'], font=fnt2, fill=(0,0,0,255))
            #d.rectangle(((600, 500), (700, 600)), fill="black")
            out = Image.alpha_composite(image1, txt)
            #out.paste(img,(610,510),img)
            out.save('image.png')
            out.show()
            shutil.copy("image.png","{}.jpg".format(names))
            sending_mail('@gmail.com',email_receiver,names,'*******')#login credentials 
passes('.csv','')#files