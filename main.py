from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.listview import ListItemButton
from kivy.config import Config

# Settings for window display
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', '0')
Config.write()

class Timer(Widget):
    work_time, default = 1500, 1500
    break_time = 300
    long_break = 900
    sequence = ['Work', 'Break', 'Work', 'Break', 'Work', 'Break', 'Work', 'Long Break']
    cycle = 0
    pomo_count = 1
    timer_On = False
    timer_alarm = SoundLoader.load('Resources/screamingsun.mp3')

    def __init__(self, **kwargs):
        super(Timer, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)

    #Function to convert time into minutes and seconds
    def time_convert(self):
        self.minutes, self.seconds = divmod(self.work_time, 60)
        return str("%d:%02d" %(self.minutes, self.seconds))

    #Function to start timer
    def start_timer(self):
        self.timer_On = True

    #Function to stop timer
    def stop_timer(self):
        self.timer_On = False

    # Restore timer to default settings
    def reset_timer(self):
        self.cycle = 0
        self.pomo_count = 1
        self.timer_On = False
        self.work_time = self.default

    # Checks for number of completed cycles
    def check_cycle(self):
        if self.cycle < 7:
            self.cycle += 1
        else:
            self.cycle = 0
        self.setup()

    # Determines if the "Status" of the timer is work/break/long break
    def setup(self):
        self.timer_alarm.play()
        self.statusLabel.text = str('Status: ' + self.sequence[self.cycle])
        if self.sequence[self.cycle] == 'Work':
            self.work_time = self.default
            self.pomo_count += 1
            if self.pomo_count == 4:
                self.pomo_count = 0
        elif self.sequence[self.cycle] == 'Break':
            self.cycleLabel.text = 'Completed Cycles: ' + str(self.pomo_count) + '/4'
            self.work_time = self.break_time
        else:
            self.cycleLabel.text = 'Completed Cycles: ' + str(self.pomo_count) + '/4'
            self.work_time = self.long_break
        if self.timer_On is False:
            self.btn_default()
        else:
            self.pause_default()

    # Default style of the Pause Button
    def pause_default(self):
        self.main_btn.background_normal = './Resources/test_pause.png'
        self.main_btn.background_down = './Resources/test_pause.png'


    # Default style of Start Button
    def btn_default(self):
        self.main_btn.background_normal = './Resources/test.png'
        self.main_btn.background_down = './Resources/test.png'

    # Start/Pause Button
    def start_button(self):
        if self.timer_On:
            self.btn_default()
            self.stop_timer()
        else:
            self.pause_default()
            self.start_timer()

    # Button to skip to next cycle
    def break_button(self):
        self.timer_On = True
        self.check_cycle()

    # Button to reset all timer values back to default
    def reset_button(self):
        self.reset.disabled = True
        self.reset_timer()
        self.displayLabel.text = str(self.time_convert())
        self.cycleLabel.text = "Completed Cycles: 0/4"
        self.statusLabel.text = "Status: Work"
        self.btn_default()

    def update(self, *args, **kwargs):
        if self.timer_On and self.work_time > 0:
            self.reset.disabled = False
            self.work_time -= 1
            self.displayLabel.text = self.time_convert()
        elif self.work_time == 0:
            self.timer_On = False
            self.displayLabel.text = "Time is Up!!!"
            self.displayLabel.font_size = "50"
            self.check_cycle()

class TaskButton(ListItemButton):
    pass

class TaskLayout(BoxLayout):
    task_input = ObjectProperty()
    task_list = ObjectProperty()

    def add_task(self):
        if self.task_input.text != "":
            self.task_list.adapter.data.extend([self.task_input.text])
            self.task_list._trigger_reset_populate()
        else:
            pass

    def del_task(self):
        if self.task_list.adapter.selection:
            selection = self.task_list.adapter.selection[0].text
            self.task_list.adapter.data.remove(selection)
            self.task_list._trigger_reset_populate()

class TimerScreen(Screen):
    pass

class TaskScreen(Screen):
    pass

class Manager(ScreenManager):
    pass

class PomoApp(App):
    pass

if __name__ == '__main__':
    PomoApp().run()
