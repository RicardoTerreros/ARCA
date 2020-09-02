#!/usr/bin/env python
import time
import rospy
import pygame
from node_mssg.msg import ViewTemplate


def callback(data1):
	caso = data1.caso
	pygame.mixer.init()
	print(caso)

	if caso == '5': #borrar poner solo letra
		pygame.mixer.music.load("Intro_Op2.mp3")
		#playsound('~/catkin_ws/src/ARCA/kinematics/src/Intro_Op2.mp3')	

	if caso == '7':
		pygame.mixer.music.load("Despedida_Op2.mp3")
		#playsound('~/catkin_ws/src/ARCA/kinematics/src Despedida_Op2.mp3')	

	if caso == '2':
		pygame.mixer.music.load("Saludo_Op2.mp3")
		#playsound('~/catkin_ws/src/ARCA/kinematics/src/Saludo_Op2.mp3')

	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
    
    

def listener():
    rospy.init_node('voz', anonymous=True)
    rospy.Subscriber("comunicacion", ViewTemplate, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
