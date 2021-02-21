# %%
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

email_from = input('Infome o seu E-mail: ')
email_password = os.getenv('EMAIL_PASSWORD')
email_server = 'smtp.gmail.com'

while True:
    receiver = input('Quais são os destinatarios ?: ')
    list_receivs = [receiver]

    reapt = input('\nAdcionar mais um destinatario?: ')
    if reapt == 's':
        continue
    else:
        break

title = 'E-mail Automatizado com Python'

header = MIMEMultipart()
header['From'] = email_from
header['Subject'] = title

msg = 'A curiosidade é fascinante, a vontade de aprender coisas novas é uma da melhores sensações'
msg_body = MIMEText(msg, 'html')
header.attach(msg_body)

try:
    protocol_smtp = smtplib.SMTP(email_server, 587)
    protocol_smtp.ehlo()
    protocol_smtp.starttls()
    protocol_smtp.ehlo()
    protocol_smtp.login(email_from, email_password)
    protocol_smtp.sendmail(email_from, ','.join(
        list_receivs), header.as_string())
    protocol_smtp.quit()
    print(f'E-mail enviado')
except Exception as error:
    print(f'Falha ao enviar o E-mail, Erro: {error}')

# %%
