from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

class Timer(Widget):
    
    work_time = 300
    default = 300
    break_time = 300
    timer_On = False

    # Function to convert time into minutes and seconds
    def time_convert(self):
        self.minutes, self.seconds = divmod(self.work_time, 60)
        return ("%d:%02d" % (self.minutes, self.seconds))

    # Function to start the timer
    def start_timer(self):
        self.timer_On = True
        print('Timer is currently running') #REMOVE THIS LINE WHEN DONE TESTING

    # Function to stop the timer
    def stop_timer(self):
        self.timer_On = False
        
    # this should go back to the 'default' display
    def reset_timer(self):
        self.timer_On = False
        self.work_time = self.default 
    
class PomoLayout(Widget):
    
    timer = Timer()
    displayLabel = ObjectProperty(None)

    def default_display(self):
        return str(self.timer.time_convert())


    def start_button(self):
        self.timer.start_timer()
    
    def stop_button(self):
        self.timer.stop_timer()

    def reset_button(self):
        self.timer.reset_timer()
        self.displayLabel.text = self.default_display()

    def update(self, *args, **kwargs):
        if self.timer.timer_On and self.timer.work_time > 0:
            self.timer.work_time -= 1
            self.displayLabel.text = self.timer.time_convert()
        elif self.timer.work_time == 0:
            self.timer.timer_On = False
            self.displayLabel.text = 'Time is Up!!!'


class PomoApp(App):
    def build(self):
        layout = PomoLayout()
        Clock.schedule_interval(layout.update, 1)
        return layout

PomoApp().run()
