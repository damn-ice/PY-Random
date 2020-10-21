import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 587)

server.ehlo()

server.starttls()

with open("password.txt", "r") as pas:
    password = pas.read()

server.login("joel.default1@gmail.com", password)

msg = MIMEMultipart()

msg["From"] = "Damn-!cE"
msg["To"] = "joelik18@gmail.com"
msg["Subject"] = "Network With Python"

with open("message.txt", "r") as mesg:
    message = mesg.read()

# Attach body of message... 
msg.attach(MIMEText(message, "plain"))

filename = "code.jpg"
attachment = open(filename, "rb")

p = MIMEBase("application", "octet-stream")

p.set_payload(attachment.read())
encoders.encode_base64(p)

p.add_header("Content-Disposition", f"attachment; filename={filename}")

# Attach picture...
msg.attach(p)

text = msg.as_string()

server.sendmail("joel.default1@gmail.com", "joelik18@gmail.com", text)

print("done")

# print(attachment)