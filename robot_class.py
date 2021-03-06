import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

MotorR1 = 2
MotorR2 = 3
MotorR3 = 4
MotorR4 = 17

MotorL1 = 27
MotorL2 = 22
MotorL3 = 10
MotorL4 = 9

GPIO.setup(MotorR1,GPIO.OUT) #GPIO 2  -> Motor rechts A
GPIO.setup(MotorR2,GPIO.OUT) #GPIO 3  -> Motor rechts B
GPIO.setup(MotorR3,GPIO.OUT) #GPIO 4  -> Motor rechts C
GPIO.setup(MotorR4,GPIO.OUT) #GPIO 17 -> Motor rechts D

GPIO.setup(MotorL1,GPIO.OUT) #GPIO 27 -> Motor Left A
GPIO.setup(MotorL2,GPIO.OUT) #GPIO 22 -> Motor Left B
GPIO.setup(MotorL3,GPIO.OUT) #GPIO 10 -> Motor Left C
GPIO.setup(MotorL4,GPIO.OUT) #GPIO 9  -> Motor Left D

class Robot:    # In de 'Robot' class staan de richtingen die de robot kan rijden.

    def rechtdoor(self):      # Deze def zorgt ervoor dat de robot vooruit rijdt.

        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)
        sleep(.0008)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,1)

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)
        sleep(.0008)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)
        sleep(.0008)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)
        sleep(.0008)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)
        sleep(.0008)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,1)
        sleep(.0008)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)
        sleep(.0008)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)
        sleep(.0008)

    def linksaf(self):          # Deze def zorgt ervoor dat de robot linksaf rijdt.

        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)

        sleep(.0008)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,1)

        sleep(.0008)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)

        sleep(.0008)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)

        sleep(.0008)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        sleep(.0008)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        sleep(.0008)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        sleep(.0008)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)

        sleep(.0008)

    def rechtsaf(self):        # Deze def zorgt ervoor dat de robot rechtsaf rijdt.

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)

        sleep(.0008)
        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)

        sleep(.0008)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)

        sleep(.0008)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)

        sleep(.0008)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)

        sleep(.0008)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,1)

        sleep(.0008)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)

        sleep(.0008)
        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)

        sleep(.0008)

    def scherplinks(self):    # Deze def zorgt ervoor dat de robot een scherpe bocht naar links maakt.

        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)
        sleep(.0008)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,1)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,1)
        sleep(.0008)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)
        sleep(.0008)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)
        sleep(.0008)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)
        sleep(.0008)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)
        sleep(.0008)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)
        sleep(.0008)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)
        sleep(.0008)

    def scherprechts(self):    # Deze def zorgt ervoor dat de robot een scherpe bocht naar rechts maakt.

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)

        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)
        sleep(.0008)
        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)

        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)
        sleep(.0008)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)

        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)
        sleep(.0008)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)

        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)
        sleep(.0008)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)

        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)
        sleep(.0008)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,1)

        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,1)
        sleep(.0008)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)

        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)
        sleep(.0008)
        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)

        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)
        sleep(.0008)
