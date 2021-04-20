# Print out realtime audio volume as ascii bars

import sounddevice as sd
import numpy as np

def print_sound(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print(str(volume_norm) + "|" * int(volume_norm))

with sd.InputStream(callback=print_sound):
    sd.sleep(100000)