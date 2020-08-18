#!/usr/bin/env python
from __future__ import division
import time
import rospy
from node_mssg.msg import ViewTemplate
import smbus
import math

bus=smbus.SMBus(1)
address=0x04

def writeNumber(ADDRESS, value):
    try:
        if value=='N' or value=='U' or value=='D' or value=='L' or value=='R' or value=='-':
            VALUE=0
        else:
            VALUE=int(value)

        bus.write_byte(ADDRESS,VALUE)
        print ("Dato enviado",VALUE)
        return -1
    except IOError:
        print ("Error de envio")
        return -1
        


def callback(data1):
    accion=data1.caso
    #Defino el nodo de comunicacion
    writeNumber(address,accion)

    

def listener():
    rospy.init_node('cabeza', anonymous=True)
    rospy.Subscriber("comunicacion", ViewTemplate, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()


