# SMTP-send message using 'mail.qq.com'
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

#qq邮箱smtp服务器
host_server = 'smtp.qq.com'
#sender_qq为发件人的qq号码
sender_qq = '16***09'
#qq邮箱的授权码
autho_code = 'eim***gha'
#发件人的邮箱
sender_qq_mail = '16***09@qq.com'
#收件人邮箱
receiver = 'flyingfish9344@gmail.com'
#邮件的正文内容
mail_content = '\nHello,this is just a test...\n'
#邮件标题
mail_title = 'A test from Tanglong'
#ssl登录
smtp = SMTP_SSL(host_server)
#set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)

# send mail
smtp.ehlo(host_server)
smtp.login(sender_qq, autho_code)

msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = receiver
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()