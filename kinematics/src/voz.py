
#!/usr/bin/env python
from __future__ import division
import time
import rospy
from playsound import playsound
from node_mssg.msg import ViewTemplate


def callback(data1):
	caso = data1.caso

	print(caso)

	if caso == 'Acerca de mi': #borrar poner solo letra
		playsound('Intro_Op2.mp3')	

	if caso == 'Despedida':
		playsound('Despedida_Op2.mp3')	

	if caso == 'Saludar':
		playsound('Saludo_Op2.mp3')	



    
    

def listener():
    rospy.init_node('voz', anonymous=True)
    rospy.Subscriber("comunicacion", ViewTemplate, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
