import Tkinter as tk
from picamera import PiCamera
import time
import bluetooth

camera = PiCamera()
tg=0.5
def callopen():
    camera.start_preview(fullscreen=False, window=(100,20,640,480))
def callclose():
    camera.stop_preview()

obd = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
obd.connect(('00:1D:A5:1D:06:EC', 1))
obd.send('AT Z\r\n')
time.sleep(tg)
data = obd.recv(20)
print (str(data))
obd.send('AT E0\r\n')
time.sleep(tg)
data = obd.recv(20)
print (str(data))
obd.send('AT H0\r\n')
time.sleep(tg)
data2 = obd.recv(20)
print (str(data2))
obd.send('AT L0\r\n')
time.sleep(tg)
data = obd.recv(20)
print (str(data))
obd.send('AT SP 0\r\n')
time.sleep(tg)
data3 = obd.recv(20)
print (str(data3))
obd.send('01 00\r\n')
time.sleep(tg)
data4 = obd.recv(20)
time.sleep(tg)
data6 = obd.recv(20)
time.sleep(tg)
data7 = obd.recv(20)
print (str(data7))
 
master = tk.Tk()
a = tk.Button(master, text="Open", font=('calibri','40','bold'), command=callopen)
a.pack()
b = tk.Button(master, text="Close", font=('calibri','40','bold'), command=callclose)
b.pack()
c = tk.Label(master,font=('calibri','40','bold'))
d = tk.Label(master,font=('calibri','40','bold'))
c.pack()
d.pack()

def mphloop():
 obd.send('010d\r\n')
 time.sleep(tg)
 mph = obd.recv(20)
 mphA=mph[6:8]
 mph10=int(mphA, 16)
 c.config(text="Speed is: %d" %mph10)
 c.after(800, mphloop)

def rpmloop():
 obd.send('010C\r\n')
 time.sleep(tg)
 rpm = obd.recv(20)
 rpmA=rpm[6:8]
 rpmB=rpm[9:11]
 rpmA10=int(rpmA, 16)
 rpmB10=int(rpmB, 16)
 
 rpm=(256*rpmA10+rpmB10)/4
 d.config(text="rpm is: %d" %rpm)
 d.after(800, rpmloop)
mphloop()
rpmloop()

master.mainloop()




