import kivy
import time

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class PomoGridLayout(GridLayout):
    pass

class PomodoroApp(App):
    def build(self):
        return PomoGridLayout()


class Timer(Widget):
    


PomodoroApp().run()
