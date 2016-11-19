#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail(user):
    ret=True
    try:
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["吴老师",'wptawy@126.com'])
        #msg['To'] = formataddr(["willian",'284607861@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.126.com", 25)
        server.login("wptawy@126.com", "WW.3945.59")
        server.sendmail('wptawy@126.com', [user,], msg.as_string())
        server.quit()
    except Exception:
        ret=False
    return ret

ret = mail('284607860@qq.com')
if ret:
    print('发送成功')
else:
    print("发送失败")
