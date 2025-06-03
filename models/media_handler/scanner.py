from pathlib import Path
from .file_storing_manager import StoreManager

class Scanner:
    def __init__(self):
        self.manager = StoreManager()

    def scan(self, root):
        for file_path in Path(root).rglob('*'):
            if file_path.is_file():
                self.manager.add_file(str(file_path))