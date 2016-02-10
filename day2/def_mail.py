#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

"""
def mail():
    ret=True
    try:
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["吴老师",'wptawy@126.com'])
        msg['To'] = formataddr(["willian",'@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.126.com", 25)
        server.login("wptawy@126.com", "passwd")
        server.sendmail('wptawy@126.com', ['@qq.com',], msg.as_string())
        server.quit()
    except Exception:
        ret=False
    return ret

ret = mail()
if ret:
    print('发送成功')
else:
    print("发送失败")
    """
def show():
    print('a')
    if 1==2:
        return [11,22]
    print('b')

ret=show()
print(ret)