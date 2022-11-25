from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
class EmailSender:

    def send_email_to_student(self, r_email, message):
        email_password = "nwzcnxhgvxuigoaj"
        email_sender = "myekini1@gmail.com"
        email_receiver = r_email
        
        
        email = EmailMessage()
        email['From '] = "myekini1@gmail.com"
        email['To'] = r_email
        email['Subject'] = "$ATL BALANCE"
        
        # attach the body with the msg instance
        email_message = email['Subject'].attach(MIMEText(message, 'html'))
        email.set_content(email_message)
        
        # Add SSL (layer of security)
        context = ssl.create_default_context()
        

        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, email.as_string())
    
    def send_email_to_support(self):
        return "support working"

            


        


            