import smtplib

MY_EMAIL = 'YOUR GMAIL ACCOUNT'
MY_PASSWORD = 'YOUR PASSWORD'

class SendMail():
    def __init__(self):
        self.connection = smtplib.SMTP("smtp.gmail.com", 587)
        self.connection.starttls()
        self.connection.login(user=MY_EMAIL, password=MY_PASSWORD)

    def sendmail(self, name, email, phone, message):
        self.connection.sendmail(from_addr=MY_EMAIL,
                                  to_addrs=MY_EMAIL,
                                  msg=f"Subject:New Blog Message!\n\n"
                                      f"Name: {name}\n"
                                      f"Email: {email}\n"
                                      f"Phone: {phone}\n"
                                      f"Message: {message}")

        self.connection.quit()
            
                                        
    