#!/usr/bin/env python

from scipy import signal
from scipy.io.wavfile import read, write
import numpy as np
import matplotlib.pyplot as plt
import wave, argparse, sys, time
import os

def fileparse():
    # Parse des fichiers locaux à compresser
    files = os.listdir(os.curdir)
    return files

def readfile(evt):
    texts = []
    t=0
    while (t < len(evt)):
        # Recherche des fichiers textes
        if evt[t].endswith(".txt"):
            f = open(evt[t], "r")
            #Sauvegarde de leur contenus
            texts.append(f.read())
            f.close()
            t=t+1
        else:
            t=t+1
    return texts

def compress():
    uncompressed = readfile(fileparse())
    compressed = []
    #Compression de chaque texte
    for b in range(0,len(uncompressed)):
        #Création du dictionnaire

        dict_size = 256
        dictionary = {chr(i): i for i in range(dict_size)}
        w = ""
        result = []
        for c in uncompressed[b]:
            wc = w + c
            if wc in dictionary:
                w = wc
            else:
                compressed.append(dictionary[w])
                # Add wc to the dictionary.
                dictionary[wc] = dict_size
                dict_size += 1
                w = c
        # Output the code for w.
        if w:
            compressed.append(dictionary[w])
    return compressed

def dectobin(evt):
    binary=[]
    for j in range (0,len(evt)):
        binary = binary+[int(x) for x in list('{0:0b}'.format(evt[j]))]
        binary = binary+[2]
    return binary
#shit to transfer
chains = dectobin(compress())

N = 1000
tiv = 1/N
t=0
r=0
signal = []



while(t<len(chains)):
    signal=signal+[chains[int(t)]*np.sin(2*np.pi*10*t)]
    t = t+tiv
    print(t)
print(signal)

figure, axe1 = plt.subplots()
axe1.set_xlabel("Temps (s)")
axe1.set_ylabel("Position en fonction du temps", color="red")
axe1.plot(signal, color="red")
axe1.tick_params(axis="y", labelcolor="red")
plt.show()