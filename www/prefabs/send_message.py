import smtplib
from email.mime.text import MIMEText

import secret_codes


class SendMessage:
    """Class that allows system to send emails. This code is similar to the one
    given on Mailgun examples page (http://www.mailgun.com/)."""

    # Instantiate PreSecretCode class.
    secret_code = secret_codes.SecretCode()

    # Get smtp login data.
    loginData = secret_code.get_mailgun_login()

    def __init__(self):
        pass

    def send_password(self, sendTo, password):
        # Compose message if user requests new password
        msg = MIMEText(
            'Password recovery. Your new password to Social Cook is: "%s"' % password)
        msg['Subject'] = "Hello"
        msg['From'] = "SocialCooks@SocialCooks.org"
        msg['To'] = sendTo
        self.send_mail(msg)

    def send_contact(self, email, message):
        # Compose message if user sends message to portal
        msg = MIMEText('Hi Nuno, "%s" sent you the following message: "%s"' % (
        email, message), "plain", "utf-8")
        msg['Subject'] = "Hello"
        msg['From'] = "SocialCooks@SocialCooks.org"
        msg['To'] = "nmiguelmoura@gmail.com"
        self.send_mail(msg)

    def send_mail(self, msg):
        # Send mail
        s = smtplib.SMTP('smtp.mailgun.org', 587)
        s.login(self.loginData["login"], self.loginData["password"])
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()
