#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from std_msgs.msg import Float32
import numpy 

def talker():
#Defino el nodo de comunicacion
    pub = rospy.Publisher('comunicacion', Float32, queue_size=10)
#Iniciamos el nodo
    rospy.init_node('base', anonymous=True)
    rate = rospy.Rate(0.1) # 10hz

    while not rospy.is_shutdown():
        #Publicacion 
        theta = 0.0
        theta = 3.141592
        #PUBLICACION
        #rospy.loginfo(hello_str)
        pub.publish(theta)
        rate.sleep()
   

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
