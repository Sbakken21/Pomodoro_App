import kivy
import time

from kivy.app import App
from kivy.uix.widget import Widget

class Widgets(Widget):
    def get_count(self):
        count = 1500
        self.minutes, self.seconds = divmod(count, 60)
        return ('%d:%02d' % (self.minutes, self.seconds))

class PomodoroApp(App):
    def build(self):
        return Widgets()



class Timer(Widget):
    pass    

PomodoroApp().run()
