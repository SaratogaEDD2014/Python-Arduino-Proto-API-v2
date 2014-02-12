from arduino import *
import time

class ArduinoStepMotor(Arduino):
    def __init__(self, port, baudrate=115200, units = 'in', limit = 12):
        super(ArduinoStepMotor, self).__init__(port, baudrate)
        self.units = units #whether we are using metric or English, important for calculating pitch
        self.position = 0 #the absolute linear position of the motor apparatus
        self.limit = limit #maximum distance motor is allowed to move

        if(self.units == 'in'):
            self.pitch = 50.8
        elif(self.units == 'mm'):
            self.pitch = 2
        else:
            print('invalid agruement for units, units must be set to "in" or "mm"')
            self.pitch = 50.8

    def relMove(self, distance):
        if(distance < self.limit): 
            self.sendData('6')
            self.sendData(str(distance))
        else:
            print("distance out of range")

    def absMove(self, newPosition):
        if (newPosition < 0):
            newPosition = 0
        if (newPosition > self.limit):
            newPosition = limit
        self.relMove(newPosition - self.position)
        self.position = newPosition

    def reset(self): # WARNING: THIS CAN INTERFERE WITH PROTCOLS WHICH PREVENT THE MOTOR FROM MOVING OUT OF RANGE
        self.position = 0

ar1 = ArduinoStepMotor('COM5')
for i in range(200):
    time.sleep(.005)
    ar1.relMove(400)

