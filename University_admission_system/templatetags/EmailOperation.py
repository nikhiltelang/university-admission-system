import smtplib
from email.message import EmailMessage
class EmailManagement:
    def __init__(self):
        pass

    def sendEmail(self,sender,receiver,message):
        try:
            smtp = smtplib.SMTP('smtp.gmail.com',587)
            smtp.ehlo()
            smtp.starttls()
            smtp.login("nikhiltelang70@ gmail.com","Nikhil@1234")
            smtp.sendmail(sender,receiver,message)
            # smtp.close()
            print("Email send Successfully")
        except Exception as e:
            print(e)
            return e