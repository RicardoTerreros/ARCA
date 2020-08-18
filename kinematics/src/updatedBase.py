#!/usr/bin/env python
import serial
import time
import math
import struct

import rospy
from node_mssg.msg import ViewTemplate

arduinoRight =serial.Serial('/dev/ttyUSB2',9600)
arduinoLeft  =serial.Serial('/dev/ttyUSB3',9600)

#arduinoRight.close()
#arduinoLeft.close()

#Control Variables

RADIO_WHEELS = 0.0625
RADIO_MOBILE = 0.14
real_rotacional_angle = 0.0
#Serial Comunication
def float2Bytes(float_src):
	byte_dest = bytearray(struct.pack('f', float_src))
	return  (byte_dest)

def writeNumber(arduino,floatNumber):
	bytes_Number = float2Bytes(floatNumber)
	arduino.write(bytes_Number)

def readNumber(arduino):
	try:
		input_bytes= arduino.readline().rstrip()
		data_src =float(input_bytes.decode('ASCII'))
		print("Dato Leido",data_src)
	except ValueError:
		data_src = 0.0
		print("Error al leer el dato")
		print(input_bytes)
	return data_src


#Kinematics functions
def inverseKinematic(CHOOSE_MOTOR,forwardVelocity,rotacionalVelocity):
	rightMotorVelocity = (forwardVelocity + RADIO_MOBILE*rotacionalVelocity)/RADIO_WHEELS
	leftMotorVelocity =  (forwardVelocity - RADIO_MOBILE*rotacionalVelocity)/RADIO_WHEELS
	if CHOOSE_MOTOR == "right":
		return rightMotorVelocity
	elif CHOOSE_MOTOR == "left":
		return leftMotorVelocity
	else:
		return 0


def forwardKinematic(CHOOSE_VELOCITY,rightMotorVelocity,leftMotorVelocity):
	forwardVelocity    = (rightMotorVelocity + leftMotorVelocity)*RADIO_WHEELS/(2.0)
	rotacionalVelocity = (rightMotorVelocity - leftMotorVelocity)*RADIO_WHEELS/(2*RADIO_MOBILE)
	if CHOOSE_VELOCITY == "forward":
		return forwardVelocity
	elif CHOOSE_VELOCITY == "rotacional":
	  	return rotacionalVelocity
	else:
	    return 0


#Control functions
def positionControl(KP,error):
	control_effort = KP*error
	return control_effort


def OrientationControl(desired_rotacional_angle):#,last_rotacional_angle):
    global arduinoRight
    global arduinoLeft	
    endProcess = False
    desired_orientation = desired_rotacional_angle
    real_rotacional_angle = 0.0

    desired_right_motor_velocity = 0.0
    desired_left_motor_velocity = 0.0

    real_right_motor_velocity = 0.0
    real_left_motor_velocity = 0.0

    orientation_control_effort = 0.0

    desired_forward_velocity = 0.0
    desired_rotation_velocity = 0.0

    KP_orientation = 0.5

    cur_time = 0.0
    last_time = 0.0

    last_time= float(time.time())

    #arduinoRight.open()
    #arduinoLeft.open()

    while endProcess == False:
        cur_time = float(time.time())
        delta_time =cur_time - last_time

        orientation_error = desired_orientation - real_rotacional_angle

        orientation_control_effort = positionControl(KP_orientation, orientation_error)

        desired_forward_velocity = 0.0
        desired_rotation_velocity = orientation_control_effort

        desired_right_motor_velocity = inverseKinematic("right",desired_forward_velocity,desired_rotation_velocity)
        desired_left_motor_velocity =  inverseKinematic("left",desired_forward_velocity,desired_rotation_velocity)

        writeNumber(arduinoRight,desired_right_motor_velocity)
        #time.sleep(1.5)
        writeNumber(arduinoLeft,desired_left_motor_velocity)

        

        real_right_motor_velocity = readNumber(arduinoRight)
        real_left_motor_velocity  = readNumber(arduinoLeft)

        real_rotacional_velocity = forwardKinematic("rotacional",real_right_motor_velocity,real_left_motor_velocity)
        real_rotacional_angle = real_rotacional_angle + real_rotacional_velocity*delta_time

        if  abs(orientation_error) < 0.01:
            endProcess = True

        print("real_rotacional_angle", real_rotacional_angle)
        last_time = cur_time
        print(endProcess)

    #arduinoRight.close()
    #arduinoLeft.close()		
    desired_right_motor_velocity = 0.0
    desired_left_motor_velocity = 0.0

    writeNumber(arduinoRight,desired_right_motor_velocity)
    writeNumber(arduinoLeft,desired_left_motor_velocity)
    return(-1)

def adelante():
	global arduinoRight
	global arduinoLeft


	#arduinoRight.open()
	#arduinoLeft.open()
	desired_right_motor_velocity = 5
	desired_left_motor_velocity = 5

	writeNumber(arduinoRight,desired_right_motor_velocity)
	writeNumber(arduinoLeft,desired_left_motor_velocity)

	time.sleep(3)

	desired_right_motor_velocity = 0
	desired_left_motor_velocity = 0

	writeNumber(arduinoRight,desired_right_motor_velocity)
	writeNumber(arduinoLeft,desired_left_motor_velocity)

	#arduinoRight.close()
	#arduinoLeft.close()		
	return(-1)

def atras():
	global arduinoRight
	global arduinoLeft

	#arduinoRight.open()
	#arduinoLeft.open()

	desired_right_motor_velocity = -5
	desired_left_motor_velocity = -5

	writeNumber(arduinoRight,desired_right_motor_velocity)
	writeNumber(arduinoLeft,desired_left_motor_velocity)

	time.sleep(3)

	desired_right_motor_velocity = 0
	desired_left_motor_velocity = 0

	writeNumber(arduinoRight,desired_right_motor_velocity)
	writeNumber(arduinoLeft,desired_left_motor_velocity)

	#arduinoRight.close()
	#arduinoLeft.close()	
	return(-1)

def parar():
    global arduinoRight
    global arduinoLeft

    #arduinoRight.open()
    #arduinoLeft.open()

    desired_right_motor_velocity = 0
    desired_left_motor_velocity = 0

    writeNumber(arduinoRight,desired_right_motor_velocity)
    writeNumber(arduinoLeft,desired_left_motor_velocity)

    #arduinoRight.close()
    #arduinoLeft.close()	

    return(-1)

secuencia = 0
angulo = 0.0
flag = 0
i = 0

def callback(data1):
	global secuencia
	global angulo
	global flag
	secuencia = data1.caso
	angulo = data1.ang
	flag = 1
	global i
	i+= 1
	print("callback arg: ", data1)
	#print(i)
	if secuencia == 1:	
		print("1")
		#time.sleep(1)
		OrientationControl(angulo)

	elif secuencia == 2:
		print("2")
		adelante()

	elif secuencia == 3:
		print("3")
		atras()

	else:
		print("secuencia",secuencia)
		print("angulo",angulo)
		parar()

	

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("comunicacion", ViewTemplate, callback)
	global secuencia
	global angulo
	global flag
	global arduinoRight
	global arduinoLeft

	#rate = rospy.Rate(0.5) # 10hz
	#while not rospy.is_shutdown(): 
		#try:
		#if flag:

			
			#time.sleep(2)
	#	if secuencia == 1:	
	#		print("1")
			#time.sleep(1)
	#		OrientationControl(angulo)

	#	elif secuencia == 2:
	#		print("2")

	#		adelante()

	#	elif secuencia == 3:
	#		print("3")
	#		atras()

	#	else:
	#		print("secuencia",secuencia)
	#		print("angulo",angulo)
	#		parar()
			#flag = 0

		# except KeyboardInterrupt:
		# 	arduinoRight.open()
		# 	arduinoLeft.open()
		# 	time.sleep(2)
		# 	parar()
		# 	arduinoRight.close()
		# 	arduinoLeft.close()


	#simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	listener()	

