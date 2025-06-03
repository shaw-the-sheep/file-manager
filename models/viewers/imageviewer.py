from pathlib import Path


class ImageViewer:
    @staticmethod
    def check_type(filepath):
        ext = Path(filepath).suffix.lower()
        if ext in [".jpg", ".png", "jpeg"]:
            return True
        return False

