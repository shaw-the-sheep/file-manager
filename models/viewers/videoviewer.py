from moviepy import VideoFileClip
from moviepy import AudioFileClip

class VideoViewer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.video = self.check_type()
        self.current_position = 0

    def check_type(self):
        try:
            video = VideoFileClip(self.filepath)
            return True
        except Exception:
            return False

    def duration(self):
        return self.video.duration

    def file_path(self):
        return self.filepath


class AudioViewer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.audio = self.check_type()

    def check_type(self):
        audio = AudioFileClip(self.filepath)
        return audio

    def duration(self):
        return self.audio.duration