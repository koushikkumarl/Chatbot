from flask import Flask
from flask_mail import Mail, Message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def sendmailfile():
    MAIL_USERNAME = 'testiiitb01@gmail.com'
    MAIL_PASSWORD = 'machinelearning'
    RECEIVER = 'koushik.feb11@gmail.com'
    MAIL_SERVER = smtplib.SMTP('smtp.gmail.com',587)
    MAIL_SERVER.starttls()
    MAIL_SERVER.login(MAIL_USERNAME, MAIL_PASSWORD)
    SUBJECT = 'Restaurant details from ChatBot'
    MSG = MIMEMultipart()
    MSG['From'] = MAIL_USERNAME
    MSG['TO'] = RECEIVER
    MSG['Subject'] = SUBJECT
    #BODY = tracker.get_slot('emailbody')
    BODY = 'This is body of Email'
    MSG.attach(MIMEText(BODY,'plain'))
    text = MSG.as_string()
    MAIL_SERVER.sendmail(MAIL_USERNAME,RECEIVER,text)
    MAIL_SERVER.close()

sendmailfile()