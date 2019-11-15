#!/usr/bin/python

import pylirc, time
import RPi.GPIO as GPIO

blocking = 0;


def setup():

    pylirc.init("pylirc", "./conf", blocking)

def button(config):
    if config == 'KEY_LEFT':
        print ('LEFT')

    if config == 'KEY_ENTER':
        print ('ENTER')

    if config == 'KEY_RIGHT':
        print ('RIGHT')

    if config == 'KEY_UP':
        print ('UP')

    if config == 'KEY_DOWN':
        print ('DOWN')

    if config == 'KEY_PLAYPAUSE':
        print ('PLAYPAUSE')

    if config == 'KEY_VOLUMEDOWN':
        print ('VOLUMEDOWN')

    if config == 'KEY_VOLUMEUP':
        print ('VOLUMEUP')

    if config == 'KEY_BACK':
        print ('BACK')
  
    if config == 'KEY_ENTER':
        print ('ENTER')

    if config == 'KEY_STOP':
        print ('STOP')
    if config == 'KEY_SETUP':
        print ('SETUP')

    if config == 'KEY_KP0':
        print ('0')
        
    if config == 'KEY_KP1':
        print ('1')
    if config == 'KEY_KP2':
        print ('2')
        
    if config == 'KEY_KP3':
        print ('3')
    if config == 'KEY_KP4':
        print ('4')
        
    if config == 'KEY_KP5':
        print ('5')
    if config == 'KEY_KP6':
        print ('6')
        
    if config == 'KEY_KP7':
        print ('7')
    if config == 'KEY_KP8':
        print ('8')
        
    if config == 'KEY_KP9':
        print ('9')
        
def loop():
    while True:
        s = pylirc.nextcode(1)
        
        while(s):
            for (code) in s:
#                print 'Command: ', code["config"] #For debug: Uncomment this
#               line to see the return value of buttons
                button(code["config"])
            if(not blocking):
                s = pylirc.nextcode(1)
            else:
                s = []

def destroy():
    pylirc.exit()

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()
'''

import os
a=os.popen("irw").read()
#echo=ech.split()
print(type(a))
'''