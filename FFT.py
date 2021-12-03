import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft,rfft
from glob import glob
import librosa as lr
from scipy.signal import butter, lfilter,freqz,filtfilt 

def butter_highpass(cutoff, sampling_rate, order):
    nyq = 0.5 * sampling_rate
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, sampling_rate, order):
    b, a = butter_highpass(cutoff, sampling_rate, order)
    y = lfilter(b, a, data)
    return y

#data_dir ='C:/Users/Lenovo/Desktop/Database-project/25-02-2020/sous'
#data_f ='C:/Users/Lenovo/Desktop/Database-project/25-02-2020/frequecry'
#data_t ='C:/Users/Lenovo/Desktop/Database-project/25-02-2020/time'
data_dir = 'C:/Users/Lenovo/Desktop/' 
data_pic = 'C:/Users/Lenovo/Desktop/'

audio_file = glob(data_dir + '/*.wav')

for file in range(0,len(audio_file),1):
# Time Domian
    # bring Sound have .wav Crate X-Axis Y-Axis
    audio, sfreq = lr.load(audio_file[file])
    #time = np.arange(0,len(audio))/(sfreq)
    fss = sfreq * 2
    print(fss)
    fig, ax = plt.subplots()
    ax.plot(time,audio)
    ax.set(xlabel='Time(s)',ylabel='Sound Amplitude')
    #fig.savefig(data_t + '/TimeDomain%s.png'%file)
    fig.savefig(data_pic + '/TimeDomain%s.png'%file)

# Frequency Domain  
    # Crate X-axis Frequency
    n = np.size(audio)
    fr = (fss/2)*np.linspace(0,1,round(n/2))/2
    yf =fft(audio)
    x_m = (2/n)* abs(yf[0:np.size(fr)])
    #high_filter
    cutoff = 3000 # Hz
    sampling_rate = 30000 #Hz # อัตราการสุ่ม 1Hz คือ สุ่ม 1 ใน 1วินาที ในทางเป็นจริงต้องสุ่ม 10 เท่า
    order = 2
    y = butter_highpass_filter(x_m, cutoff, sampling_rate, order)
    fig, ax = plt.subplots()
    ax.plot(fr,abs(y),linewidth=2)
    ax.set(xlabel='Frequency (Hz)',ylabel='Amplitube')
    plt.grid()
    #fig.savefig(data_f + '/FrequencyDomain%s.png'%file)
    fig.savefig(data_pic + '/FrequencyDomain%s.png'%file)
    
