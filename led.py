import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

while True:
    GPIO.output(18, True)
    GPIO.output(23, True)
    GPIO.output(24, True)
    GPIO.output(25, True)
    GPIO.output(12, True)
    
    GPIO.output(4, True)
    GPIO.output(17, True)
    GPIO.output(22, True)
    GPIO.output(6, True)
    GPIO.output(13, True)
    GPIO.output(19, True) 
    GPIO.output(26, True)
   
    time.sleep(0.0001)
    
    GPIO.output(18, False)
    GPIO.output(23, False)
    GPIO.output(24, False)
    GPIO.output(25, False)
    GPIO.output(12, False)
    
    GPIO.output(4, False)
    GPIO.output(17, False)
    GPIO.output(22, False)
    GPIO.output(6, False)
    GPIO.output(13, False)
    GPIO.output(19, False)
    GPIO.output(26, False)
    
    time.sleep(0.0099)
