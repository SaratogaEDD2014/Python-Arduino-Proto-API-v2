from arduino import Arduino
import time
import serial

#b = Arduino('/dev/ttyUSB0')
b = Arduino('COM5')
pin = 3

#declare output pins as a list/tuple
#b.output([pin])
#b.output([2,3])


for x in range(200):
    #b.setHigh(pin)
    #time.sleep(1)
    #print b.getState(pin)
    #b.setLow(pin)
    #print b.getState(pin)
#time.sleep(1)
    b.step()
    #time.sleep(1)
#b.sendData('6')
#time.sleep(0.05)
#b.sendData('9')
#ser=serial.Serial('COM5', 9600)
#time.sleep(1)
#ser.write('6')
b.close()
