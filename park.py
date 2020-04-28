import ttk as tk
from picamera import PiCamera
from time import sleep

camera = PiCamera()


master = Tk()
a = Button(master, text="Open", command=callopen)
a.pack()

b = Button(master, text="Close", command=callclose)
b.pack()

mainloop()



def callopen():
    camera.start_preview()
def callclose():
    camera.stop_preview()