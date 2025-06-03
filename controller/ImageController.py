from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class ImageWindow(Screen):
    filepath = StringProperty("")
    filename = StringProperty("default")
