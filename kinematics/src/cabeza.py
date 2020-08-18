import smbus
import time
import math

bus=smbus.SMBus(1)
address=0x04

def writeNumber(ADDRESS, value):
    try:
        VALUE=int(value)
        bus.write_byte(ADDRESS,VALUE)
        print ("Dato enviado",VALUE)
        return -1
    except IOError:
        print ("Error de envio")
        return -1

try:
    while True:
        codigo=input("Ingrese valor:")
        writeNumber(address,codigo)


except KeyboardInterrupt:
    print ("Fin de programa")


