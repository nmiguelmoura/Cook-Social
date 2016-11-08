import smtplib
from email.mime.text import MIMEText

import secret_code


class SendMessage:
    secret_code = secret_code.PreSecretCode()
    loginData = secret_code.get_mailgun_login()

    def __init__(self):
        pass

    def send_password(self, sendTo, password):
        msg = MIMEText('Password recovery. Your new password to Social Cook is: "%s"' % password)
        msg['Subject'] = "Hello"
        msg['From'] = "SocialCook@SocialCook.com"
        msg['To'] = sendTo
        self.send_mail(msg)

    def send_contact(self, email, message):
        msg = MIMEText('Hi Nuno, "%s" sent you the following message: "%s"' % (email, message))
        msg['Subject'] = "Hello"
        msg['From'] = "SocialCook@SocialCook.com"
        msg['To'] = "nmiguelmoura@gmail.com"
        self.send_mail(msg)

    def send_mail(self, msg):

        s = smtplib.SMTP('smtp.mailgun.org', 587)

        s.login(self.loginData["login"], self.loginData["password"])
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()