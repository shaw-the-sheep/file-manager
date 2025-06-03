from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class VideoWindow(Screen):
    filepath = StringProperty("")
    state = StringProperty("play")
    filename = StringProperty("filename is too long")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def stop_video(self, widget):
        self.state = "stop"

    def play_video(self):
        self.state = "play"