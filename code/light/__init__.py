'''
Keep track of the state of the light entity
'''
class Light:
    def __init__(self):
        self.state = 0

    def getState(self):
        return self.state

    def on(self):
        self.state = 1

    def off(self):
        self.state = 0

