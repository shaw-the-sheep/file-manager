from pathlib import Path

from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.videoplayer import VideoPlayer

from models.viewers.pdfviewer import PDFViewer
from models.viewers.videoviewer import VideoViewer, AudioViewer
from models.viewers.imageviewer import ImageViewer

class FileExplorerWindow(Screen):
    widget_name = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def choose_file(self, filechooser):
        selection = filechooser.selection
        if not selection:
            return
        selected_path = selection[0]
        if ImageViewer.check_type(selected_path):
            try:
                image_screen = self.manager.get_screen("image")
                image_screen.filepath = selected_path
                image_screen.filename = self.get_name(selected_path)
                fn = self.get_name(selected_path)
                if len(fn) < 21:
                    image_screen.filename = fn
                else:
                    image_screen.filename = "filename is too long"
                self.manager.current = "image"
                return
            except Exception as e:
                print(e)

        file = PDFViewer(selected_path)
        type_checked = file.check_type()
        if type_checked:
            try:
                pdf_screen = self.manager.get_screen("pdf")
                pdf_screen.file = file
                pdf_screen.filename = self.get_name(selected_path)
                pdf_screen.set_page()
                pdf_screen.ids.pdf_page.reload()
                self.manager.current = "pdf"
                return
            except Exception as e:
                print(e)
        file = VideoViewer(selected_path)
        type_checked = file.check_type()
        if type_checked:
            try:
                video_screen = self.manager.get_screen("video")
                video_screen.filepath = selected_path
                video_screen.state = "play"
                self.manager.current = "video"
                return
            except Exception as e:
                print(e)

        file = AudioViewer(selected_path)
        sound = SoundLoader.load(selected_path)
        try:
            if file.check_type():
                self.manager.current = "audio"
                audio_screen = self.manager.get_screen("audio")
                if sound:

                    audio_screen.sound = sound
                    audio_screen.set_time()
                    audio_screen.set_duration()
        except Exception as e:
            print(e)
        finally:
            sound.play()

    def get_name(self, path):
        return str(Path(path).stem)