import Tkinter as tk
from picamera import PiCamera
import time
import bluetooth
import matplotlib.pyplot as plt
import matplotlib.animation as animation

camera = PiCamera()

y=[]
x=[]
z=[]
for i in range(10):
    x.append(i)
    y.append(0)
    z.append(0)
tg=0.4

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

print (str(obd.recv(20)))

obd.send('AT H0\r\n')

time.sleep(tg)

print (str(obd.recv(20)))

obd.send('AT L0\r\n')

time.sleep(tg)

print (str(obd.recv(20)))

obd.send('AT SP 0\r\n')

time.sleep(tg)

print (str(obd.recv(20)))

obd.send('01 00\r\n')

time.sleep(tg)

obd.recv(20)

time.sleep(tg)

obd.recv(20)

time.sleep(tg)

print (str(obd.recv(20)))

 

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

 mph10=int(mphA, 16)*0.621371
 z.append(mph10)
 z.pop(0)

 c.config(text="Speed is: %d" %mph10)

 c.after(500, mphloop)


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

 y.append(rpm)
 y.pop(0)
 d.after(500, rpmloop)
 

mphloop()
rpmloop()








def Checkenginelight():

 cel= tk.Toplevel(master)

 obd.send('0101\r\n')

 time.sleep(tg)

 DTC = obd.recv(20)

 DTC=int(DTC[6:8],16)-128

 DTCnumber = tk.Label(cel, text="Checking" )

 DTCnumber.pack()

 if DTC<0:

    DTCnumber.config(text="0 code found", font=('calibri','40','bold'))

 else:

    DTCnumber.config(text="%s codes found" %DTC, font=('calibri','40','bold'))

    for x in range(DTC):

        obd.send('03\r\n')

        time.sleep(tg)

        response[x] = obd.recv(20)

        process=response[x]

        process=process[3:5]+process[6:8]

        response[x]=process

        resplabel=tk.Label(cel, text="Engine light code: %s" %response[x], font=('calibri','40','bold'))

        resplabel.pack()

        

e=tk.Button(master, text="Check engine light", font=('calibri','40','bold'), command=Checkenginelight)
e.pack()


fig = plt.figure()
#creating a subplot 
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)



def animate(i):
   
    
    ax1.clear()
    ax1.plot(x, y)
    ax2.clear()
    ax2.plot(x, z)
ani = animation.FuncAnimation(fig, animate, interval=1000) 
plt.show()
master.mainloop()

