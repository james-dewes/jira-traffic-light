'''
Keep track of the state of the light entity
'''
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Light:
    def __init__(self, pin, state=False):
        """


        :type state: boolean
        :type pin: int
        :type self: object
        """
        self.state = state
        self.pin = pin

        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        self.state = True
        GPIO.output(self.pin, self.state)

    def off(self):
        self.state = False
        GPIO.output(self.pin, self.state)

    def cleanup(self):
        GPIO.cleanup()

