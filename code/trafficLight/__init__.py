"""
Keep track of the state of the light entity
"""
import light


class TrafficLight:
    colours = ["red", "yellow", "green"]

    def __init__(self):
        self.red = light.Light()
        self.yellow = light.Light()
        self.green = light.Light()

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