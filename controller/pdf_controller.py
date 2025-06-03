import cv2
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen


class PDFWindow(Screen):
    index = NumericProperty(0)
    page_path = StringProperty("")
    h = NumericProperty(900)
    file = None
    filename = StringProperty("Default")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def previous_page(self):
        self.file.prev_page()
        self.set_page()
        self.ids.scroll.scroll_y = 0
        self.index = self.file.current_page()

    def next(self):
        try:
            self.file.next_page()
            self.set_page()
            self.index = self.file.current_page()
        except Exception:
            pass

    def get_dim(self, path):
        img = cv2.imread(path)
        return img.shape[0] - 700

    def set_page(self):
        self.page_path = self.file.page_path()
        self.h = self.get_dim(self.page_path)
        self.ids.scroll.scroll_y = 1


