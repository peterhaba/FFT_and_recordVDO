import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
from picamera import PiCamera
from time import sleep

def Record_sound(fs,seconds):
    camera.start_preview()
    print("Start Recording VDO and sound")
    myrecording = sd.rec(np.random.randn(int(seconds * fs))/10, samplerate=fs, channels=1,blocking = 'True')
    camera.start_recording('./VDO/myvdo%s.h264'%i)
    sleep(10)
    sd.wait()  # Wait until recording is finished
    camera.stop_recording()
    print("End Recording VDO and sound")
    camera.stop_preview()
    write("./sound/sounds%.2f.wav"%i ,fs,myrecording)
    return fs,seconds
    
fs = 44100  # Sample rate
seconds = 10 # Duration of recording

camera = PiCamera()
camera.rotation = 180
camera.resolution = (640,480)
camera.framerate = 24

for i in range(3):
    Record_sound(fs,seconds)