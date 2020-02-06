#!/usr/bin/env python

from scipy import signal
from scipy.io.wavfile import read, write
import numpy as np
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
        dict_size = 255
        dictionary = {chr(i): i for i in range(dict_size)}
        w = ""
        for c in uncompressed[b]:
            wc = w + c
            if wc in dictionary:
                w = wc
            else:
                compressed.append(dictionary[w])
                w=c
        # Résultat
        if w:
            compressed.append(dictionary[w])
    return compressed

def dectobin(evt):
    binary=[]
    for j in range (0,len(evt)):
        binary = binary+[int(x) for x in list('{0:0b}'.format(evt[j]))]
        binary = binary+[2]
    return binary

def modul():
    chains = dectobin(compress())
    N = 1000
    tiv = 1/N
    t=0
    r=0
    sign = []
    fc = 150
    print(chains)
    while(t<len(chains)):
        sign=sign+[chains[int(t)]*np.sin(2*np.pi*fc*t)]
        t = t+tiv
    sign = np.array(sign, dtype=np.float32)
    write("test2.wav", 44100, sign)
    return sign
modul()