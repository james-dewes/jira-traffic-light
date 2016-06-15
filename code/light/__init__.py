'''
Keep track of the state of the light entity
'''
state = 0
def getState():
    return state

def on():
    state = 1

def off():
    state = 0

