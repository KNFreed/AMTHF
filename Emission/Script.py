#!/usr/bin/env python

from scipy import signal
from scipy.io.wavfile import read, write
import numpy as np
import matplotlib.pyplot as plt
import wave, argparse, sys, time

#IM GETTING TIRED OF THIS SHIT

#shit to transfer
chain = []

#shitty amplitudes for the ask
AH = 1
AB = 0.5

#samplingrate cunt
samplingrate = 22000

t = 0: 1/fs : 1

time = []
ASK_signal = []
Digital_signal = []

for ii = 1: 1: length(bit_stream) :

    ASK_signal = [ASK_signal(bit_stream(ii) == 0) * A1 * sin(2 * pi * f * t) + (bit_stream(ii) == 1) * A2 * sin(2 * pi * f * t)]

    Digital_signal = [Digital_signal(bit_stream(ii) == 0) * zeros(1, length(t)) + (bit_stream(ii) == 1) * ones(1, length(t))]
    time = [time,t]
    t = t + 1
