#!/usr/bin/env python

from scipy import signal
from scipy.io.wavfile import read, write
import numpy as np
import matplotlib.pyplot as plt
import wave, argparse, sys, time

original = wave.open("test.wav", 'rb')
samplingrate = wave.Wave_read.getframerate(original)

input_data = read("test.wav")
audio = input_data[1]

#vars
echfreq = 10000
nyqfreq = echfreq / 2
filtertype = "lowpass"
filterfreq = [2000]

# Échantillonage
f = signal.resample(audio, echfreq)
# Paramètres de filtrage
if (filtertype == "bandstop") or (filtertype =="bandpass"):
    cutoff = [filterfreq[0]/nyqfreq, filterfreq[1]/nyqfreq]
    cutoffreq = filterfreq
else:
    cutoff = filterfreq[0] / nyqfreq
    cutoffreq = filterfreq[0]
#Filtrage
b, a = signal.butter(5, cutoff, btype=filtertype)
filteredaudio = signal.lfilter(b, a, f)

Time = np.linspace(0, len(audio) / samplingrate, num=len(audio))
Time2 = np.linspace(0, len(f) / echfreq, num=len(f))
Time3 = np.linspace(0, len(filteredaudio) / echfreq, num=len(filteredaudio))


plt.plot(Time,audio, label='Original Audio')
plt.plot(Time2,f, label='Filtered Audio')
plt.plot(Time3,filteredaudio, label='Filtered Audio')
plt.title('Filtered & Unfiltered comparison', fontsize=14)
plt.xlabel('Time (Hz)')
plt.ylabel('Range')
plt.legend()
plt.show()



plt.figure()
plt.subplot(2,1,1)
plt.xlabel("Temps")
plt.ylabel("Position en fonction du temps")
plt.plot(w,EVLC_rect(Vitesse,1000,0.2,1.2,1.4,100,500,-500))
plt.plot(w,filsdepute(w,0.2,1.2,1.4,100,500,-500))
plt.show()
