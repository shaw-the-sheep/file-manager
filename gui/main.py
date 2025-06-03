from threading import Thread

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import ScreenManager
from controller.file_explorer import FileExplorerWindow
from kivymd.app import MDApp
from controller.ImageController import ImageWindow
from controller.pdf_controller import PDFWindow
from controller.window_manager import MyWindow
from controller.video_controller import VideoWindow
from controller.audio_controller import AudioFileWindow
from models.motion.hand_tracking import HandTracking

class WindowManager(ScreenManager):
    pass

class MyHeader(MDBoxLayout):
    header_text = StringProperty("Default")
    file_name = StringProperty("Default")

class MediaApp(MDApp):
    def build(self):
        self.title = "Improved Media Controller"
        self.tracker = HandTracking()


        return Builder.load_file("media.kv")

    def button_animation(self, widget):
        manager = self.root.ids.manager
        manager.transition.direction = "right"
        manager.current = "explorer"

    def go_to_viewer(self, widget, name):
        manager = self.root.ids.manager
        manager.transition.direction = "left"
        manager.current = name

    def on_stop(self):
        self.tracker.stop()

if __name__ == "__main__":
    MediaApp().run()