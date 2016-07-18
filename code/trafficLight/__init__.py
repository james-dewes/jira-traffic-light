'''
Keep track of the state of the light entity
'''
import light


class TrafficLight:
    def __init__(self):
        self.red = light()
        self.yellow = light()
        self.green = light()

    def change(self, colour):
        # type: (object) -> object colour =''):
        self[colour].state != self[colour].state
