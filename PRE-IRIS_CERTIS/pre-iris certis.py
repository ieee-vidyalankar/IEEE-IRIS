#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:13:13 2018

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
    body ="""""" #add body no changes are to be made here
    msg.attach(MIMEText(body,'plain'))
    img_data = open('{}.jpg'.format(names), 'rb').read()
    html_part = MIMEMultipart(_subtype='related')
    body = MIMEText('<H1>Greetings %s!</H1><p><h4>Thanks for attending Pre-IRIS.<br><br>We hope that the event was beneficial for you.<br><br>Kindly find your E-Certificate for the same, attached along with this mail.<br>We look forward to seeing you at all our future workshops, seminars and events!<br><br>Regards,<br>IEEE-VIT Student Branch<br><center><br>Follow us on<br><p><a href="https://twitter.com/vidyalankarieee?lang=en"><img src="http://icons.iconarchive.com/icons/sicons/basic-round-social/512/twitter-icon.png" height="50" width="50" hspace="20"><a href="https://www.instagram.com/ieeevit/"><img src="https://images-na.ssl-images-amazon.com/images/I/71VQR1WetdL.png" height="50" width="50" hspace="20"><a href="https://www.facebook.com/IEEEVIT1/"><img src="https://ioufinancial.com/wp-content/uploads/2017/02/facebook.png" height="50" width="50" hspace="20"></a><br><h7>click to follow<br></center><p>For any errors in certificate<a href="https://docs.google.com/forms/d/e/1FAIpQLScIov5y2i4nk6UzJMTmxW9D777GdSh2QaoTICNU7Scc9PwcOA/viewform?c=0&w=1&usp=mail_form_link"> click here</p><img src="cid:myimage" />'%names, _subtype='html')
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
            names=row['Full Name (as required on certificate)']
            email_receiver=row['E-mail']
            txt = Image.new('RGBA', image1.size, (255,255,255,0))
            font_type = ImageFont.truetype(textfont,45)
            d=ImageDraw.Draw(txt)
            x,y = image1.size
            a,b = font_type.getsize(names)
            d.text(xy = (440-a/2,240),text=names, font = font_type, fill=(33,140,141,255))#change 440 and 240 with desired x y positions
            out = Image.alpha_composite(image1, txt)
            out.save('image.png')
            out.show()
            shutil.copy("image.png","{}.jpg".format(names))
            sending_mail('ieeevitcertificates@gmail.com',email_receiver,names,'*********')#login credentials 
passes('.csv','certi of preiris 2.png','CODE Bold.otf')#files as per format 

