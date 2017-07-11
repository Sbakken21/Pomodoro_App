import kivy
import time

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

class Widgets(Widget):



    def get_count(self):
        count = 1500
        self.minutes, self.seconds = divmod(count, 60)
        return ('%d:%02d' % (self.minutes, self.seconds))
        
    def countdown(self):        
        count = 1500
        self.minutes, self.seconds = divmod(count, 60)
        #print("%d:%02d" % (self.minutes, self.seconds)) <-- Shows the starting time 
        for self.minutes in range(self.minutes, -1, -1):
            print("%d:%02d" % (self.minutes, self.seconds))
        return('Work time is up')    
        # ^^^ above code prints minutes (counting down), need to update label w/ data

class PomodoroApp(App):

    def build(self):
        return Widgets()



class Timer(Widget):
    pass    

PomodoroApp().run()
