import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

file = open('receiver_list.txt','r')
daftar_penerima = [(line.strip()).split() for line in file]
print(daftar_penerima)
file.close()

email = 'adityamailana1@gmail.com' #tulis email pengirim
password = '12345678Aa@' #tulis password email
send = daftar_penerima #tulis email penerima
subject = 'Tulis Subject di Sini' #Tulis isi subject di sini
message = 'Tulis Pesan di sini' #Tulis isi pesan di sini
    
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send
msg['Subject'] = subject
    
msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send, text)
server.quit()