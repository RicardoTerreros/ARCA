#!/usr/bin/env python
# license removed for brevity
import rospy
from node_mssg.msg import ViewTemplate
from std_msgs.msg import Int32
import numpy 
import serial
import RPi.GPIO as GPIO


slave = serial.Serial('/dev/ttyS0',9600)
pub = rospy.Publisher('comunicacion', ViewTemplate, queue_size=10)



def callback(data):
    datos=data.data
    enviar=str(datos)+'\n'
    slave.write(datos)

def listener():
    rospy.init_node('public', anonymous=True)
    #Defino el nodo de comunicacion
    rospy.Subscriber("termino", Int32, callback)
    #Iniciamos el nodo
    rate = rospy.Rate(0.1) # 10hz
    
    last_ang=0.0
    while not rospy.is_shutdown():
        if slave.in_waiting:
            try:
                data = slave.readline()
                data_list = data.split(',')
                caso = int(data_list[0])
                ang = float(data_list[1])
                print("COM:", caso, ang)
                last_ang = ang
                listener()
                
            except:
                caso = 0
                ang = last_ang
            
            x = ViewTemplate(caso=caso,ang=ang)
            pub.publish(x)
            rate.sleep() 
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass 	
