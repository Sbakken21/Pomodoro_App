import kivy
import time #used to run program every second

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class PomoGridLayout(Gridlayout):
    pass

class Clock:
    #Converts the seconds into minutes:seconds format
    def convertSec(self):
        count = int(input('Enter the amount of time in seconds: '))
        self.minutes, self.seconds = divmod(count, 60)
        # print('%d:%02d' % (minutes,seconds))
        # return (minutes, seconds)

    #Countdown using minutes:seconds from convertSec function
    def countdown(self):
        #print("%d:%02d" % (self.minutes, self.seconds)) <-- Shows the starting time 
        for self.minutes in range(self.minutes, -1, -1):
            while self.seconds > 0:
                self.seconds -= 1
                print("%d:%02d" % (self.minutes, self.seconds), end='\r')
                time.sleep(1)
            self.seconds = 60
        print('Work time is up')
                

   
foo = Clock()
foo.convertSec()
foo.countdown()