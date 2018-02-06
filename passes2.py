#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:19:56 2018

__author__ = "PREETAM RANE"
__copyright__ = "Copyright 2007, IEEE-VIT STUDENT BRANCH"
__credits__ = ["PRATIK BHURAN", "NISHANT JADHAV", "HEMANT SIRSAT"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "IEEE-VIT TECH-WEB TEAM"
__email__ = "ieee@vit.edu.in"
__status__ = "Production"
"""
 

import csv
import qrcode
from PIL import Image,ImageDraw,ImageFont
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

import shutil

with open('tty.csv','r') as csv_file:
	
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
		
		image1=Image.open('TICKET_png.png').convert('RGBA')
		txt = Image.new('RGBA', image1.size, (255,255,255,0))
		fnt=ImageFont.truetype('/Users/preetam/Desktop/blackjack.otf',40)
		fnt1=ImageFont.truetype('/Users/preetam/Desktop/blackjack.otf',32)
		fnt2=ImageFont.truetype('/Users/preetam/Desktop/blackjack.otf',32)

		d=ImageDraw.Draw(txt)
		d.text((230,360),row['first_name']+" "+row['last_name'], font=fnt2, fill=(0,0,0,255))
		d.text((230,410),"IRIS#000"+row['serial'], font=fnt2, fill=(0,0,0,255))
		d.rectangle(((600, 500), (700, 600)), fill="black")
		out = Image.alpha_composite(image1, txt)
		out.paste(img,(610,510),img)
		out.save('image.png')
		shutil.copy("image.png","{}.png".format(row['first_name']+" "+row['last_name']))

		email_sender='@vit.edu.in'#email id
		email_receiver=row['email']
		body="Here is your  PRE-IRIS Pass"
		subject='IEEE- IRIS PASS'


		msg=MIMEMultipart()
		msg['From']= email_sender
		msg['to']= email_receiver
		msg['subject']= subject
		msg.attach(MIMEText(body,'plain'))



		img_data = open('{}.png'.format(row['first_name']+" "+row['last_name']), 'rb').read()

		html_part = MIMEMultipart(_subtype='related')
		body = MIMEText('<H7><font face = "Comic sans MS">Please download the pass and carry with you during event</font></H7><img src="cid:myimage" />', _subtype='html')
		html_part.attach(body)

		img = MIMEImage(img_data, 'png')
		img.add_header('Content-Id', '<myimage>')
		img.add_header("Content-Disposition", "inline", filename="myimage")
		html_part.attach(img)
		  

		msg.attach(html_part)

		text = msg.as_string()
		smtpsrv = "smtp.office365.com"
		smtpserver = smtplib.SMTP(smtpsrv,587)
		smtpserver.starttls()
		smtpserver.login(email_sender,'********')#password
		smtpserver.ehlo()
		smtpserver.sendmail(email_sender,email_receiver,text)
		smtpserver.quit()






























