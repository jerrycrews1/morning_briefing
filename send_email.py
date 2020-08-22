import ssl
import smtplib

from mako.template import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# for loading the .env file
import os
from dotenv import load_dotenv
load_dotenv()

GMAIL_EMAIL = os.getenv("GMAIL_EMAIL")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")


def send_email(var_dicts):
    port = 465
    smtp_server = "smtp.gmail.com"

    recipients = []
    message = MIMEMultipart("alternative")
    message["Subject"] = "Your Morning Briefing"
    message["From"] = GMAIL_EMAIL
    message['To'] = ", ".join(recipients)

    text = """\
    Honestly, if this didn't load, sorry.  We can do better than this!"""
    mytemplate = Template(filename='email.html', default_filters=['decode.utf8'], input_encoding='utf-8',
                          )
    html = mytemplate.render(**var_dicts)

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(GMAIL_EMAIL, GMAIL_PASSWORD)
        server.sendmail(GMAIL_EMAIL, recipients, message.as_string())
