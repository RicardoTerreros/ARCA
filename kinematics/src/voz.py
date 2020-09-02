
#!/usr/bin/env python
from __future__ import division
import time
import rospy
from playsound import playsound
from node_mssg.msg import ViewTemplate


def callback(data1):
	caso = data1.caso

	print(caso)

	if caso == '5': #borrar poner solo letra
		playsound('~/catkin_ws/src/ARCA/kinematics/src/Intro_Op2.mp3')	

	if caso == '7':
		playsound('~/catkin_ws/src/ARCA/kinematics/src/Despedida_Op2.mp3')	

	if caso == '2':
		playsound('~/catkin_ws/src/ARCA/kinematics/src/Saludo_Op2.mp3')



    
    

def listener():
    rospy.init_node('voz', anonymous=True)
    rospy.Subscriber("comunicacion", ViewTemplate, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
