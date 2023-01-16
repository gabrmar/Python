from .exceptions import InvalidAudioFile


class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise InvalidAudioFile(
                f"Invalid audio file format. Expecting a {self.ext} file"
            )
        self.filename = filename


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))
