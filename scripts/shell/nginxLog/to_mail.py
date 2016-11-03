#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib,os,sys
from email.mime.text import MIMEText
mailto_list=[""]
mail_host="smtp.exmail.qq.com"
mail_user="tom@ex.cn"
mail_pass="xx"
mail_postfix="ex.cn"


#cwd=os.path.abspath('temp.txt')
cwd="/usr/local/bin/slow_interface/temp.txt"

with open(cwd,'r') as f:
    content=f.read()

def send_mail(to_list,sub,content):
    me="willian"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='utf8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mailto_list,"xx","xx%s"%content):
        print "success"
    else:
        print "fail"
