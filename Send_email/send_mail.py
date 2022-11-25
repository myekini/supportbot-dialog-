from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class EmailSender:

    def send_email_to_student(self, r_email, message):
        email_password = "nwzcnxhgvxuigoaj"
        email_sender = "myekini1@gmail.com"
        email_receiver = r_email
        
    
        email = MIMEMultipart("alternative")
        email["Subject"] = "$ATL BALANCE"
        email["From"] = "myekini1@gmail.com"
        email["To"] = r_email

        # Turn these into plain/html MIMEText objects
        part = MIMEText(message, "html")
        

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        email.attach(part)

        
        # Add SSL (layer of security)
        context = ssl.create_default_context()
        
        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, email.as_string())
    
    def send_email_to_support(self):
        return "support working"

            



            