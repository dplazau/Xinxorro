import socket
import smtplib
import time

email = "dplaza@tryento.com"
password = "72e(q|{ih2yT"
to = "rodolfoplaza@hotmail.com"

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

with smtplib.SMTP_SSL('35.214.219.34', 465) as smtp:

    smtp.login(email, password)

    subject = "{} {}".format(hostname, time.ctime())
    body = "{}".format(local_ip)

    msg = "Subject: {}\n\n{}".format(subject, body)

    smtp.sendmail(email, to, msg)