#!/usr/bin/python 

##############################################################################################
#                                   Q U A D I E
#   authors: Christian Hinostroza & Alexander Sanchez
#   Code designed for the Engineering Design 2 Project of Florida Atlantic University 
#   term: Winter 2015
#   Date: 3-27-2015
#############################################################################################
import time
import math
import threading
import logging
from PWM import pwmMain as pwm
from Libraries import FreeIMU as FreeIMU
from Libraries import controller as Controller
from PID import pid as pid
from PING import PingSensor as PING
import Queue
import socket

controller = Controller.Controller()
sensors = FreeIMU.FreeIMU()

yaw = 0.0
pitch = 0.0
roll = 0.0
b1 = 0
b2 = 0
b3 = 0
gy = 0
gp = 0
gr = 0
pn = 0
rn = 0
dn = 0
baro = 0

#############################################################################################
#                                                                                           #
#                                   Sensor reading                                          #
#                                                                                           #
#############################################################################################


def getSensorData():
    y,p,r = sensors.getYawPitchRoll()
    #print "y = %f p = %f r = %f"%(y,p,r)
    b1,b2,b3,gy,gp,gr,pn,rn,dn = sensors.getValues()
    baro = sensors.getBaroAlt()
    return
  
#############################################################################################
#                                                                                           #
#                                      Main Thread                                          #
#                                                                                           #
#############################################################################################

getSensorData()

