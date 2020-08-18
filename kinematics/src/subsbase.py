#!/usr/bin/env python
from __future__ import division
import time
import rospy
from node_mssg.msg import ViewTemplate
import smbus
import math
import RPi.GPIO as GPIO


motor1APin = 13						# PWM pin connected to LED
motor1BPin = 19
motor2APin = 16
motor2BPin = 18

duty = 100

GPIO.setwarnings(False)				#disable warnings
GPIO.setmode(GPIO.BCM)			#set pin numbering system
GPIO.setup(motor1APin,GPIO.OUT)
GPIO.setup(motor1BPin,GPIO.OUT)
GPIO.setup(motor2APin,GPIO.OUT)
GPIO.setup(motor2BPin,GPIO.OUT)

motor1A = GPIO.PWM(motor1APin,500)	#create PWM instance with frequency
motor1B = GPIO.PWM(motor1BPin,500)
motor2A = GPIO.PWM(motor2APin,500)		
motor2B = GPIO.PWM(motor2BPin,500)

motor1A.start(0)					#start PWM of required Duty Cycle 
motor1B.start(0)
motor2A.start(0)
motor2B.start(0)



def callback(data1):
	caso = data1.caso
	print(caso)
	if caso == 'D':
        	motor1A.ChangeDutyCycle(duty)
        	motor1B.ChangeDutyCycle(0)

		motor2A.ChangeDutyCycle(duty)
		motor2B.ChangeDutyCycle(0)

	if caso == 'L':
		motor1A.ChangeDutyCycle(0)
		motor1B.ChangeDutyCycle(duty)

		motor2A.ChangeDutyCycle(duty)
		motor2B.ChangeDutyCycle(0)

	if caso == 'R':
		motor1A.ChangeDutyCycle(duty)
		motor1B.ChangeDutyCycle(0)

		motor2A.ChangeDutyCycle(0)
		motor2B.ChangeDutyCycle(duty)

	if caso == 'U':
		motor1A.ChangeDutyCycle(0)
		motor1B.ChangeDutyCycle(duty)

		motor2A.ChangeDutyCycle(0)
		motor2B.ChangeDutyCycle(duty)


	if caso == '-' or caso == 'N':
		motor1A.ChangeDutyCycle(0)
		motor1B.ChangeDutyCycle(0)

		motor2A.ChangeDutyCycle(0)
		motor2B.ChangeDutyCycle(0)

    
    

def listener():
    rospy.init_node('base', anonymous=True)
    rospy.Subscriber("comunicacion", ViewTemplate, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
