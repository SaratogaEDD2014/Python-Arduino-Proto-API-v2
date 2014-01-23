import serial
import time

class Arduino(object):


    __OUTPUT_PINS = -1


    def __init__(self, port, baudrate=115200, units = 'in', limit = 100):
        self.serial = serial.Serial(port, baudrate)
        self.serial.write('99')
        self.units = units #whether we are using metric or English, important for calculating pitch
        self.position = 0 #the absolute linear position of the motor apparatus
        if(self.units == 'in'):
            #self.pitch = 50.8
            self.pitch = 10/127
        elif(self.units == 'mm'):
            self.pitch = 2
        else:
            print('invalid agruement for units, units must be set to "in" or "mm"')
            #self.pitch = 50.8
            self.pitch = 10/127
        self.limit = limit


    def __str__(self):
        return "Arduino is on port %s at %d baudrate" %(self.serial.port, self.serial.baudrate)


    def output(self, pinArray):
        self.__sendData(len(pinArray))


        if(isinstance(pinArray, list) or isinstance(pinArray, tuple)):
            self.__OUTPUT_PINS = pinArray
            for each_pin in pinArray:
                self.__sendData(each_pin)
        return True


    def setLow(self, pin):
        self.__sendData('0')
        self.__sendData(pin)
        return True


    def setHigh(self, pin):
        self.__sendData('1')
        self.__sendData(pin)
        return True


    def getState(self, pin):
        self.__sendData('2')
        self.__sendData(pin)
        return self.__formatPinState(self.__getData()[0])


    def analogWrite(self, pin, value):
        self.__sendData('3')
        self.__sendData(pin)
        self.__sendData(value)
        return True


    def analogRead(self, pin):
        self.__sendData('4')
        self.__sendData(pin)
        return self.__getData()


    def turnOff(self):
        for each_pin in self.__OUTPUT_PINS:
            self.setLow(each_pin)
        return True


    def __sendData(self, serial_data):
        while(self.__getData()[0] != "w"):
            pass
        self.serial.write(str(serial_data))


    def __getData(self):
        return self.serial.readline().rstrip('\n')


    def __formatPinState(self, pinValue):
        if pinValue == '1':
            return True
        else:
            return False

    def close(self):
        self.serial.close()
        return True

    def move(self, steps):

        self.__sendData('6')
        self.__sendData(str(steps))
        #self.position = self.position + steps
        print steps

    def relmove (self, distance):
        print distance
        for i in range (500):
            move (400)

    def absMove(self, newPosition):
        self.relMove(newPosition - self.position)
        self.position = newPosition

    def reset(self):
        self.position = 0


Skotty = Arduino("COM5")
for i in range(200):
    time.sleep(.005)
    Skotty.move(400)


