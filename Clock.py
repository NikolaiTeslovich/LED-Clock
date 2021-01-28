#!/usr/bin/env python
# coding: utf-8


import RPi.GPIO as GPIO
import time

#GPIO.cleanup()


# define the segment pins for the led segment

segs = [22, 4, 19, 6, 17, 13, 26]
digits = {0:[1, 1, 1, 0, 1, 1, 1],
          1:[0, 0, 1, 0, 0, 1, 0],
          2:[1, 0, 1, 1, 1, 0, 1],
          3:[1, 0, 1, 1, 0, 1, 1],
          4:[0, 1, 1, 1, 0, 1, 0],
          5:[1, 1, 0, 1, 0, 1, 1],
          6:[1, 1, 0, 1, 1, 1, 1],
          7:[1, 0, 1, 0, 0, 1, 0],
          8:[1, 1, 1, 1, 1, 1, 1],
          9:[1, 1, 1, 1, 0, 1, 1]}


seg1 = 22
seg2 = 4
seg3 = 19
seg4 = 6
seg5 = 17
seg6 = 13
seg7 = 26

# define the pins for the 4 led digits

digs = [23,24,25,12]
dig1 = 23
dig2 = 24
dig3 = 25
dig4 = 12

# define the pin for the blinker
blink = 18

# disable annoying warnings
GPIO.setwarnings(False)

# this is the current numbering layout
GPIO.setmode(GPIO.BCM)

# initialize the led digit segments as outputs
GPIO.setup(seg1, GPIO.OUT)
GPIO.setup(seg2, GPIO.OUT)
GPIO.setup(seg3, GPIO.OUT)
GPIO.setup(seg4, GPIO.OUT)
GPIO.setup(seg5, GPIO.OUT)
GPIO.setup(seg6, GPIO.OUT)
GPIO.setup(seg7, GPIO.OUT)

# initialize the four digits as outputs
GPIO.setup(dig1, GPIO.OUT)
GPIO.setup(dig2, GPIO.OUT)
GPIO.setup(dig3, GPIO.OUT)
GPIO.setup(dig4, GPIO.OUT)

# initialize the middle led second blinker
GPIO.setup(blink, GPIO.OUT)

def zero(digit):

    GPIO.output(seg1, True)
    GPIO.output(seg2, True)
    GPIO.output(seg3, True)
    GPIO.output(seg4, False)
    GPIO.output(seg5, True)
    GPIO.output(seg6, True)
    GPIO.output(seg7, True)

    GPIO.output(digit, True)

def one(digit):

    GPIO.output(seg1, False)
    GPIO.output(seg2, False)
    GPIO.output(seg3, True)
    GPIO.output(seg4, False)
    GPIO.output(seg5, False)
    GPIO.output(seg6, True)
    GPIO.output(seg7, False)

    GPIO.output(digit, True)

def two(digit):

    GPIO.output(seg1, True)
    GPIO.output(seg2, False)
    GPIO.output(seg3, True)
    GPIO.output(seg4, True)
    GPIO.output(seg5, True)
    GPIO.output(seg6, False)
    GPIO.output(seg7, True)

    GPIO.output(digit, True)

def three(digit):

    GPIO.output(seg1, True)
    GPIO.output(seg2, False)
    GPIO.output(seg3, True)
    GPIO.output(seg4, True)
    GPIO.output(seg5, False)
    GPIO.output(seg6, True)
    GPIO.output(seg7, True)

    GPIO.output(digit, True)

def four(digit):

    GPIO.output(seg1, False)
    GPIO.output(seg2, True)
    GPIO.output(seg3, True)
    GPIO.output(seg4, True)
    GPIO.output(seg5, False)
    GPIO.output(seg6, True)
    GPIO.output(seg7, False)

    GPIO.output(digit, True)

def five(digit):

    GPIO.output(seg1, True)
    GPIO.output(seg2, True)
    GPIO.output(seg3, False)
    GPIO.output(seg4, True)
    GPIO.output(seg5, False)
    GPIO.output(seg6, True)
    GPIO.output(seg7, True)

    GPIO.output(digit, True)

def six(digit):

    GPIO.output(seg1, True)
    GPIO.output(seg2, True)
    GPIO.output(seg3, False)
    GPIO.output(seg4, True)
    GPIO.output(seg5, True)
    GPIO.output(seg6, True)
    GPIO.output(seg7, True)

    GPIO.output(digit, True)

def seven(digit):

    GPIO.output(seg1, True)
    GPIO.output(seg2, False)
    GPIO.output(seg3, True)
    GPIO.output(seg4, False)
    GPIO.output(seg5, False)
    GPIO.output(seg6, True)
    GPIO.output(seg7, False)

    GPIO.output(digit, True)

def eight(digit):

    GPIO.output(seg1, True)
    GPIO.output(seg2, True)
    GPIO.output(seg3, True)
    GPIO.output(seg4, True)
    GPIO.output(seg5, True)
    GPIO.output(seg6, True)
    GPIO.output(seg7, True)

    GPIO.output(digit, True)

def nine(digit):

    GPIO.output(seg1, True)
    GPIO.output(seg2, True)
    GPIO.output(seg3, True)
    GPIO.output(seg4, True)
    GPIO.output(seg5, False)
    GPIO.output(seg6, True)
    GPIO.output(seg7, True)

    GPIO.output(digit, True)

def blink(boolean):

    GPIO.output(18, boolean)

def digoff(digit):

    GPIO.output(seg1, False)
    GPIO.output(seg2, False)
    GPIO.output(seg3, False)
    GPIO.output(seg4, False)
    GPIO.output(seg5, False)
    GPIO.output(seg6, False)
    GPIO.output(seg7, False)

    GPIO.output(digit, False)

def gettime():

    current_time = []
    t = time.localtime()
    start = time.time()
    current_time = time.strftime("%H%M%S", t)
    return current_time

actual_time = gettime()

while True:

    i = 0

    j = 0

    dig = 0

    actual_time = gettime()

    while j < 1000:


        while i < 4:

            if i == 0:
                dig = dig1

            elif i == 1:
                dig = dig2

            elif i == 2:
                dig = dig3

            elif i == 3:
                dig = dig4


            if actual_time[i] == '0':
                zero(dig)

            elif actual_time[i] == '1':
                one(dig)

            elif actual_time[i] == '2':
                two(dig)

            elif actual_time[i] == '3':
                three(dig)

            elif actual_time[i] == '4':
                four(dig)

            elif actual_time[i] == '5':
                five(dig)

            elif actual_time[i] == '6':
                six(dig)

            elif actual_time[i] == '7':
                seven(dig)

            elif actual_time[i] == '8':
                eight(dig)

            elif actual_time[i] == '9':
                nine(dig)

            if int(actual_time[5]) % 2 == 0:
                blink(True)

            elif int(actual_time[5]) % 2 == 1:
                blink(False)

           # time.sleep(0.002)

            digoff(dig)

            i += 1

        j += 1

