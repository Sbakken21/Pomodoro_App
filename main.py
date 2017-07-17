from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

class Timer(Widget):
    
    work_time, default = 10, 10
    break_time = 5
    long_break = 15
    sequence = ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'lb']
    cycle = 0
    pomo_count = 0
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

    def break_timer(self):
        self.pomo_count = 0
        self.cycle = 0
        self.timer_On = True
        if self.sequence != 'lb' or 'w':
            self.work_time = self.break_time
        else:
            self.work_time = self.long_break     # THIS NEEDS TO BE ADJUSTED, FOR W, B, AND LB (CURRENTLY SET UP ONLY FOR TESTING)
    
class PomoLayout(Widget):
    
    timer = Timer()
    displayLabel = ObjectProperty(None)
    cycleLabel = ObjectProperty(None)
    
    def check_cycle(self):
        self.cycleLabel.text = 'Completed Cycles: ' + str(self.timer.pomo_count)
        if self.timer.cycle < 3:
            self.timer.cycle += 1
        else:
            self.timer.cycle = 0
        self.setup()


    def setup(self):
        if self.timer.sequence[self.timer.cycle] == 'w':
            self.timer.work_time = self.timer.default
            self.timer.pomo_count += 1
            if self.timer.pomo_count == 5:
                self.timer.pomo_count = 0
                
        elif self.timer.sequence[self.timer.cycle] == 'b':
            self.timer.work_time = self.timer.break_time
        else:
            self.timer.work_time = self.timer.long_break
        self.btn_default()
        # self.cycle_display()
        

    def default_display(self):
        return str(self.timer.time_convert())

    def cycle_display(self):
        print('Count: ' + str(self.timer.pomo_count))
        return 'Completed cycles: ' + str(self.timer.pomo_count)

    def btn_default(self):
        self.main_btn.text = 'Start'
        self.main_btn.background_color = (0,1,0,1)


    def start_button(self):
        if self.timer.timer_On == True:
            self.btn_default()
            self.timer.stop_timer()
        else: 
            self.main_btn.text = 'Pause'
            self.main_btn.background_color = (1,1,0,1)
            self.timer.start_timer()
    
    def break_button(self):
        self.timer.break_timer()

    def reset_button(self):
        self.reset.disabled = True
        self.timer.reset_timer()
        self.displayLabel.text = self.default_display()
        self.btn_default()
 

    def update(self, *args, **kwargs):
        if self.timer.timer_On and self.timer.work_time > 0:
            self.reset.disabled = False
            self.timer.work_time -= 1
            print(self.timer.work_time)
            self.displayLabel.text = self.timer.time_convert()
        elif self.timer.work_time == 0:
            self.timer.timer_On = False
            self.displayLabel.text = 'Time is Up!!!' # change this for different cycle stuff
            self.check_cycle()
            


class PomoApp(App):
    def build(self):
        layout = PomoLayout()
        Clock.schedule_interval(layout.update, 1)
        return layout

PomoApp().run()
