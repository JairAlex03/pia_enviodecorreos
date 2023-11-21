import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
msg = MIMEMultipart()
msg['From'] = ''
msg['To'] = 'gerardo.bernal@uanl.edu.mx'
msg['Subject'] = 'Prueba de envio(script Phyton)-1862507'
body = "Practica 12 \n\n Ejercicio de la practica 12 Para envio de correos \n Nombre: Jair Alejandro Gonzalez Ramirez \n Matricula: 1862507."
msg.attach(MIMEText(body, 'plain'))

attachment = open(r'C:\Users\jair_\Downloads\fcfm_cool.png', 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename=fcfm_cool.png")
msg.attach(part)
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.starttls()
conn.login('jairalex907.3@gmail.com', '')
conn.sendmail('jairalex907.3@gmail.com', 'gerardo.bernal@uanl.edu.mx', msg.as_string())

