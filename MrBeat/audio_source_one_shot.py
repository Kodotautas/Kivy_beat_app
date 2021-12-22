from array import array

from audio.sources.thread import ThreadSource

class AudioSourceOneShot(ThreadSource):
    def __init__(self, output_stream, *args, **kwargs):
        ThreadSource.__init__(self, output_stream, *args, **kwargs)
        self.chunk_nb_samples =32
        self.buf = array('h', b'\x00' * self.chunk_nb_samples)

    def get_bytes(self, *args, **kwargs):
        return self.buf.tostring()
