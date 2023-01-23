from .post import Post
from .business import Analytics
from .files import MP3File


class Reel(Post, Analytics):
    video_file = None
    visual_effects = None

    def __init__(self, mp3_filename, description=None, active=True, **kwargs):
        super().__init__(description, **kwargs)
        self.music = MP3File(filename=mp3_filename)

    def add_effects(self):
        pass

    def add_music(self):
        pass

    def create(self):
        pass

    def read(self):
        pass

    def delete(self):
        pass
