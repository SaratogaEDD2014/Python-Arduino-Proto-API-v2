from arduino import Arduino
import time

#b = Arduino('/dev/ttyUSB0')
b = Arduino('COM4')
pin = 3

#declare output pins as a list/tuple
b.output([pin])
#b.output([2,3])


for x in range(1000):
    #b.setHigh(pin)
    #time.sleep(1)
    #print b.getState(pin)
    #b.setLow(pin)
    #print b.getState(pin)
    #time.sleep(1)
    b.step()
    #time.sleep(1)

b.close()

