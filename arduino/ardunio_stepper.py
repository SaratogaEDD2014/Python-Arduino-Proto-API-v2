from arduino import *

class ArduinoStepMotor(Arduino):
    def __init__(self, port, baudrate=115200, units = 'in'):
        super(ArduinoStepMotor, self).__init__(port, baudrate)
        self.units = units #whether we are using metric or English, important for calculating pitch
        if(self.units == 'in'):
            pitch = 50.8
        elif(self.units == 'mm'):
            pitch = 2
        else:
            print('invalid agruement for units, units must be set to "in" or "mm"')
            pitch = 50.8

    def relMove(self, distance):
        microSteps = 8 #number of microsteps in a step
        stepsPerRev = 200 #number of steps in a rotation
        numSteps = microSteps*stepPerRev*self.pitch*distance
        numSteps = round(numSteps,0)
        if(numsSteps<0):
            numSteps = numSteps*-1
            self.sendData(7)
        else:
            self.sendData(6)
        self.sendData(numSteps)

sKotty = ArduinoStepMotor(COM3)
sKotty.relMove (100)
