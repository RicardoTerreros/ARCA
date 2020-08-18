#!/usr/bin/env python
# license removed for brevity
import rospy
from node_mssg.msg import ViewTemplate
from std_msgs.msg import Int32
import numpy 
import serial
import RPi.GPIO as GPIO


slave = serial.Serial('/dev/ttyS0',9600)

datos=0


def talker():    
    rospy.init_node('public', anonymous=True)#Defino el nodo de comunicacion
    pub = rospy.Publisher('comunicacion', ViewTemplate, queue_size=10)
    #Iniciamos el nodo
    x = ViewTemplate()
    rate = rospy.Rate(10)
    
    last_ang=0.0
    while not rospy.is_shutdown():
        if slave.in_waiting:
            try:
                data = slave.readline()
                print(data)
                data_list = data.split(',')
                caso = int(data_list[0])
                ang = float(data_list[1])
                print("COM:", caso, ang)
                last_ang = ang
                
                
            except:
                caso = 0
                ang = last_ang
            
            x.caso=caso
            x.ang=ang
            pub.publish(x)
            
        rate.sleep() 


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass 	
