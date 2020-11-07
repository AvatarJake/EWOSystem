import smtplib
from email.mime.multipart import MIMEMultipart
from administrar.models import *
from email.mime.text import MIMEText

emails=Miembro.objects.all()
destino=[]

for e in emails:
    destino.append(e.email)
    print(e.email)

msg= MIMEMultipart()
direccionenvio = 'ewosystem@gmail.com'
msg['From'] = direccionenvio
msg['To']= ",".join(destino)
msg['Subject']= 'Nuevo evento Programado'

html_body =f'''
<html>
    <head></head>
    <body>
    <h1>Hola , se ha programado un nuevo evento</h1>
    <p>'Donacion de estufas'</p>
    <p>'El Morral'</p>
    <p>'fecha'</p>
    </body>
</html>
'''
msg.attach(MIMEText(html_body,'html'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('ewosystem@gmail.com','jake09101989')

text = msg.as_string()

server.sendmail(direccionenvio,destino,text)

server.quit()

print("el correo fue enviado!")