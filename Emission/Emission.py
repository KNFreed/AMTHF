#!/usr/bin/env python

from scipy.io.wavfile import write
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
            #Sauvegarde de leurs contenu
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
        dictionary = {'ESCAPE': 0, 'ESCAP': 1, 'ESCA': 2, 'ESC': 3, 'ES': 4, 'XOR': 5, 'ECHEC': 6, 'ECHE': 7, 'ECH': 8, 'EC': 9, '\n': 10, 'NOR': 11, 'ETAGE': 12, 'ETAG': 13, 'ETA': 14, 'ET': 15, 'CLU': 16, 'SI': 17, 'DI': 18, 'KI': 19, 'WI': 20, 'SE': 21, 'TE': 22, 'DE': 23, 'NE': 24, 'PRE': 25, 'TRE': 26, 'LA': 27, 'PA': 28, 'SA': 29, 'KO': 30, 'VO': 31, ' ': 32, '!': 33, '"': 34, '#': 35, '$': 36, '%': 37, '&': 38, "'": 39, '(': 40, ')': 41, '*': 42, '+': 43, ',': 44, '-': 45, '.': 46, '/': 47, '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57, ':': 58, ';': 59, '<': 60, '=': 61, '>': 62, '?': 63, '@': 64, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, '[': 91, '\\': 92, ']': 93, '^': 94, '_': 95, '`': 96, 'UD': 97, 'AS': 98, 'ER': 99, 'OF': 100, 'UM': 101, 'PIR': 102, 'PLU': 103, 'BOR': 104, 'CRI': 105, 'CEL': 106, 'CLU': 107, 'GA': 108, 'GE': 109, 'GO': 110, 'GI': 111, 'GU': 112, 'GLI': 113, 'GIR': 114, 'GUR': 115, 'GOL': 116, 'GUE': 117, 'EAU': 118, 'ION': 119, 'PHO': 120, 'OUILLE': 121, 'OYA': 122, '{': 123, '|': 124, '}': 125, '~': 126, 'PO': 127, 'NO': 128, 'TO': 129, 'PRO': 130, 'TRO': 131, 'VU': 132, 'TU': 133, 'Œ': 134, 'MA': 135, 'MI': 136, 'MO': 137, 'MU': 138, 'RA': 139, 'RI': 140, 'RO': 141, 'RU': 142, 'FA': 143, 'FI': 144, 'FO': 145, 'FU': 146, 'SA': 147, 'SI': 148, 'SO': 149, 'SU': 150, 'LI': 151, 'LO': 152, 'LU': 153, 'PI': 154, 'PO': 155, 'PU': 156, 'COT': 157, 'GI': 158, 'PY': 159, 'NAS': 160, '¡': 161, '¢': 162, '£': 163, '¤': 164, '¥': 165, '¦': 166, '§': 167, '¨': 168, '©': 169, 'ª': 170, '«': 171, '¬': 172, '\xad': 173, '®': 174, '¯': 175, '°': 176, '±': 177, '²': 178, '³': 179, '´': 180, 'µ': 181, '¶': 182, '·': 183, '¸': 184, '¹': 185, 'º': 186, '»': 187, '¼': 188, '½': 189, '¾': 190, '¿': 191, 'QA': 192, 'QE': 193, 'QI': 194, 'QO': 195, 'QU': 196, 'WA': 197, 'WE': 198, 'WI': 199, 'WO': 200, 'WU': 201, 'XA': 202, 'XE': 203, 'XI': 204, 'XO': 205, 'XU': 206, 'ZA': 207, 'ZE': 208, 'ZI': 209, 'ZO': 210, 'ZU': 211, 'CA': 212, 'CE': 213, 'CI': 214, 'CO': 215, 'CU': 216, 'HA': 217, 'HE': 218, 'HI': 219, 'HO': 220, 'HU': 221, 'VOU': 222, 'BOU': 223, 'TOU': 224, 'MOU': 225, 'SOU': 226, 'ZOU': 227, 'POU': 228, 'LOU': 229, 'CHA': 230, 'CHI': 231, 'CHO': 232, 'CHU': 233, 'CHE': 234, 'KI': 235, 'KA': 236, 'CLE': 237, 'NO': 238, 'NOM': 239, 'NOMB': 240, 'NOMBR': 241, 'NOMBRE': 242, 'CLO': 243, 'GA': 244, 'GAU': 245, 'GAUC': 246, 'GAUCH': 247, 'GAUCHE': 248, 'LOR': 249, 'DR': 250, 'DRO': 251, 'DROI': 252, 'DROIT': 253, 'DROITE': 254}
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

def dectobin():
    #On appelle le résultat de la compression
    evt = compress()
    binary=[]
    #On convertit en binaire
    for j in range (0,len(evt)):
        binary = binary+[int(x) for x in list('{0:0b}'.format(evt[j]))]
        binary = binary+[2]
    return binary

def trame():
    # On appelle la donnée en binaire
    raw_data = dectobin()
    # Déclaration des variables de trame
    start = [0,0,0,0,0,0,0,0]
    end = [1,1,1,1,1,1,1,1]
    control = [0,0,0,1,1,0,0,1]
    temporary = []
    final=[]
    i=0

    while i<len(raw_data):
        #Je rajoute dans la liste temporaire la donnée tant que je ne suis pas arrivée à la ifn de celle-ci
        while raw_data[i]!=2:
            temporary.append(raw_data[i])
            i=i+1
        i=i+1
        #Si la donnée fait moint de 8 bits, je complète avec des 0 pour correspondre aux critères du protocole.
        while len(temporary)<8:
            temporary.insert(0,0)
        #Calcul du bit de parité
        if sum(temporary)%2==0:
            pair = [0]
        else :
            pair = [1]
        #Création de la trame
        final = final + start + control + temporary + pair + end
        temporary = []
    return final

def modul():
    # On appelle la trame précédemment crée
    chains = trame()
    # Paramètres de la modulation
    N = 1000
    tiv = 1/N
    t=0
    sign = []
    fc = 600
    # Modulation avec une fréquence entre 15 kHz et 20 kHz
    while(t<len(chains)):
        sign=sign+[chains[int(t)]*np.sin(2*np.pi*fc*t)]
        t = t+tiv
    # Enregistrement du fichier modulé dans un fichier *.wav
    sign = np.array(sign, dtype=np.float32)
    write("hidden message.wav", 44100, sign)
    return sign

modul()