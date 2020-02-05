#!/usr/bin/env python

from scipy import signal
from scipy.io.wavfile import read
import wave
import configparser

config = configparser.ConfigParser()
config.read_file(open(r'config.txt'))

original = wave.open("test.wav", 'rb')
samplingrate = wave.Wave_read.getframerate(original)

lplus = int(samplingrate/2)

def filter():

    input_data = read("test.wav")
    audio = input_data[1]

    #vars
    echfreq = 10000
    nyqfreq = echfreq / 2
    filtertype = "lowpass"
    filterfreq = [2000]

    # Échantillonage    f = signal.resample(audio, echfreq)

    # Paramètres de filtrage
    if (filtertype == "bandstop") or (filtertype =="bandpass"):
        cutoff = [filterfreq[0]/nyqfreq, filterfreq[1]/nyqfreq]
        cutoffreq = filterfreq
    else:
        cutoff = filterfreq[0] / nyqfreq
        cutoffreq = filterfreq[0]
    #Filtrage
    b, a = signal.butter(6, cutoff, btype=filtertype)
    filteredaudio = signal.lfilter(b, a, f)
    return filteredaudio

def demodul():
    sign = filter()
    l = 0
    demod = []
    while (l < len(sign)):
        if sign[l] == 1 and sign[(l + lplus)] == 1:
            demod = demod + [1]
            l = l + int((1.5 * lplus))
        elif sign[l] == 0 and sign[l + lplus] == 0:
            demod = demod + [0]
            l = l + int((1.5 * lplus))
        elif sign[l] == 2 and sign[l + lplus] == 2:
            demod = demod + [2]
            l = l + int((1.5 * lplus))
        else:
            l = l + 1
    return sign

def bin2dec():
    bin = demodul()
    l=0
    dec = []
    while(l<len(bin)):
        temporary=[]
        while(bin[l]!=2):
            temporary = temporary + [bin[l]]
            l=l+1
        dec = dec + ["".join(map(str, temporary))]
        l=l+1
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