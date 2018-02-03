#NISHANT JADHAV 
#IEEE-VIT 
#CMPN -A 

import csv
from PIL import Image,ImageDraw,ImageFont
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

with open('IEEE-form.csv','r') as file:
	x = csv.DictReader(file)
	for row in x:
		
		logo = Image.open('iris.jpg')
		image = Image.open('image.jpg')
		large_font = ImageFont.truetype('arial.ttf',80)
		small_font = ImageFont.truetype('arial.ttf',35)
		big_font = ImageFont.truetype('arial.ttf',60)
		

		draw = ImageDraw.Draw(image)
		draw.text(xy=(250,500),text= row['Full Name'],fill=(0,0,0),font = small_font)
		draw.text(xy=(250,600),text= row['Email ID '], fill=(0,0,0),font = small_font)
		draw.text(xy=(2000,250),text= row['Serial no.'],fill=(0,0,0),font = big_font)
		draw.text(xy=(500,250),text="Welcome to IRIS",fill=(0,0,0),font=large_font)

		image.paste (logo,(0,0))
		image.show()
		image.save('pass.jpg')

		email_sender='nishprojects232@gmail.com'
		email_receiver=row['Email ID ']
		body="Here is your  IRIS Pass"
		subject='IEEE- IRIS PASS'


		msg=MIMEMultipart()
		msg['From']= email_sender
		msg['to']= email_receiver
		msg['subject']= subject
		msg.attach(MIMEText(body,'plain'))

		###Working on attachment of Images with EMAIL
		filename = 'pass.jpg'


		attachment = open(filename,'rb')

		part = MIMEBase('application','octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disapositon',"attachment; filename ="+filename)  

		msg.attach(part)
		

		text = msg.as_string()
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(email_sender,'*************')

		server.sendmail(email_sender,email_receiver,text)
		server.quit()




















