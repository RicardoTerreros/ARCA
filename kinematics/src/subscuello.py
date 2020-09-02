#!/usr/bin/env python
from __future__ import division
import time
import rospy
from node_mssg.msg import ViewTemplate
from std_msgs.msg import Int32
accion='0'
# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 100 # Min pulse length out of 4096
servo_max = 690  # Max pulse length out of 4096

pwm.set_pwm_freq(60)
# Helper function to make setting a servo pulse width simpler.
def angulo(channel,angulo):
    pulse=int(( ((servo_max-servo_min)/180) *angulo) + servo_min)
    pwm.set_pwm(channel, 0, pulse)

def despierta_cuello():
    time.sleep(2)
    angulo(6,45)
    time.sleep(2)
    angulo(6,135)
    time.sleep(2)
    angulo(6,90)
    time.sleep(1)

def estado_normal_cuello():
		time.sleep(1)
		angulo(6,90)

def callback(data1):
    accion=data1.caso
    #Defino el nodo de comunicacion

    if accion=='1':
	estado_normal_cuello()
        time.sleep(3)
        rospy.loginfo("normal")
    elif accion=='2':
        estado_normal_cuello()
        time.sleep(3)
        rospy.loginfo("hola")
    elif accion=='3':
        despierta_cuello()
        rospy.loginfo("despertar")
    elif accion=='4':
        estado_normal_cuello()
        time.sleep(3)
        estado_normal()
        rospy.loginfo("planes open day")
    elif accion=='5':
        estado_normal_cuello()
        time.sleep(3)
        rospy.loginfo("acerca de mi")
    elif accion=='6':
        estado_normal_cuello()
	time.sleep(3)
        rospy.loginfo("hold")
    elif accion=='7':
        estado_normal_cuello()
	time.sleep(3)
        rospy.loginfo("despedida")
    elif accion=='8':
        estado_normal_cuello()
	time.sleep(3)
        rospy.loginfo("victoria")
    else:
        accion='0'
        estado_normal_cuello()
        rospy.loginfo("normal")
    accion='0'

    
    

#
def listener():
    rospy.init_node('cuello', anonymous=True)
    rospy.Subscriber("comunicacion", ViewTemplate, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

