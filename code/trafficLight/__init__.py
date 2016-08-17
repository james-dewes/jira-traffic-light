"""
Keep track of the state of the light entity
"""
import light


class TrafficLight:
    colours = ["red", "yellow", "green"]

    def __init__(self, pins):
        self.red = light.Light(pins[0])
        self.yellow = light.Light(pins[1])
        self.green = light.Light(pins[2])

    def __getitem__(self, item):
        try:
            return self.__dict__[item]
        except KeyError:
            return False

    def change(self, colour):
        # type: (object, string):
        for c in self.colours:
            if c == colour:
                self[c].on()
            else:
                self[c].off()


    def cleanup(self):
        self.red.cleanup()
        self.yellow.cleanup()
        self.green.cleanup()
