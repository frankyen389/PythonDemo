# -*- coding: utf-8 -*-
'''
Created on 2016年7月1日

@author: frank_yen
'''

import smtplib
from email.mime.text import MIMEText

def sendMail(smtp_host, smtp_port, sender, recipients, title, message):
    s = smtplib.SMTP(smtp_host, smtp_port)
    msg = MIMEText(message)
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    s.sendmail(sender, recipients, msg.as_string())

if __name__ == '__main__':
    try:
        title = 'Mail Sender'
        message = 'Mail Sender Test'
        recipients = ['frank_yen@cht.com.tw', 'javamidlet@gmail.com']
        sendMail('192.168.30.67', '10025', 'fsdadmin@cht.com.tw', recipients, title, message)
        print "it's been sent a mail"
    except:
        print "can't send email"
