from audiostream import get_output

class AudioEngine:

    NB_CHANNERS = 1
    SAMPLE_RATE = 44100
    BUFFER_SIZE = 1024
    def __init__(self):
        self.output_stream = get_output(channels = self.NB_CHANNELS,
                            rate=self.SAMPLE_RATE, buffersize=self.BUFFER_SIZE)
