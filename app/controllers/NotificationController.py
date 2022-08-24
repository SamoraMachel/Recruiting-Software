from ast import Subscript
from dataclasses import dataclass
from email.errors import MessageError
from os import getenv
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

from app.db.Company import Company
from app.db.Employee import Employee

load_dotenv()

EMAIL_SERVER = getenv("EMAIL_SERVER")
EMAIL_PORT = getenv("EMAIL_PORT")
GMAIL_LINK_SETUP = getenv("GMAIL_LINK_SETUP")


class Notification:

    def __init__(self, notifier : Company, subscriber : Employee, message : dict = {}) -> None:
        self.notifier = notifier
        self.subscriber = subscriber
        self.message = message
        
        self.subscriber_email = subscriber.email
        self.__event_listeners = []

    def check_smtp_detail(self):
        if self.subscriber.smtp_email:
            self.notifier_email = self.subscriber.smtp_email
        else:
            raise Exception(f"Please setup your gmail details using the link {GMAIL_LINK_SETUP}")
        if self.subscriber.smtp_password:
            self.email_password = self.subscriber.smtp_password
        
    
    def setup_email(self, email, password):
        self.notifier_email = email
        self.email_password = password

        self.subscriber.smtp_email = email,
        self.subscriber.smtp_password = password
        self.subscriber.update()

    def __send_email(self):
        sender_email = self.notifier_email
        receiver_email = self.subscriber_email
        password = self.email_password

        message = MIMEMultipart("alternative")
        message["Subject"] = self.message.get("title", "")
        message["From"] = sender_email
        message["To"] = receiver_email

        body = self.message.get("body", "")

        _html = MIMEText(body, "html")
        message.attach(_html)
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(EMAIL_SERVER, EMAIL_PORT, context=context) as server:
            try: 
                server.login(sender_email, password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )
            except Exception as e:
                print(e)
                 

    def __send_notification(self):
        print(f"Sending Notification to {self.subscriber.name}....{self.message}")
        return {
            "notifier":self.notifier,
            "subscriber": self.subscriber,
            "notifier_email":self.notifier_email,
            "message": self.message
        }

    def register_email(self):
        self.__event_listeners.append(self.__send_email)
    
    def register_notification(self):
        self.__event_listeners.append(self.__send_notification)
        

    def notify(self):
        for event in self.__event_listeners:
            event()



    