'''SMTP(simple mail transfer protocol)
--------------------------------------
-->This is used to send emails from server to another server

Note:
-----
1) SMTP SSL Port:
----------------
465

2)SMTP TLS Port:
---------------
587

import smtplib

EmailMessage Class
------------------
msg['Subject'] = 'SMTP ON Mail'
msg['From'] = 'sender@mail.com'
msg['To'] = 'Receiver@mail.com'

app password 'jfpv wooc nxmi lygj

import smtplib
from email.message import EmailMessage
sender='reshmanaguru30@gmail.com'
password='jfpvwoocnxmilygj'
msg=EmailMessage()
msg['Subject'] = 'Welcome Mail'
msg['From'] = sender
msg['To'] = 'deepthiseerapu2004@gmail.com'
msg.set_content('Hai')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()'''

import smtplib
from email.message import EmailMessage

sender='reshmanaguru30@gmail.com'
password='oumyzsgkvaljghsf'
receiver=['kavs14345@gmail.com','deepthiseerapu2004@gmail.com']
server = smtplib.SMTP ('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
for email in receiver:
    msg = EmailMessage()
    msg['Subject'] = 'Infosys'
    msg['From'] = sender
    msg['To'] = email
    msg.set_content('you are successfully rejected for infosys')
    server.send_message(msg)
server.quit()










    
















