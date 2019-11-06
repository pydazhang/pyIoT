import RPi.GPIO as GPIO
import time
import pyfirmata, pyfirmata.util

board=pyfirmata.Arduino('/dev/ttyACM0')
iterator = pyfirmata.util.Iterator(board)
iterator.start()
time.sleep(1)
board.analog[0].enable_reporting()


servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start(0)
try:
    while True:
        a=board.analog[0].read()
        if a == None:
            pass
        else:
            a
            if 0.2 <= a <= 0.8:
                print('stop')
                pass
            else:
                if a>0.8:
                    p.ChangeDutyCycle(2)
                    print('large')
                    time.sleep(0.1)
                    p.ChangeDutyCycle(0)
                if a<0.2:
                    p.ChangeDutyCycle(9)
                    print('less')
                    time.sleep(0.1)
                    p.ChangeDutyCycle(0)

 # GPIO 17 for PWM with 50Hz # Initialization

#  while True:
#      if board.analog[0].read() == None:
#          pass
#      else:
      
#      print(board.analog[0].read())
#          if 0.2 <= board.analog[0].read() <= 0.8:
#            p.ChangeDutyCycle(7.2)
#            print("stop")
#            p.stop()
#          if board.analog[0].read()>0.8:
#            p.start(7.2)
#            p.ChangeDutyCycle(6)
#            print("larger")
 #           time.sleep(1)
#          if board.analog[0].read()<0.2:
#            p.start(7.2)
#            p.ChangeDutyCycle(8)
#            print("less")
#            time.sleep(1)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()