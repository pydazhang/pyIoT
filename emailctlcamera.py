import smtplib
import easyimap
import time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 80

server = smtplib.SMTP('smtp.gmail.com', 587)
#server.connect("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.ehlo()
#Next, log in to the server
login = 'Sever username'
password = 'Sever psw'
Sname='Sever username@gmail.com'
server.login(login, password)


    
while 1:
    imapper = easyimap.connect('imap.gmail.com', login, password)
    for mail_id in imapper.listids(limit=1):
        mail = imapper.mail(mail_id)
        if mail.title =='123':
            s = mail.from_addr
            remail=s.split('<')[1]
            email=remail.split('>')[0]
            print(email)
#contents=mail.body
#contents = contents.rstrip('1')
            camera.capture('/home/pi/Desktop/image.jpg')
            time.sleep(5)
                
#packet attachment                
            msg = MIMEMultipart()
            msg.attach(MIMEImage(file("/home/pi/Desktop/image.jpg").read()))
#Send the mail                
            server.sendmail(Sname, email, msg.as_string())
            server.sendmail(Sname, Sname, msg.as_string())
            break
