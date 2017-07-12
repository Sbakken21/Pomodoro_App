from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty

class Timer:
    
    work_time = 1500
    break_time = 300
    display_time = ObjectProperty(None)
    timer_On = False


    # Function to start the timer
    def start_timer(self):
        Clock.schedule_interval(self.update, 1)
        self.timer_On = True

    # Function to stop the timer
    def stop_timer(self):
        self.timer_On = False
    
    def reset_timer(self):
        pass

    

    # Function to count the time remaining
    def time_remaining(self):
        pass
    
class PomoLayout(BoxLayout):

    displayLabel = ObjectProperty(None)
    
    def display_time(self):
        self.displayLabel.text='25555'

    def start_button(self):
        pass
    
    def stop_button(self):
        pass

    def reset_button(self):
        pass


class PomoApp(App):
    def build(self):
        return PomoLayout()

PomoApp().run()
