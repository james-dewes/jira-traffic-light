'''
Keep track of the state of the light entity
'''
class Light:
    def __init__(self, state=False):
        """


        :type state: boolean
        :type self: object
        """
        self.state = state

    def on(self):
        self.state = True

    def off(self):
        self.state = False

