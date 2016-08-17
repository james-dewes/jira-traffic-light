import os

class sound():

        
    def play(self):
        os.system('mpg321 sound/sound.mp3 -q &')

