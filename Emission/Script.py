#!/usr/bin/env python

from scipy import signal
from scipy.io.wavfile import read, write
import numpy as np
import matplotlib.pyplot as plt
import wave, argparse, sys, time

#IM GETTING TIRED OF THIS SHIT

#shit to transfer
chain = [0,1,0,1]

#shitty amplitudes for the ask
AH = 1
AB = 0.5

#samplingrate cunt
samplingrate = 22000

N = 44100
tiv = 1/N
t=0
r=0
signal = []
print(len(chain))

while(t<len(chain)):
    signal=signal+[chain[int(t)]*np.sin(2*np.pi*21000*t)]
    t = t+tiv
    print(t)
print(signal)

figure, axe1 = plt.subplots()
axe1.set_xlabel("Temps (s)")
axe1.set_ylabel("Position en fonction du temps", color="red")
axe1.plot(signal, color="red")
axe1.tick_params(axis="y", labelcolor="red")
plt.show()