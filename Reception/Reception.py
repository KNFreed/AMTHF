#!/usr/bin/env python

from scipy import signal
from scipy.io.wavfile import read
import numpy as np
import configparser

# Déclaration fichier config
config = configparser.ConfigParser()
config.read_file(open(r'config.txt'))

def filter():
    # Imports des données via le fichier config
    input_data = read(config.get('Config','file'))
    audio = input_data[1]
    #vars
    echfreq = int(config.get('Config','echfreq'))
    nyqfreq = echfreq / 2
    filtertype = config.get('Config','filtertype')
    filterfreq = [int(config.get('Config','filterfreq'))] + [int(config.get('Config','2ndfilterfreq'))]

    # Paramètres de filtrage
    if (filtertype == "bandstop") or (filtertype =="bandpass"):
        cutoff = [filterfreq[0]/nyqfreq, filterfreq[1]/nyqfreq]
    else:
        cutoff = filterfreq[0] / nyqfreq
    #Filtrage via butterworth
    b, a = signal.butter(2, cutoff, btype=filtertype)
    filteredaudio = signal.lfilter(b, a, audio)
    filteredarray = np.array(filteredaudio, dtype=np.float32)

    return filteredarray

def demodul():
    # Appel du signal filtré
    sign = filter()
    #Définition de variabmes
    l = 0
    lplus = 20*49
    demod = []
    d=0
    # Tant que la longueur maximale du signal n'est pas dépassée
    while ((l + lplus) < len(sign)):
        # Si un signal haut se répète 49 fois à 20 ms de distance, le traduire par un 1
        if 0.7 < round(sign[l], 2) < 0.9 and 0.7 < round(sign[(l + lplus)], 2) < 0.9:
            d=int(d/lplus)
            # Même démarche pour les signaux bas et les 0
            for k in range(0,d):
                demod = demod+[0]
            demod = demod + [1]
            l = l + int((lplus + 1))
            d=0
        # Compteur de périodes à 0
        elif sign[l] < 0.1 :
            d=d+1
            l=l+1
        else:
            l = l + 1
    return demod

def bin2dec():
    # Appel du signal démodulé
    bin = demodul()
    d=0
    dec = []

    while(d<len(bin)):
        temporary=[]
        temporarycontrol = []
        firstcontrol = 0
        #vérification début de trame
        if sum(bin[d:d+8])==0:
            #Calcul du nombre de bits écoulé
            d=d+8
            for d in range (d,d+8):
                # Storage de la valeur en binaire du nombre de bits de la trame
                temporarycontrol = temporarycontrol +[bin[d]]
                d=d+1
            # Variable comptant les bits "passés"
            firstcontrol = 8
            for d in range (d,d+8):
                #Storage de la donnée
                temporary = temporary +[bin[d]]
                d=d+1
            firstcontrol = firstcontrol + 8
            if sum(temporary) % 2 == bin[d]:
                #Vérification du bit de parité
                firstcontrol = firstcontrol + 1
                d=d+1
                if sum(bin[d:d + 8]) == 8:
                    #Vérification fin de trame
                    firstcontrol = firstcontrol + 8
                    # Jointure de tous les éléments de la liste en un élément
                    temporarycontroldec = ["".join(map(str, temporarycontrol))]
                    # Conversion de cet élément en décimal
                    temporarycontroldec[0] = int(temporarycontroldec[0], 2)
                    #Vérification nombre de bits total trame
                    if firstcontrol == temporarycontroldec[0]:
                        #Jointure de tous les éléments de la liste en un élément
                        dec = dec + ["".join(map(str, temporary))]
                        d = d + 1
                    else:
                        d=d+1
                        error = open("Error total.txt", "w")
                        error.close()
                else:
                    d=d+1
            else:
                d=d+1
                error = open("Error parite.txt", "w")
                error.close()
        else:
            d=d+1
    l = 0
    while (l < len(dec)):
        #Conversion de cet élément en décimal
        dec[l] = int(dec[l], 2)
        l = l + 1
    return dec

def dec2text():
    evt = bin2dec()
    # Dicitonnaire
    dictionary = {0: 'ESCAPE', 1: 'ESCAP', 2: 'ESCA', 3: 'ESC', 4: 'ES', 5: 'XOR', 6: 'ECHEC', 7: 'ECHE', 8: 'ECH', 9: 'EC', 10: '\n', 11: 'NOR', 12: 'ETAGE', 13: 'ETAG', 14: 'ETA', 15: 'ET', 107: 'CLU', 148: 'SI', 18: 'DI', 235: 'KI', 199: 'WI', 21: 'SE', 22: 'TE', 23: 'DE', 24: 'NE', 25: 'PRE', 26: 'TRE', 27: 'LA', 28: 'PA', 147: 'SA', 30: 'KO', 31: 'VO', 32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'", 40: '(', 41: ')', 42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/', 48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@', 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z', 91: '[', 92: '\\', 93: ']', 94: '^', 95: '_', 96: '`', 97: 'UD', 98: 'AS', 99: 'ER', 100: 'OF', 101: 'UM', 102: 'PIR', 103: 'PLU', 104: 'BOR', 105: 'CRI', 106: 'CEL', 244: 'GA', 109: 'GE', 110: 'GO', 158: 'GI', 112: 'GU', 113: 'GLI', 114: 'GIR', 115: 'GUR', 116: 'GOL', 117: 'GUE', 118: 'EAU', 119: 'ION', 120: 'PHO', 121: 'OUILLE', 122: 'OYA', 123: '{', 124: '|', 125: '}', 126: '~', 155: 'PO', 238: 'NO', 129: 'TO', 130: 'PRO', 131: 'TRO', 132: 'VU', 133: 'TU', 134: 'Œ', 135: 'MA', 136: 'MI', 137: 'MO', 138: 'MU', 139: 'RA', 140: 'RI', 141: 'RO', 142: 'RU', 143: 'FA', 144: 'FI', 145: 'FO', 146: 'FU', 149: 'SO', 150: 'SU', 151: 'LI', 152: 'LO', 153: 'LU', 154: 'PI', 156: 'PU', 157: 'COT', 159: 'PY', 160: 'NAS', 161: '¡', 162: '¢', 163: '£', 164: '¤', 165: '¥', 166: '¦', 167: '§', 168: '¨', 169: '©', 170: 'ª', 171: '«', 172: '¬', 173: '\xad', 174: '®', 175: '¯', 176: '°', 177: '±', 178: '²', 179: '³', 180: '´', 181: 'µ', 182: '¶', 183: '·', 184: '¸', 185: '¹', 186: 'º', 187: '»', 188: '¼', 189: '½', 190: '¾', 191: '¿', 192: 'QA', 193: 'QE', 194: 'QI', 195: 'QO', 196: 'QU', 197: 'WA', 198: 'WE', 200: 'WO', 201: 'WU', 202: 'XA', 203: 'XE', 204: 'XI', 205: 'XO', 206: 'XU', 207: 'ZA', 208: 'ZE', 209: 'ZI', 210: 'ZO', 211: 'ZU', 212: 'CA', 213: 'CE', 214: 'CI', 215: 'CO', 216: 'CU', 217: 'HA', 218: 'HE', 219: 'HI', 220: 'HO', 221: 'HU', 222: 'VOU', 223: 'BOU', 224: 'TOU', 225: 'MOU', 226: 'SOU', 227: 'ZOU', 228: 'POU', 229: 'LOU', 230: 'CHA', 231: 'CHI', 232: 'CHO', 233: 'CHU', 234: 'CHE', 236: 'KA', 237: 'CLE', 239: 'NOM', 240: 'NOMB', 241: 'NOMBR', 242: 'NOMBRE', 243: 'CLO', 245: 'GAU', 246: 'GAUC', 247: 'GAUCH', 248: 'GAUCHE', 249: 'LOR', 250: 'DR', 251: 'DRO', 252: 'DROI', 253: 'DROIT', 254: 'DROITE'}
    output = open("output.txt", "w")
    text=""
    for k in evt:
        if k in dictionary:
            entry = dictionary[k]
        text = text + entry
    #Sauvegarde dans fichier texte
    output.write(text)
    output.close

dec2text()
