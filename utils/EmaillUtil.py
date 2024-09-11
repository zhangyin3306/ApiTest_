import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.Conf import ConfigYaml

class SendUtil:
    def __init__(self,smtp_addr,username,password,recv,title,content = None,file=None):
        self.smtp_addr = smtp_addr
        self.username = username
        self.password = password
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file
    def send(self):
        msg = MIMEMultipart()
        msg['Subject'] = self.title
        msg['From'] = self.username
        msg['To'] = self.recv
        if self.file:
            att = MIMEText(open(self.file).read(), 'plain', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="%s"' % self.file
            msg.attach(att)
        self.smtp = smtplib.SMTP(self.smtp_addr, port=25,local_hostname='utf-8')
        self.smtp.login(self.username, self.password)
        self.smtp.sendmail(self.username, self.recv, msg.as_string())
if __name__ == '__main__':
   from config.Conf import ConfigYaml
   email_info = ConfigYaml().get_conf_email()
   smtp_addr = email_info['smtpserver']
   username = email_info['username']
   password = email_info['password']
   recv = email_info['receiver']
   email = SendUtil(smtp_addr,username,password,recv,"测试")
   email.send()