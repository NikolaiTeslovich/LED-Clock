#!/usr/bin/env python
# coding: utf-8

# In[12]:


import RPi.GPIO as GPIO
import time

#GPIO.cleanup()


# In[13]:


segs = [22, 4, 19, 6, 17, 13, 26]
digs = [23, 24, 25, 12]

num = [[True, True, True, False, True, True, True],
       [False, False, True, False, False, True, False],
       [True, False, True, True, True, False, True],
       [True, False, True, True, False, True, True],
       [False, True, True, True, False, True, False],
       [True, True, False, True, False, True, True],
       [True, True, False, True, True, True, True],
       [True, False, True, False, False, True, False],
       [True, True, True, True, True, True, True],
       [True, True, True, True, False, True, True]]

blink = 18


# In[16]:


# this is the current numbering layout
GPIO.setmode(GPIO.BCM)

# disable annoying warnings
GPIO.setwarnings(False)

# initialize the led digits and segments as outputs
GPIO.setup(segs, GPIO.OUT)
GPIO.setup(digs, GPIO.OUT)
GPIO.setup(blink, GPIO.OUT)


# In[17]:


def gettime():
    return time.strftime("%H%M%S", time.localtime())


# In[18]:


# Turn everything the damn off!

def damnoff():
    GPIO.output(segs, False)
    GPIO.output(digs, False)
    GPIO.output(blink, False)


# In[ ]:


s = 0.0025

while True:
    timestr = gettime()
    for i in range(0,100):
        #time.sleep(s)
        for d in range(0,4):
            damnoff()
            GPIO.output(digs[d], True)
            GPIO.output(segs, num[int(timestr[d])])
            if int(timestr[5]) % 2 == 0:
                GPIO.output(blink, True)
            elif int(timestr[5]) % 2 == 1:
                GPIO.output(blink, False)
            time.sleep(s)


# In[ ]:




