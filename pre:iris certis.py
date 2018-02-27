#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 00:08:00 2018

__author__ = "PREETAM RANE"
__copyright__ = "Copyright 2007, IEEE-VIT STUDENT BRANCH"
__credits__ = ["SAURABH FEGADE"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "IEEE-VIT TECH-WEB TEAM"
__email__ = "ieee@vit.edu.in"
__status__ = "Production"
"""
import csv
from PIL import Image,ImageDraw,ImageFont
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import shutil


def sending_mail(email_sender, email_receiver, names, password):
    subject='certificate'
    msg=MIMEMultipart()
    msg['From']= email_sender
    msg['to']= email_receiver
    msg['subject']= subject
    body = """........... %s"""%names #add body discription here in place of ........
    msg.attach(MIMEText(body,'plain'))
    img_data = open('{}.jpg'.format(names), 'rb').read()
    html_part = MIMEMultipart(_subtype='related')
    body = MIMEText('<img src="cid:myimage" />', _subtype='html')
    html_part.attach(body)
    img = MIMEImage(img_data, 'jpg')
    img.add_header('Content-Id', '<myimage>')
    img.add_header("Content-Disposition", "inline", filename="{}.jpg".format(names))
    html_part.attach(img)
    msg.attach(html_part)
    text = msg.as_string()
    session = smtplib.SMTP('smtp.gmail.com', 587)#server as per requirement       
    session.starttls()         
    session.login(email_sender, password)        
    session.sendmail(email_sender, email_receiver, text)         
    session.quit()

def passes(file,img,textfont):
    with open(file,'r') as csv_file:
        x=csv.reader(csv_file)
        x=csv.DictReader(csv_file)
        
        for row in x:
            image1=Image.open(img).convert('RGBA')
            names=row['FULL NAME']
            email_receiver=row['email']
            txt = Image.new('RGBA', image1.size, (255,255,255,0))
            font_type = ImageFont.truetype(textfont,200)
            d=ImageDraw.Draw(txt)
            x,y = image1.size
            a,b = font_type.getsize(names)
            d.text(xy = (1240-a/2,1750),text=names, font = font_type, fill=(0,0,0,255))#change 1240 and 1750 with desired x y positions
            out = Image.alpha_composite(image1, txt)
            out.save('image.png')
            out.show()
            shutil.copy("image.png","{}.jpg".format(names))
            sending_mail('@gmail.com',email_receiver,names,'********')#login credentials 
passes('.csv','.png','.ttf')#files as per format 