
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from glob import glob
import librosa as lr
from scipy.signal import butter, lfilter,freqz,filtfilt 
import matplotlib as mpl

def butter_highpass(cutoff, sampling_rate, order):
    nyq = 0.5 * sampling_rate
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, sampling_rate, order):
    b, a = butter_highpass(cutoff, sampling_rate, order)
    y = lfilter(b, a, data)
    return y
fp = mpl.font_manager.FontProperties(family='Tahoma',size=13)
data_sound1 = 'C:/Users/Lenovo/Desktop/ซ่อน&ไม่ซ่อน/ซ่อน/' 
data_sound2 = 'C:/Users/Lenovo/Desktop/ซ่อน&ไม่ซ่อน/ไม่ซ่อน/' 
data_pic = 'C:/Users/Lenovo/Desktop/'

audio_file = glob(data_sound1 + '/*.wav')
audio_file2 = glob(data_sound2 + '/*.wav')
 
audio, sfreq = lr.load(audio_file[0])
audio2, sfreq = lr.load(audio_file2[0])

fss = sfreq * 2

n = np.size(audio)
n2 = np.size(audio2)

fr = (fss/2)*np.linspace(0,1,round(n/2))/2
fr2 = (fss/2)*np.linspace(0,1,round(n2/2))/2

yf =fft(audio)
yf2 =fft(audio2)

x_m = (2/n)* abs(yf[0:np.size(fr)])
x_m2 = (2/n2)* abs(yf2[0:np.size(fr2)])
    #high_filter
cutoff = 3000 # Hz
sampling_rate = 30000 #Hz # อัตราการสุ่ม 1Hz คือ สุ่ม 1 ใน 1วินาที ในทางเป็นจริงต้องสุ่ม 10 เท่า
order = 2

y = butter_highpass_filter(x_m, cutoff, sampling_rate, order)
y2 = butter_highpass_filter(x_m2, cutoff, sampling_rate, order)

fig, ax = plt.subplots()
ax.plot(fr,abs(y),linewidth=2,label=u'มีที่ซ่อน')
ax.plot(fr2,abs(y2),linewidth=2,label=u'ไม่มีที่ซ่อน')
ax.set(xlabel='Frequency (Hz)',ylabel='Amplitube')
ax.legend(prop=fp,loc=7,fancybox=1)
plt.grid()
fig.savefig(data_pic + '/FrequencyDomain%s.png')
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
fp = mpl.font_manager.FontProperties(family='Tahoma',size=13)
x = range(1970,2011,5)
take = [35017,36273,36895,36286,34771,33451,31935,30657,28655]
ono = [183325,185503,180901,177532,166930,159890,155200,150225,145217]
fuku = [355264,405677,425675,441502,445403,453791,456908,459087,459087]
ax = plt.gca()
ax.set(xlabel = u'Year', ylabel = u'Population')
ax.plot(x,take,label=u'ทาเกฮาระ')
ax.plot(x,ono,label=u'โอโนมิจิ')
ax.plot(x,fuku,label=u'ฟุกุยามะ')
ax.legend(prop=fp,loc=7,fancybox=1)
plt.grid()
plt.show()
"""