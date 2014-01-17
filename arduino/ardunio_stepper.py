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

        microSteps = 8 #number of microsteps in a step
        stepsPerRev = 200 #number of steps in a rotation

        if (self.position + distance > self.limit):
            distance = self.limit - self.position
        if (self.position + distance < 0):
            distance = self.position* -1

        numSteps = microSteps*stepsPerRev*self.pitch*distance
        numSteps = round(numSteps,0)
        if(numSteps<0):
            numSteps = numSteps*-1
            self.sendData('7')
        else:
            self.sendData('6')
        self.sendData(str(numSteps))
        self.position = self.position + distance

    def absMove(self, newPosition):
        if (newPosition < 0):
            newPosition = 0
        if (newPosition > self.limit):
            newPosition = limit
        self.relMove(newPosition - self.position)
        self.position = newPosition

    def reset(self): # WARNING: THIS CAN INTERFERE WITH PROTCOLS WHICH PREVENT THE MOTOR FROM MOVING OUT OF RANGE
        self.position = 0

sKotty = ArduinoStepMotor('COM5')
for i in range(20):
    time.sleep(.1)
    sKotty.relMove(9)
sKotty.absMove (0)
