
#filename, displayname
import wave
from array import array


class Sound:
    nb_samples = 0
    samples = None

    def __init__(self, filename, displayname):
        self.filename = filename
        self.displayname = displayname
        self.load_sound()

    def load_sound(self):
        wav_file = wave.open(self.filename, 'rb')
        self.nb_samples = wav_file.getnframes()
        frames = wav_file.readframes(self.nb_samples) #bytes (8 bits)
        self.samples = array('h', frames) # 16 bits

class SoundKit:
    sounds = ()
    def get_nb_tracks(self):
        return len(self.sounds)

class SoundKit1(SoundKit):
    sounds = (Sound('sounds/kit1/kick.wav', 'KICK'),
              Sound('sounds/kit1/clap.wav', 'CLAP'),
              Sound('sounds/kit1/shaker.wav', 'SHAKER'),
              Sound('sounds/kit1/snare.wav', 'SNARE'),)

class SoundKitService:
    soundkit = SoundKit1()

    def get_nb_tracks(self):
        return self.soundkit.get_nb_tracks()

    def get_sound_at(self, index):
        if index >= len(self.soundkit.sounds):
            return None
        return self.soundkit.sounds[index]