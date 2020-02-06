#!/usr/bin/env python

from scipy import signal
from scipy.io.wavfile import read, write
import numpy as np
import wave
import configparser

config = configparser.ConfigParser()
config.read_file(open(r'config.txt'))

def filter():

    input_data = read("test2.wav")
    audio = input_data[1]

    #vars
    echfreq = 10000
    nyqfreq = echfreq / 2
    filtertype = "highpass"
    filterfreq = [2]

    # Échantillonage    f = signal.resample(audio, echfreq)

    # Paramètres de filtrage
    if (filtertype == "bandstop") or (filtertype =="bandpass"):
        cutoff = [filterfreq[0]/nyqfreq, filterfreq[1]/nyqfreq]
    else:
        cutoff = filterfreq[0] / nyqfreq
    #Filtrage
    b, a = signal.butter(6, cutoff, btype=filtertype)
    filteredaudio = signal.lfilter(b, a, audio)
    filsdepute = np.array(filteredaudio, dtype=np.float32)
    write("test3.wav", 44100, filsdepute)
    return filteredaudio

def demodul():
    sign = filter()
    l = 0
    lplus = 20*49
    demod = []

    while ((l + lplus) < len(sign)):
        if sign[l] == 1.0 and sign[(l + lplus)] == 1.0:
            demod = demod + [1]
            l = l + int((lplus+1))
        elif sign[l] == 0 and sign[l + lplus] == 0:
            demod = demod + [0]
            l = l + int((lplus+1))
        elif sign[l] == 2 and sign[l + lplus] == 2:
            demod = demod + [2]
            l = l + int((lplus+1))
        else:
            l = l + 1
    print(demod)
    return demod

def bin2dec():
    bin = demodul()
    d=0
    dec = []
    print(bin)
    while(d<len(bin)):
        temporary=[]
        while(d<len(bin) and bin[d]!=2):
            temporary = temporary + [bin[d]]
            d=d+1
        dec = dec + ["".join(map(str, temporary))]
        d=d+1
    l = 0
    while (l < len(dec)):
        dec[l] = int(dec[l], 2)
        l = l + 1
    return dec

def dec2text():
    evt = bin2dec()
    # Dicitonnaire
    dict_size = 255
    dictionary = {i: chr(i) for i in range(dict_size)}

    output = open("output.txt", "w")
    text=""
    for k in evt:
        if k in dictionary:
            entry = dictionary[k]
        else:
            raise ValueError("Error")
        text = text + entry
    output.write(text)
    output.close

dec2text()