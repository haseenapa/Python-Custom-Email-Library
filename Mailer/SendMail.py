"""
title           :SendMail.py
description     :Custom package to send a mail
author          :Haseena
date            :26-09-2016
python_version  :2.7.10
ref link : http://stackoverflow.com/questions/27272367/trying-to-send-email-from-python
"""

# Import smtplib for the actual sending function
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

class SendMail(object):
    """Initialising config variables"""
    def __init__(self, config):
        """Call to setconfig"""
        self.setconfig(config)
    def setconfig(self, config):
        """Initialising config variables"""
        self.config = config
    def sendmail(self, data):

        """Initialising config variables"""
        

        try:
            # Send an email with html or plain text
            msg = MIMEMultipart()
            msg['From'] = (data.has_key('From')) and data['From'] or self.config['server_mail']
            msg['To'] = ", ".join(data['To'])
            msg['Subject'] = (data.has_key('Subject')) and data['Subject'] or ''
            html = (data.has_key('Message_Type')) and data['Message_Type'] or 'html'
            receiver = data['To']
            if data.has_key('Cc'):
                msg['Cc'] = ", ".join(data['Cc'])
                receiver += data['Cc']
            if data.has_key('Bcc'):
                msg['Bcc'] = ", ".join(data['Bcc'])
                receiver += data['Bcc']
            msg.attach(MIMEText(data['Message'], html))

            #send an email with attachment
            if data.has_key('Filepath'):
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(open(data['Filepath'], "rb").read())
                filename = os.path.basename(data['Filepath']) #to get the file name from path
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                msg.attach(part)

            #smtp connection
            server = smtplib.SMTP(self.config['server'], self.config['port'])
            server.ehlo()
            server.starttls()
            server.ehlo()

            #log in to the server
            server.login(self.config['server_mail'], self.config['server_pass'])

            # send mail
            server.sendmail(msg['From'], receiver, msg.as_string())
            server.close()
            print "Successfully sent email"
        except smtplib.SMTPException, error:
            print str(error)
            print "Error: unable to send email"
