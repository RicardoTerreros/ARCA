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
servo_min = 130 # Min pulse length out of 4096
servo_max = 630  # Max pulse length out of 4096

pwm.set_pwm_freq(60)
# Helper function to make setting a servo pulse width simpler.
def angulo(channel,angulo):
    pulse=int((1.85*angulo)+130)
    pwm.set_pwm(channel, 0, pulse)

def estado_normal():
    angulo(2,135)
    angulo(5,135)
    time.sleep(0.1)
    angulo(4,152)
    angulo(1,135)
    time.sleep(0.1)
    angulo(0,55)
    angulo(3,235)
    time.sleep(1)

def estado_inicial_hola():
    angulo(2,135)
    angulo(5,135)
    time.sleep(0.1)
    angulo(4,152)
    angulo(1,135)
    time.sleep(0.1)
    angulo(0,55)
    angulo(3,235)
    time.sleep(0.1)
    angulo(5,200)
    time.sleep(1)


def hola():
    estado_inicial_hola()
    a=135
    for i in range (55,245,1):
        angulo(0,i)
        time.sleep(0.002)
    time.sleep(0.3)

    for i in range (135,181,1):
        angulo(1,i)
        time.sleep(0.002)
    time.sleep(0.3)

    for i in range (181,119,-1):
        angulo(1,i)
        time.sleep(0.002)
    time.sleep(0.3)

    for i in range (119,181,1):
        angulo(1,i)
        time.sleep(0.002)
    time.sleep(0.3)

    for i in range (181,119,-1):
        angulo(1,i)
        time.sleep(0.002)
    time.sleep(0.3)

    for i in range (135,181,1):
        angulo(2,i)
        time.sleep(0.002)
    time.sleep(0.3)

    for i in range (181,119,-1):
        angulo(2,i)
        time.sleep(0.002)
    time.sleep(0.3)

    for i in range (119,181,1):
        angulo(2,i)
        time.sleep(0.002)
    time.sleep(0.3)

    for i in range (181,119,-1):
        angulo(2,i)
        time.sleep(0.002)

    time.sleep(1) #corregir al final, solo es por cuestiones de prueba


def hold():
    estado_normal()
    a=225;
    for i in range (45,140,1):
        angulo(0,i)
        angulo(3,a)
        a-=1
        time.sleep(0.002)


#Tuning de angulos por si falta
    angulo(0,145)  
    time.sleep(0.002)  
    angulo(0,150)
    time.sleep(0.002)
    angulo(0,155)
    time.sleep(0.3)

    for i in range (135,186,1):
        angulo(4,i+13)
        angulo(1,i)
        time.sleep(0.002)        
    #angulo(4,189)
    
    time.sleep(10) #corregir al final, solo es por cuestiones de prueba


def levantar_brazo_izquierdo():
    estado_normal()
    for i in range (235,41,-1):
        angulo(3,i)
        time.sleep(0.002)
        
    time.sleep(1) #corregir al final, solo es por cuestiones de prueba
    
def levantar_brazos():
    estado_normal()

    a=55
    for i in range (235,41,-1):
        angulo(3,i)
        angulo(0,a)
        a+=1
        time.sleep(0.002)
        
    time.sleep(1) #corregir al final, solo es por cuestiones de prueba

def sorprendida():
    estado_normal()
    a=55
    for i in range (235,41,-1):
        angulo(3,i)
        angulo(0,a)
        a+=1
        time.sleep(0.002)

    time.sleep(0.05)
    angulo(4,170)
    angulo(1,160)

    for i in range (135,220,1):
        angulo(2,i+3)
        angulo(5,i+10)
        time.sleep(0.002)


        





def despertar():
    estado_normal()
    angulo(5,200)
    angulo(2,200)
    time.sleep(0.2)
    a=55
    s=1
    ang=200-s
    for i in range (235,41,-1):
        angulo(3,i)
        angulo(0,a)
        a+=1
        if i<=200:
            angulo(5,ang)
            angulo(2,ang)
            
            if(ang>135):
                s+=1
                ang1=200-s
                ang=ang1
            else:
                s=0
                ang2=135
                ang=ang2
            
        time.sleep(0.005)

        
    time.sleep(1) #corregir al final, solo es por cuestiones de prueba



def what():
    estado_normal()

    a=55
    for i in range (235,41,-1):
        angulo(3,i)
        angulo(0,a)
        a+=1
        time.sleep(0.002)


    for i in range (135,75,-1):
        angulo(4,i)
        angulo(1,i)
        time.sleep(0.002)


    for i in range (135,200,1):
        angulo(5,i)
        angulo(2,i)
        time.sleep(0.002)   
  


   
    time.sleep(1) #corregir al final, solo es por cuestiones de prueba
        
def callback(data1):
    accion=data1.caso
    #Defino el nodo de comunicacion
    pub2 = rospy.Publisher('termino', Int32, queue_size=10)
 

    if accion=='1':
        estado_normal()
        time.sleep(3)
        estado_normal()
        rospy.loginfo("normal")

    elif accion=='2':
        hola()
        time.sleep(3)
        estado_normal()
        rospy.loginfo("hola")
	
    elif accion=='3':
        time.sleep(4)
        despertar()
        time.sleep(1.5)
        estado_normal()
        rospy.loginfo("despertar")

    elif accion=='4':
        levantar_brazo_izquierdo()
	time.sleep(6)
        rospy.loginfo("planes open day")

    elif accion=='5':
        levantar_brazo_izquierdo()
	time.sleep(6)
        rospy.loginfo("acerca de mi")

    elif accion=='6':
        hold()
	time.sleep(10) #editar cantidad de segundos
        rospy.loginfo("hold")

    elif accion=='7':
        hola()
        time.sleep(3)
        estado_normal()
        rospy.loginfo("despedir")

    elif accion=='8':
        levantar_brazos()
        #sorprendida()
        time.sleep(20)
        rospy.loginfo("victoria")

    else:
        accion='0'
        estado_normal()
        rospy.loginfo("normal")

    accion='0'
    term = 1
    #PUBLICACION
    #rospy.loginfo(hello_str)
    pub2.publish(term)
    

#
def listener():
    rospy.init_node('brazos', anonymous=True)
    rospy.Subscriber("comunicacion", ViewTemplate, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

