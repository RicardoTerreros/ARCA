#!/usr/bin/env python
# license removed for brevity
import rospy
from node_mssg.msg import ViewTemplate
import numpy 
import serial
import time


#Defino el puerto de slave
slave = serial.Serial('/dev/rfcomm0',9600)

#DEfino variables
pi = 3.141592


def talker():
    #Defino el nodo de comunicacion
    pub = rospy.Publisher('comunicacion', ViewTemplate, queue_size=10)
    #Iniciamos el nodo
    rospy.init_node('brazos', anonymous=True)
    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():
        #Publicacion
        dato = ViewTemplate()
        dato.caso=str(slave.read(1))
        dato.ang=pi
        #PUBLICACION
        #rospy.loginfo(hello_str)
        pub.publish(dato)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
