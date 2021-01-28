import RPi.GPIO as GPIO
import time

# define the segments, digits, and numbers
segs = [22, 4, 19, 6, 17, 13, 26]
digs = [23, 24, 25, 12]

num = {0:[True, True, True, False, True, True, True],
1:[False, False, True, False, False, True, False],
2:[True, False, True, True, True, False, True],
3:[True, False, True, True, False, True, True],
4:[False, True, True, True, False, True, False],
5:[True, True, False, True, False, True, True],
6:[True, True, False, True, True, True, True],
7:[True, False, True, False, False, True, False],
8:[True, True, True, True, True, True, True],
9:[True, True, True, True, False, True, True]}

off = [False, False, False, False, False, False, False]

blink = 18

# this is the current numbering layout
GPIO.setmode(GPIO.BCM)

# disable annoying warnings
GPIO.setwarnings(False)

# initialize the led digits and segments as outputs
GPIO.setup(segs, GPIO.OUT)
GPIO.setup(digs, GPIO.OUT)
GPIO.setup(blink, GPIO.OUT)

def gettime():
    return time.strftime("%H%M", time.localtime())

timestr = gettime()

GPIO.output(segs, num[1])

while True:

    GPIO.cleanup()

    gettime()

    d = 0

    while d < 4:

        GPIO.output(digs[d], True)
        GPIO.output(segs, num[timestr[d]])

        d += 1

        time.sleep(0.1)
