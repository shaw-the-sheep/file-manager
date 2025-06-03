from datetime import time

from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.slider import MDSlider


class AudioFileWindow(Screen):
    sound = ObjectProperty(None)
    audio_length = NumericProperty(0)
    duration = StringProperty("loading...")
    current_time = StringProperty("00:00")
    current_time_in_seconds = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.sched = Clock.schedule_interval(self.get_current_time, 0.5)

    def set_time(self):
        self.audio_length = int(self.sound.length)
        print(self.audio_length)
        print("time set")

    def set_duration(self):
        self.duration = self.time_format(self.audio_length)

    def get_current_time(self, dt):
        if self.sound:
            self.current_time = self.time_format(self.sound.get_pos())
            self.current_time_in_seconds = self.get_current_time_in_seconds()

    def set_current_time(self, widget):
        self.current_time = widget.value

    def time_format(self, t):
        minutes = t // 60
        hours = 0
        if minutes >= 60:
            hours = minutes // 60
            minutes = minutes % 60
        seconds = t % 60
        return time(int(hours), int(minutes), int(seconds)).strftime("%H:%M:%S")

    def play(self):
        if self.sound.state != "play":
            self.sound.play()

    def stop(self):
        if self.sound.state == "play":
            self.sound.stop()

    def resume(self):
        if self.sound.state != "play":
            self.sound.seek(self.current_time_in_seconds)
            self.play()

    def jump_to(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.sound.seek(instance.value)

    def get_current_time_in_seconds(self):
        t = time().fromisoformat(self.current_time)
        h = t.hour
        m = t.minute
        s = t.second
        return s + m*60 + h*3600

    def change_volume(self, instance):
        self.sound.volume = instance.value