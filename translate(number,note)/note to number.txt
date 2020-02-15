import mido
from mido import Message, MidiFile, MidiTrack

#把音名、唱名等换成 MIDO相对应的数字
#已完成
def num(yin):                    
    if yin == "A0" or yin =="a0":            #最低音 la
        return 21
    if yin == "B0" or yin == "b0":           #最低的si
        return 23
    if yin == "C1" or yin == "c1":           #低三个八度 do
        return 24
    if yin == "D1" or yin == "d1":           #re
        return 26
    if yin == "E1" or yin == "e1":           #mi
        return 28
    if yin == "F1" or yin == "f1":           #fa
        return 29
    if yin == "G1" or yin == "g1":           #so 或者说 sol
        return 31
    if yin == "A1" or yin == "a1":           #la
        return 33
    if yin == "B1" or yin == "b1":           #si
        return 35
    if yin == "C2" or yin == "c2":           #低两个八度 do
        return 36
    if yin == "D2" or yin == "d2":           #re
        return 38
    if yin == "E2" or yin == "e2":           #mi
        return 40
    if yin == "F2" or yin == "f2":           #fa
        return 41
    if yin == "G2" or yin == "g2":           #so 或者说 sol
        return 43
    if yin == "A2" or yin == "a2":           #la
        return 45
    if yin == "B2" or yin == "b2":           #si
        return 47
    if yin == "C3" or yin == "c3" or yin == ".do" or yin == ".1" or yin == ".Do" or yin == ".DO":          #低八度   do
        return 48
    if yin == "D3" or yin == "d3" or yin == ".re" or yin == ".2" or yin == ".Re" or yin == ".RE":           #re
        return 50
    if yin == "E3" or yin == "e3" or yin == ".mi" or yin == ".3" or yin == ".Mi" or yin == ".MI":           #mi
        return 52
    if yin == "F3" or yin == "f3" or yin == ".fa" or yin == ".4" or yin == ".Fa" or yin == ".FA":           #fa
        return 53
    if yin == "G3" or yin == "g3" or yin == ".so" or yin == ".sol" or yin == ".5" or yin == ".So" or yin == ".Sol" or yin == ".SO" or yin == ".SOL":   #so 或者说 sol
        return 55
    if yin == "A3" or yin == "a3" or yin == ".la" or yin == ".6" or yin == ".La" or yin == ".LA":            #la
        return 57
    if yin == "B3" or yin == "b3" or yin == ".si" or yin == ".7" or yin == ".Si" or yin == ".SI":             #si
        return 59
    #中音区
    if yin == "C4" or yin == "c4" or yin == "C" or yin == "c" or yin == "1" or yin == 1 or yin == "do" or yin == "Do" or yin == "DO":       #中音do
        return 60
    if yin == "D4" or yin == "d4" or yin == "D" or yin == "d" or yin == "2" or yin == 2 or yin == "re" or yin == "Re" or yin == "RE":        #中音re
        return 62
    if yin == "E4" or yin == "e4" or yin == "E" or yin == "e" or yin == "3" or yin == 3 or yin == "mi" or yin == "Mi" or yin == "MI":       #中音mi
        return 64
    if yin == "F4" or yin == "f4" or yin == "F" or yin == "f" or yin == "4" or yin == 4 or yin == "fa" or yin == "Fa" or yin == "FA":       #中音fa
        return 65
    if yin == "G4" or yin == "g4" or yin == "G" or yin == "g" or yin == "5" or yin == 5 or yin == "so" or yin == "sol" or yin == "So" or yin == "Sol" or yin == "SO" or yin == "SOL":   #中音so  或者说 sol
        return 67
    if yin == "A4" or yin == "a4" or yin == "A" or yin == "a" or yin == "6" or yin == 6 or yin == "la" or yin == "La" or yin == "LA":       #中音la
        return 69
    if yin == "B4" or yin == "b4" or yin == "B" or yin == "b" or yin == "7" or yin == 7 or yin == "si" or yin == "Si" or yin == "SI":       #中音si
        return 71
    #高音区
    if yin == "C5" or yin == "c5" or yin == "1." or yin == "do." or yin == "Do." or yin == "DO.":   #do
        return 72
    if yin == "D5" or yin == "d5" or yin == "2." or yin == "re." or yin == "Re." or yin == "RE.":   #re 
        return 74
    if yin == "E5" or yin == "e5" or yin == "3." or yin == "mi." or yin == "Mi." or yin == "MI.":   #mi
        return 76
    if yin == "F5" or yin == "f5" or yin == "4." or yin == "fa." or yin == "Fa." or yin == "FA.":   #fa
        return 77
    if yin == "G5" or yin == "g5" or yin == "5." or yin == "so." or yin == "So." or yin == "SO." or yin == "sol." or yin == "Sol." or yin == "SOL.":       #so 或者说是 sol
        return 79 
    if yin == "A5" or yin == "a5" or yin == "6." or yin == "la." or yin == "La." or yin == "LA.":   #la
        return 81
    if yin == "B5" or yin == "b5" or yin == "7." or yin == "si." or yin == "Si." or yin == "SI.":   #si
        return 83
    #从此，退出常用区
    #高两个八度
    if yin == "C6" or yin == "c6":      #do
        return 84
    if yin == "D6" or yin == "d6":      #re
        return 86
    if yin == "E6" or yin == "e6":      #mi
        return 88
    if yin == "F6" or yin == "f6":      #fa
        return 89
    if yin == "G6" or yin == "g6":      #so
        return 91
    if yin == "A6" or yin == "a6":      #la
        return 93
    if yin == "B6" or yin == "b6":      #si
        return 95
    #高三个八度
    if yin == "C7" or yin == "c7":       #do
        return 96
    if yin == "D7" or yin == "d7":       #re
        return 98
    if yin == "E7" or yin == "e7":       #mi
        return 100
    if yin == "F7" or yin == "f7":       #fa
        return 101
    if yin == "G7" or yin == "g7":       #so
        return 103
    if yin == "A7" or yin == "a7":       #la
        return 105
    if yin == "B7" or yin == "b7":       #si
        return 107
    #高四个八度
    #最高音do
    if yin == "C8" or yin == "c8" or yin == "highestdo" or yin == "hdo" or yin == "h1" or yin == "highest1":  #do
        return 108