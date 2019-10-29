#import evdev
#python /usr/local/lib/python2.7/dist-packages/evdev/evtest.py
from evdev import InputDevice, categorize, ecodes
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 80
#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event4')

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    if event.code==164:
        camera.capture('/home/pi/Desktop/image.jpg')
    if event.code==104:
        print("page up")
   