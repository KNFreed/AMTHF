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

