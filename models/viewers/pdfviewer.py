import tempfile
from pathlib import Path

import fitz

class PDFViewer:
    tmp = str(Path(tempfile.gettempdir())) + "\\tmp\\"
    def __init__(self, filepath):
        self.filepath = filepath
        self.doc = None
        self.index = 0

    def check_type(self):
        ext = Path(self.filepath).suffix.lower()
        if not (ext == ".pdf"):
            return False
        self.doc = fitz.open(self.filepath)
        return True

    def page_path(self):
        page = self.doc.load_page(self.index)
        pix = page.get_pixmap(dpi=150)
        path = str(self.tmp + f"page_{self.index}.png")
        pix.save(path)
        return path

    def next_page(self):
        if self.index < self.doc.page_count:
            self.index += 1

    def prev_page(self):
        if self.index > 0:
            self.index -= 1

    def current_page(self):
        return self.index
