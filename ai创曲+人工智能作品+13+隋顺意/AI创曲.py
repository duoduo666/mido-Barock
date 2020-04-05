import mido
from mido import Message, MidiFile, MidiTrack
import random
import pygame
import sys
from pygame.locals import *
import time
import webbrowser

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

def b_three(geng=None,zhong=None,wu=None,yin_type="num"):
    if geng == None and zhong == None and wu == None:
        return "Are you kidding me?"
    if type(geng) == str:
        geng = num(geng)
    elif type(zhong) == str:
        zhong = num(zhong)
    elif type(wu) == str:
        wu = num(wu)
    if yin_type == "num":
        yin = []
        if geng and zhong and wu:
            return "Are you kidding me?"
        if geng and zhong == None and wu == None:    #知道根音
            zhong = geng + 4
            wu = zhong + 3
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if zhong and geng == None and wu == None:      #知道中音
            geng = zhong - 4
            wu = zhong + 3
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if wu and geng == None and zhong == None:      #知道五音
            zhong = wu - 3
            geng = zhong - 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
    

    
#小三和弦
def s_three(geng=None,zhong=None,wu=None,yin_type="num"):
    if geng == None and zhong == None and wu == None:
        return "Are you kidding me?"
    if type(geng) == str:
        geng = num(geng)
    elif type(zhong) == str:
        zhong = num(zhong)
    elif type(wu) == str:
        wu = num(wu)
    if yin_type == "num":
        yin = []
        if geng and zhong and wu:
            return "Are you kidding me?"
        if geng and zhong == None and wu == None:    #知道根音
                zhong = geng + 3
                wu = zhong + 4
                yin.append(geng)
                yin.append(zhong)
                yin.append(wu)
                return yin
        if zhong and geng == None and wu == None:      #知道中音
                geng = zhong - 3
                wu = zhong + 4
                yin.append(geng)
                yin.append(zhong)
                yin.append(wu)
                return yin
        if wu and geng == None and zhong == None:      #知道五音
                zhong = wu - 4
                geng = zhong - 3
                yin.append(geng)
                yin.append(zhong)
                yin.append(wu)
                return yin
            
#增三和弦
def z_three(geng = None,zhong=None,wu=None,yin_type="num"):
    if geng == None and zhong == None and wu == None:
        return "Are you kidding me?"
    if type(geng) == str:
        geng = num(geng)
    elif type(zhong) == str:
        zhong = num(zhong)
    elif type(wu) == str:
        wu = num(wu)
    if yin_type == "num":
        yin = []
        if geng and zhong and wu:
            return "Are you kidding me?"
        if geng and zhong == None and wu == None:    #知道根音
            zhong = geng + 4
            wu = zhong + 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if zhong and geng == None and wu == None:      #知道中音
            geng = zhong - 4
            wu = zhong + 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if wu and geng == None and zhong == None:      #知道五音
            zhong = wu - 4
            geng = zhong - 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        
        
        
#减三和弦
def j_three(geng = None,zhong=None,wu=None,yin_type="num"):
    if geng == None and zhong == None and wu == None:
        return "Are you kidding me?"
    if type(geng) == str:
        geng = num(geng)
    elif type(zhong) == str:
        zhong = num(zhong)
    elif type(wu) == str:
        wu = num(wu)
    if yin_type == "num":
        yin = []
        if geng and zhong and wu:
            return "Are you kidding me?"
        if geng and zhong == None and wu == None:    #知道根音
            zhong = geng + 3
            wu = zhong + 3
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if zhong and geng == None and wu == None:      #知道中音
            geng = zhong - 3
            wu = zhong + 3
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if wu and geng == None and zhong == None:      #知道五音
            zhong = wu - 3
            g_yin = zhong - 3
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
    #四和弦 （第二转为）

#大四和弦

def b_four(geng=None,zhong=None,wu=None,yin_type="num"):
    if type(geng) == str:
        geng = num(geng)
    if type(zhong) == str:
        zhong = num(zhong)
    if type(wu) == str:
        wu = num(wu)
    if geng == None and zhong == None and wu == None:
        return "Are you kidding me?"
    #返回数字
    if yin_type == "num":
        yin = []
        if geng and zhong and wu:                        #若是三个都有
            if zhong - geng == 4 and wu - zhong == 3:    #若是第一转为（三和弦）
                geng += 12
                yin.append(zhong)
                yin.append(wu)
                yin.append(geng)
                return yin
            if zhong - geng == 5 and wu - zhong == 4:    #若是第三转为（6和弦）
                wu -= 12
                yin.append(wu)
                yin.append(geng)
                yin.append(zhong)
                return yin
            if zhong - geng == 3 and wu - zhong == 5:
                return True
        if geng and zhong == None and wu == None:    #知道第一个音
            zhong = geng + 3
            wu = zhong + 5
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if zhong and geng == None and wu == None:    #知道第二个音
            geng = zhong - 3
            wu = zhong + 5
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if wu and geng == None and wu == None:      #知道最高音
            zhong = wu - 5
            geng = zhong - 3
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin

#小四六和弦
def s_four(geng=None,zhong=None,wu=None,yin_type="num"):
    if type(geng) == str:
        geng = num(geng)
    if type(zhong) == str:
        zhong = num(zhong)
    if type(wu) == str:
        wu = num(wu)
    if geng == None and zhong == None and wu == None:
        return "Are you kidding me?"
    #返回数字
    if yin_type == "num":
        yin = []
        if geng and zhong and wu:                        #若是三个都有
            if zhong - geng == 3 and wu - zhong == 4:     #若是第一转位
                geng += 12
                yin.append(zhong)
                yin.append(wu)
                yin.append(geng)
                return yin
            if zhong - geng == 5 and wu - zhong == 6:
                wu -= 12
                yin.append(geng)
                yin.append(wu)
                yin.append(zhong)
                return yin
            if zhong - geng == 4 and wu - zhong == 5:
                return True
        if geng and zhong == None and wu == None:
            zhong = geng + 4
            wu = zhong + 5
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if zhong and geng == None and wu == None:
            geng = zhong -4
            wu = zhong + 5
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if wu and geng == None and zhong == None:
            zhong = wu - 5
            geng = zhong - 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin

#增四和弦
def z_four(geng=None,zhong=None,wu=None,dif=1,yin_type="num"):
    if type(geng) == str:
        geng = num(geng)
    if type(zhong) == str:
        zhong = num(zhong)
    if type(wu) == str:
        wu = num(wu)
    if geng == None and zhong == None and wu == None:
        return "Are you kidding me?"
    #返回数字
    if yin_type == "num":
        yin = []
        if geng and zhong and wu:                        #若是三个都有
            if dif == 1:    #若是第一转为
                geng += 12
                yin.append(zhong)
                yin.append(wu)
                yin.append(geng)
                return yin
            if dif == 2:
                return True
            if dif == 3:
                wu -= 12
                yin.append(wu)
                yin.append(geng)
                yin.append(zhong)
                return yin
        if geng and zhong == None and wu == None:
            zhong = geng + 4
            wu = zhong + 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if zhong and geng == None and wu == None:
            geng = zhong-4
            wu = zhong + 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if wu and geng == None and zhong == None:
            zhong = wu - 4
            geng = zhong - 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin

#减四和弦
def j_four(geng=None,zhong=None,wu=None,yin_type="num"):
    if type(geng) == str:
        geng = num(geng)
    if type(zhong) == str:
        zhong = num(zhong)
    if type(wu) == str:
        wu = num(wu)
    if geng == None and zhong == None and wu == None:
        return "Are you kidding me?"
    #返回数字
    if yin_type == "num":
        yin = []
        if geng and zhong and wu:                        #若是三个都有
            if zhong - geng == 3 and wu - zhong == 3:    #若是第一转为
                geng += 12
                yin.append(zhong)
                yin.append(wu)
                yin.append(geng)
            elif zhong - geng == 6 and wu - zhong == 3:    #若是第二转位
                wu -= 12
                yin.append(wu)
                yin.append(geng)
                yin.append(zhong)
            elif zhong - geng == 3 and wu - zhong == 6:    #若是第二转为
                return True
        if geng and zhong == None and wu == None:        #知道根音
            zhong = geng + 3
            wu = zhong + 3
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if zhong and geng == None and wu == None:        #知道中音
            geng = zhong - 3
            wu = zhong + 3
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if wu and geng == None and zhong == None:
            zhong = wu - 3
            geng = zhong - 3
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
#四六和弦


#大四六和弦

def b_six(geng=None,zhong=None,wu=None,yin_type="num"):
    if type(geng) == str:
        geng = num(geng)
    if type(zhong) == str:
        zhong = num(zhong)
    if type(wu) == str:
        wu = num(wu)
    if geng == None and zhong == None and wu == None:
        return "Are you kidding me?"
    #返回数字
    if yin_type == "num":
        yin = []
        if geng and zhong and wu:                        #若是三个都有
            if zhong - geng == 4 and wu - zhong == 3:    #第一转为
                geng += 12
                zhong += 12
                yin.append(wu)
                yin.append(geng)
                yin.append(zhong)
                return yin
            if zhong - geng == 3 and wu - zhong -- 5:    #第二转为
                geng += 12
                yin.append(zhong)
                yin.append(wu)
                yin.append(geng)
                return yin
        if geng and zhong == None and wu == None:      #知道根音
            zhong = geng + 5
            wu = zhong + 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if zhong and geng == None and wu == None:      #知道中音
            geng = zhong - 5
            wu = zhong + 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if wu and geng == None and wu == None:         #知道五音
            zhong = wu - 4
            geng = zhong - 5
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin

#小四六和弦
def s_six(geng=None,zhong=None,wu=None,yin_type="num"):
    if type(geng) == str:
        geng = num(geng)
    elif type(zhong) == str:
        zhong = num(zhong)
    elif type(wu) == str:
        wu = num(wu)
    if geng == None and zhong == None and wu == None:
        return "Are you kidding me?"
    #返回数字
    if yin_type == "num":
        yin = []
        if geng and zhong and wu:                        #若是三个都有
            if zhong - geng == 3 and wu - zhong == 4:
                geng += 12
                zhong += 12
                yin.append(wu)
                yin.append(geng)
                yin.append(zhong)
                return yin
            if zhong - geng == 4 and wu - zhong == 5:
                geng += 12
                yin.append(zhong)
                yin.append(wu)
                yin.append(geng)
                return yin
        if geng and zhong == None and wu == None:
            zhong = geng + 5
            wu = zhong + 3
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if zhong and geng == None and wu == None:
            geng = zhong - 5 
            wu = zhong + 3
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if wu and geng == None and zhong == None:
            zhong = wu - 3
            geng = zhong - 5
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin

#增四六和弦
def z_six(geng=None,zhong=None,wu=None,dif=1,yin_type="num"):
    if type(geng) == str:
        geng = num(geng)
    elif type(zhong) == str:
        zhong = num(zhong)
    elif type(wu) == str:
        wu = num(wu)
    elif geng == None and zhong == None and wu == None:
        return "Are you kidding me?"
    #返回数字
    if yin_type == "num":
        yin = []
        if geng and zhong and wu:                        #若是三个都有
            if dif == 1:
                geng += 12
                zhong += 12
                yin.append(wu)
                yin.append(geng)
                yin.append(zhong)
                return yin
            if dif == 2:
                geng += 12
                yin.append(zhong)
                yin.append(wu)
                yin.append(geng)
                return yin
            if dif == 3:
                return True
        if geng and zhong == None and wu == None :
            zhong = geng + 4
            wu = zhong + 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if zhong and geng == None and wu == None:
            geng = zhong - 4
            wu = zhong + 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if wu and geng == None and zhong == None:
            zhong = wu - 4
            geng = zhong-4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin

#减四六和弦
def j_six(geng=None,zhong=None,wu=None,yin_type="num"):
    if type(geng) == str:
        geng = num(geng)
    elif type(zhong) == str:
        zhong = num(zhong)
    elif type(wu) == str:
        wu = num(wu)
    if geng == None and zhong == None and wu == None:
        return "Are you kidding me?"
    #返回数字
    if yin_type == "num":
        yin = []
        if geng and zhong and wu:                   #若是三个都有
            if zhong - geng == 3 and wu - zhong == 3:   #第一转为
                geng += 12
                zhong += 12
                yin.append(wu)
                yin.append(geng)
                yin.append(zhong)
                return yin
            if zhong - geng == 3 and wu - zhong == 6:    #第二转位
                geng += 12
                yin.append(zhong)
                yin.append(wu)
                yin.append(geng)
                return yin
            if zhong - geng == 6 and wu - zhong == 3:   #第三转为
                return True
        if geng and zhong == None and wu == None:    #知道根音
            zhong = geng + 6
            wu = zhong + 3
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if zhong and geng == None and wu == None:     #中音
            geng = zhong - 6
            wu = zhong + 3
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if wu and geng == None and wu == None:     #五音
            zhong = wu - 3
            geng = zhong - 6
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
#度（两个音的）

def sd_two(low=None,high=None):         #小二度
    if type(low) == str:
        low = num(low)
    elif type(high) == str:
        high = num(high)
        
    yin = []
    if low == None and high == None:
        return "Are you kidding me?"
    if low and high == None:
        high = low + 1
    if high and low == None:
        low = high - 1
    yin.append(low)
    yin.append(high)
    return yin

def bd_two(low=None,high=None):         #大二度
    if type(low) == str:
        low = num(low)
    elif type(high) == str:
        high = num(high)
    
    yin=[]
    if low and high == None:
        high = low + 2
    if high and low == None:
        low = high - 2
    yin.append(low)
    yin.append(high)
    return yin

def sd_three(low=None,high=None):        #小三度
    if type(low) == str:
        low = num(low)
    elif type(high) == str:
        high = num(high)
        
    yin=[]
    if low and high == None:
        high = low + 3
    if high and low == None:
        low = high - 3
    yin.append(low)
    yin.append(high)
    return yin

def bd_three(low=None,high=None):        #大三度
    if type(low) == str:
        low = num(low)
    elif type(high) == str:
        high = num(high)
        
    yin=[]
    if low and high == None:
        high = low + 4
    if high and low == None:
        low = high - 4
    yin.append(low)
    yin.append(high)
    return yin

def cd_four(low=None,high=None):        #纯四度
    if type(low) == str:
        low = num(low)
    elif type(high) == str:
        high = num(high)
        
    yin=[]
    if low and high == None:
        high = low + 5
    if high and low == None:
        low = high - 5
    yin.append(low)
    yin.append(high)
    return yin

def zd_four(low=None,high=None):        #增四度
    if type(low) == str:
        low = num(low)
    elif type(high) == str:
        high = num(high)
        
    yin=[]
    if low and high == None:
        high = low + 6
    if high and low == None:
        low = high - 6
    yin.append(low)
    yin.append(high)
    return yin

def d_five(low=None,high=None):        #纯五度
    if type(low) == str:
        low = num(low)
    elif type(high) == str:
        high = num(high)
        
    yin=[]
    if low and high == None:
        high = low + 7
    if high and low == None:
        low = high - 7
    yin.append(low)
    yin.append(high)
    return yin

def sd_six(low=None,high=None):        #小六度
    if type(low) == str:
        low = num(low)
    elif type(high) == str:
        high = num(high)
        
    yin=[]
    if low and high == None:
        high = low + 8
    if high and low == None:
        low = high - 8
    yin.append(low)
    yin.append(high)
    return yin

def bd_six(low=None,high=None):        #大六度
    if type(low) == str:
        low = num(low)
    elif type(high) == str:
        high = num(high)
        
    yin=[]
    if low and high == None:
        high = low + 9
    if high and low == None:
        low = high - 9
    yin.append(low)
    yin.append(high)
    return yin

def sd_seven(low=None,high=None):        #小七度
    if type(low) == str:
        low = num(low)
    elif type(high) == str:
        high = num(high)
        
    yin=[]
    if low and high == None:
        high = low + 10
    if high and low == None:
        low = high - 10
    yin.append(low)
    yin.append(high)
    return yin

def bd_seven(low=None,high=None):        #大七度
    if type(low) == str:
        low = num(low)
    elif type(high) == str:
        high = num(high)
        
    yin=[]
    if low and high == None:
        high = low + 11
    if high and low == None:
        low = high - 11
    yin.append(low)
    yin.append(high)
    return yin

def d_eight(low=None,high=None):        #八度
    if type(low) == str:
        low = num(low)
    elif type(high) == str:
        high = num(high)
        
    yin=[]
    if low and high == None:
        high = low + 12
    if high and low == None:
        low = high - 12
    yin.append(low)
    yin.append(high)
    return yin
#训练
#训练
#测试
mid = MidiFile()
track = MidiTrack()
track2 = MidiTrack()
track3 = MidiTrack()
track4 = MidiTrack()
mid.tracks.append(track)
mid.tracks.append(track2)
mid.tracks.append(track3)
mid.tracks.append(track4)
tra = [track,track2,track3,track4]

def yin(yin,pai,qian=0,unit=track,tong=0,liang=100,qi=2):              #yin是指哪个音，pai是指时间（节拍），qian是noteon里的time，liang是指音量，tong是通道，
    if type(yin)== str:
        yin = num(yin)
    unit.append(Message('program_change',channel=0,program=qi,time=0))  #pi是乐器 默认钢琴（2）
    unit.append(Message('note_on', note=yin, velocity=liang, time=int(qian),channel=tong))  #音开始
    unit.append(Message('note_off', note=yin, velocity=liang, time=int(pai),channel=tong))

def beat(time):                  #与mido的拍子互换
    time /= 60 * 1000
    time = 1/time
    return time

def myin(fu,pai,time=120,du=None,chord=None,bef=None,note="low",tr=track,yue=2):   #和声版
    pig = int(beat(time))
    for i in range(len(pai)):
        if type(pai[i]) == list:
            for j in range(len(pai[i])):
                if bef == None:
                    yin(fu[i][j],round(pai[i][j]*pig),unit=tra[j],qi=yue)
                elif bef and len(bef) == 1:
                    yin(fu[i][j],round(pai[i][j]*pig),bef,unit=tra[j],qi=yue)
                else:
                    yin(fu[i][j],round(pai[i][j]*pig),bef[i][j],unit=tra[j],qi=yue)
        else:
            if chord == None and du == None:
                yin(fu[i],pai[i]*pig,unit=tr,qi=yue)
            else:
                #和弦
                b = []
                if chord == "dasan":     #大三和弦
                    if note == "low":
                        b = b_three(fu[i])
                    elif note == "zhong":
                        b = b_three(zhong=fu[i])
                    elif note == "wu":
                        b = b_three(wu=fu[i])
                elif chord == "xiaosan":    #小三（没骂人）
                    if note == "low":
                        b = s_three(fu[i])
                    elif note == "zhong":
                        b = s_three(zhong=fu[i])
                    elif note == "wu":
                        b = s_three(wu=fu[i])
                elif chord == "zengsan":    #增三
                    if note == "low":
                        b = z_three(fu[i])
                    elif note == "zhong":
                        b = z_three(zhong=fu[i])
                    elif note == "wu":
                        b = z_three(wu=fu[i])
                elif chord == "jiansan":    #减三
                    if note == "low":
                        b = j_three(fu[i])
                    elif note == "zhong":
                        b = j_three(zhong=fu[i])
                    elif note == "wu":
                        b = j_three(wu=fu[i])
                elif chord == "dasi":      #大四
                    if note == "low":
                        b = b_four(fu[i])
                    elif note == "zhong":
                        b = b_four(zhong=fu[i])
                    elif note == "wu":
                        b = b_four(wu=fu[i])
                elif chord == "xiaosi":    #小四(没骂人)
                    if note == "low":
                        b = s_four(fu[i])
                    elif note == "zhong":
                        b = s_four(zhong=fu[i])
                    elif note == "wu":
                        b = s_four(wu=fu[i])
                elif chord == "zengsi":    #增四
                    if note == "low":
                        b = z_four(fu[i])
                    elif note == "zhong":
                        b = z_four(zhong=fu[i])
                    elif note == "wu":
                        b = z_four(wu=fu[i])
                elif chord == "jiansi":    #减四
                    if note == "low":
                        b = j_four(fu[i])
                    elif note == "zhong":
                        b = j_four(zhong=fu[i])
                    elif note == "wu":
                        b = j_four(wu=fu[i])
                elif chord == "daliu":     #大四六
                    if note == "low":
                        b = b_six(fu[i])
                    elif note == "zhong":
                        b = b_six(zhong=fu[i])
                    elif note == "wu":
                        b = b_six(wu=fu[i])
                elif chord == "xiaoliu":   #小四六
                    if note == "low":
                        b = s_six(fu[i])
                    elif note == "zhong":
                        b = s_six(zhong=fu[i])
                    elif note == "wu":
                        b = s_six(wu=fu[i])
                elif chord == "zengliu":   #增四六
                    if note == "low":
                        b = z_six(fu[i])
                    elif note == "zhong":
                        b = z_six(zhong=fu[i])
                    elif note == "wu":
                        b = z_six(wu=fu[i])
                elif chord == "jianliu":   #减四六
                    if note == "low":
                        b = j_six(fu[i])
                    elif note == "zhong":
                        b = j_six(zhong=fu[i])
                    elif note == "wu":
                        b = j_six(wu=fu[i])
                #音程（度）
                if du == "xiaoer":                   #小二度
                    if note == "low":
                        b = sd_two(fu[i])
                    if note == "high":
                        b = sd_two(high=fu[i])
                if du == "daer":                     #大二度
                    if note == "low":
                        b = bd_two(fu[i])
                    if note == "high":
                        b = bd_two(high=fu[i])
                if du == "xiaosan":                 #小三度              
                    if note == "low": 
                        b = sd_three(fu[i])
                    if note == "high":
                        b = sd_three(high=fu[i])
                if du == "dasan":                    #大三度
                    if note == "low":
                        b = bd_three(fu[i])
                    if note == "high":
                        b = bd_three(high=fu[i])
                if du == "chunsi":                   #纯四度
                    if note == "low":
                        b = cd_four(fu[i])
                    if note == "high":
                        b = cd_four(high=fu[i])
                if du == "zengsi":                   #增四度
                    if note == "low":
                        b = zd_four(fu[i])
                    if note == "high":
                        b = zd_four(high=fu[i])
                if du == "chunwu" or du == "wu":     #纯五度
                    if note == "low":
                        b = d_five(fu[i])
                    if note == "high":
                        b = d_five(high=fu[i])
                if du == "xiaoliu":                   #小六度
                    if note == "low":
                        b = sd_six(fu[i])
                    if note == "high":
                        b = sd_six(high=fu[i])
                if du == "daliu":                     #大六度
                    if note == "low":
                        b = bd_six(fu[i])
                    if note == "high":
                        b = bd_six(high=fu[i])
                if du == "xiaoqi":                   #小七度
                    if note == "low":
                        b = sd_seven(fu[i])
                    if note == "high":
                        b = sd_seven(high=fu[i])
                if du == "daqi":                    #大七度
                    if note == "low":
                        b = bd_seven(fu[i])
                    if note == "high":
                        b = bd_seven(high=fu[i])
                if du == "badu" or du == "eight" or du == "ba":      #八度
                    if note == "low":
                        b = d_eight(fu[i])
                    if note == "high":
                        b = d_eight(high=fu[i])
                #循环
                for x in range(len(b)):
                    if bef == None:
                        yin(b[x],int(pai[i]*pig),unit=tra[x],qi=yue)
                    if bef:
                        yin(b[x],int(pai[i]*pig),bef[i],unit=tra[x],qi=yue)
#升降号
def sheng(yin):                  #升好 #
    if type(yin) == str:
        return yin == num(yin) + 1
    else:
        return yin + 1
        
def jiang(yin):                   #降号 b
    if type(yin) == str:
        return yin == num(yin) - 1
    else:
        return yin - 1
    
def c_sheng(yin):                 #重升 x
    if type(yin) == str:
        return yin == num(yin) + 2
    else:
        return yin + 2

def c_jiang(yin):                  #重降 bb
    if type(yin) == str:
        return num(yin) - 2
    else:
        return yin - 2
def dao(yin):                      #计算倒影
    a = yin[0] * 2
    daoyin = []
    for i in yin:
        b = a - i
        daoyin.append(b)
    return daoyin 

def dif(first,second):
    if type(first) == str:
        first = num(first)
    if type(second) == str:
        second = num(second)
    if first < second:
        return second - first
    if second < first:
        return first - second

def getdao(xuanlu,base):
    if type(base) == str:
        base = num(base)
    xuanlu = dao(xuanlu)
    high = base - xuanlu[0]
    b= []
    for i in range(len(xuanlu)):
        a = xuanlu[i] + high
        b.append(a)
    return b

def getlu(first,second,ind):
    s = 0
    c = 0
    for i in range(1,len(second)):
        if second[i] != second[s]:
            c += 1
            if c == ind:
                return first[s:i]
            else:
                s = i
    return first[s:]

def gettime(paizi,ind):
    s = 0
    c = 0
    for i in range(1,len(paizi)):
        if paizi[i] != paizi[s]:
            c += 1
            if c == ind:
                return paizi[s:i]
            else:
                s = i
    return paizi[s:]

def tishen(yinlu,ti):
    a = []
    for i in yinlu:
        xxx = i + ti
        a.append(xxx)
    return a

def jieyin(yin):
    a = yin[0] - 12
    b = [a]
    for i in range(6):
        a += 4
        c = b_three(a)
        b.append(c)
    e = b[-1][-1]
    b.append(e)
    b.append(e-4)
    d = e-8
    b.append(e-4)
    b.append(d)
    b.append(e-9)
    b.append(d)
    b.append(yin[0])
    return b
def barok(xuanlu,paizi,jiezou=120):
    qian = getlu(xuanlu,paizi,1)     #一题段音
    hou = getlu(xuanlu,paizi,2)      #二题段音
    qiantime = gettime(paizi,1)      #一提时间
    houtime = gettime(paizi,2)       #二题时间
    
    qiandiba = tishen(qian,-12)    #一提低八
    qiantiwu = tishen(qian,7)     #一题五度
    qiandiwu = tishen(qiandiba,7)   #一题低八度提五度
    
    houdiba = tishen(hou,-12)       #二题低八
    houtiwu = tishen(hou,7)         #二题提五度

    qiandao1 = getdao(qian,houtiwu[-1])    #倒影

    qiandao2 = getdao(qian,qiandao1[-1]-2)   #倒影
    qiandao3 = getdao(qian,qiandao2[-1]-2)   #倒影
    qiandao4 = getdao(qian,qiandao3[-1]-2)   #倒影
    qiantier = tishen(qiandiba,2)          #一提低八高大二度
    
    a = qiandao4[-1] - hou[0]
    houzhong = tishen(hou,qiandao4[-1] - hou[0])            #二题，最后音为上个音
    
    qiandao5 = getdao(qian,houzhong[-1])  #第二次倒影
    qiandao6 = getdao(qian,qiandao5[-1]+2)  #第二次倒影
    qiandao7 = getdao(qian,qiandao6[-1]+2)  #第二次倒影
    qiandao8 = getdao(qian,qiandao7[-1]+2)  #第二次倒影
    
    
    #开始
    #二声部（和弦的）
    myin(qian,qiantime,time=jiezou,tr=track2)
    myin(qiandiba,qiantime,time=jiezou,tr=track2)
    myin(qiantiwu,qiantime,time=jiezou,tr=track2)
    myin(qiandiwu,qiantime,time=jiezou,tr=track2)
    
    myin(qian,qiantime,time= jiezou,tr=track3)
    myin(qiandiba,qiantime,time=jiezou,tr=track3)
    myin(qiantiwu,qiantime,time=jiezou,tr=track3)
    myin(qiandiwu,qiantime,time=jiezou,tr=track3)
    myin(qiandao1,qiantime,time=jiezou,tr=track3)
    myin(qiandao2,qiantime,time=jiezou,tr=track3)
    #一声部
    myin(qian,qiantime,time=jiezou)
    myin(qiandiba,qiantime,time=jiezou)
    myin(qiantiwu,qiantime,time=jiezou)
    myin(qiandiwu,qiantime,time=jiezou)
    
    myin(qiandao1,qiantime,time=jiezou,du="dasan")
    myin(qiandao2,qiantime,time=jiezou,du="daliu")
    myin(qiandao3,qiantime,time=jiezou,chord="dasan",note="wu")
    myin(qiandao4,qiantime,time=jiezou,chord="dasi",note="zhong")
    
    #二声部
    myin(qiantier,qiantime,time= jiezou,tr=track2)
    myin(hou,houtime,time= jiezou,tr=track2)
    myin(qiantier,qiantime,time= jiezou,tr=track3)
    myin(hou,houtime,time= jiezou,tr=track3)
    myin(qiandao5,qiantime,time= jiezou,tr=track3)
    myin(qiandao6,qiantime,time= jiezou,tr=track3)
    
    #返回一声部
    myin(qiantier,qiantime,time= jiezou)
    myin(hou,houtime,time= jiezou)
    
    
    #倒影
    myin(qiandao5,qiantime,time= jiezou,du="daliu")
    myin(qiandao6,qiantime,time= jiezou,du="dasan")
    myin(qiandao7,qiantime,time= jiezou,chord="xiaosan",note="wu")
    myin(qiandao8,qiantime,time= jiezou,chord="dasi",note="zhong")
    
    myin(qiandao5,qiantime,time= jiezou,tr=track2)
    myin(qiandao6,qiantime,time= jiezou,tr=track2)
    myin(qiandao7,qiantime,time= jiezou,tr=track2)
    myin(qiandao8,qiantime,time= jiezou,tr=track2)
    myin(qiandao5,qiantime,time= jiezou,tr=track3)
    myin(qiandao6,qiantime,time= jiezou,tr=track3)
    myin(qiandao7,qiantime,time= jiezou,tr=track3)
    myin(qiandao8,qiantime,time= jiezou,tr=track3)
    #二声部
    myin(qian,qiantime,time= jiezou,tr=track4) #先重复，占第二声部的位
    myin(hou,houtime,time= jiezou,tr=track4)
    myin(houdiba,houtime,time= jiezou,tr=track4)
    myin(houtiwu,houtime,time= jiezou,tr=track4)
    
    myin(qiandao1,qiantime,time=jiezou,tr=track4)
    myin(qiandao2,qiantime,time=jiezou,tr=track4)
    myin(qiandao3,qiantime,time=jiezou,tr=track4)
    myin(qiandao4,qiantime,time=jiezou,tr=track4)

    myin(houzhong,houtime,time=jiezou,tr=track4)

    
  
    xxxx = [1,1,1]
    lastyin = jieyin(xuanlu)
    lastpai = [1,xxxx,xxxx,xxxx,xxxx,xxxx,xxxx,1,0.5,1.5,3]
    myin(lastyin,lastpai,time=jiezou)
    a = lastyin[-1] + 1
    b = [[]]
    b[0].append(a)
    b[0].append(a+4)
    b[0].append(a+7)
    myin(b,[[6,6,6]],chord = "dasan",time=jiezou)


def creatyin(diao="do"):
    if type(diao) == str:
        if diao[0] == "#":
            diao = num(diao[1]) + 1
        elif diao[0] == "b" and len(diao) == 2:
            diao = num(diao[1]) + 1
        else:
            diao = num(diao)
    times = random.randint(6,12)
    yinfu = [diao]
    di = diao - 2
    gao = diao + 8
    for i in range(times):
        a = random.randint(di,gao)
        yinfu.append(a)
    yinfu.append(diao+7)
    return yinfu
    
def creatpai(yinfu):
    a = []
    le = len(yinfu)
    c = random.randint(3,le-3)
    d = le - c
    for i in range(c):
        a.append(1)
    e = c / d
    if int(e) == e:
        e = int(e)
    for i in range(d):
        a.append(e)
    return a



def midosong():
    def xiafile():
        import tkinter as tk
        from tkinter import filedialog
        tk.Tk().withdraw()
        Folderpath = filedialog.askdirectory()
        return Folderpath
    def fetch(sudu,diaoxin,lujin,mingzi):
        try:
            if diaoxin == "" or diaoxin == None:
                a = creatyin()
                b = creatpai(a)
            else:
                a = creatyin(diaoxin)
                b = creatpai(a)
            if sudu == "" or sudu == None:
                barok(a,b,jiezou=500)
            else:
                barok(a,b,jiezou=int(sudu))
            abcde = lujin + "/" + mingzi + ".mid"
            mid.save(abcde)
        
        except:
            screen.fill(white)
            login()
            xxxxx = "啊呀，出错，请查看'错误！错在哪了？'"
            word = t.render(xxxxx,True,(0,0,0),white)
            screen.blit(word,(400,200))
            
            pygame.display.flip()
        else:
            screen.fill(white)
            screen.blit(chuangzuo,(0,0))
            pygame.display.flip()
            time.sleep(1)
            screen.fill(white)
            screen.blit(title,(0,0))
            screen.blit(bofang,(430,180)) #播放
            screen.blit(again,(800,520))   #再来一首
            screen.blit(plane,(650,100))
            screen.blit(ship,(40,300))
            t1=pygame.font.SysFont('SimHei',48)
            word = t1.render(mingzi,True,(0,0,0),white)
            screen.blit(word,(500-12.5*len(mingzi),0))
    def ttt(word, w, pos, isBackspace=False):
        if isBackspace:
            word = word[:-1]
        else:
            word += w
        nw = t.render(word, True, (0,0,0), white)
        screen.blit(nw, pos)
        pygame.display.flip()
        return word
    
        
    def first():
        screen.fill(white)
        screen.blit(wuxian,(0,310))
        screen.blit(ship,(530,20))
        screen.blit(plane,(100,20))
        screen.blit(b_begin,(350,300))
        pygame.display.flip()
    
    def second():
        screen.fill(white)
        screen.blit(back,(0,0))
        screen.blit(one_creat,(400,100))
        screen.blit(helps,(425,410))
        pygame.display.flip()
    
    
    def creat_one():
        screen.fill(white)
        screen.blit(back,(0,0))
        screen.blit(paizi,(390,30))
        screen.blit(man,(0,195))
        screen.blit(zhong,(360,300))#加60
        screen.blit(kuai,(730,195))
        a = "默认(AI创作)"
        word = t.render(a,True,(0,0,0),white)
        screen.blit(word,(400,200))
        screen.blit(ok,(800,0))
        pygame.display.flip()
        
    def creat_diao():
        screen.fill(white)
        screen.blit(back,(0,0))
        screen.blit(diao,(390,30))
        screen.blit(dadiao,(0,300))
        screen.blit(xiaodiao,(0,463))
        a = "默认(AI创作)"
        word = t.render(a,True,(0,0,0),white)
        screen.blit(word,(400,200))
        screen.blit(ok,(800,0))
        pygame.display.flip()
    
    def creat_lu():
        screen.fill(white)
        screen.blit(back,(0,0))
        screen.blit(lu,(390,30))
        screen.blit(wenjian,(400,300))
        a = 'D:/'
        word = t.render(a,True,(0,0,0),white)
        screen.blit(word,(400,200))
        screen.blit(ok,(800,0))
        pygame.display.flip()
        
    def creat_ming():
        screen.fill(white)
        screen.blit(back,(0,0))
        screen.blit(over,(750,0))
        screen.blit(ming,(390,30))
        a = "来个英文名"
        word = t.render(a,True,(0,0,0),white)
        screen.blit(word,(400,200))
        pygame.display.flip()
    
    
    def login():
        webbrowser.open(ad2+"错误！错在哪了？.html")
    
        
    pygame.init()
    screen_size = width,height = 1000,618
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("AI创曲")
    white = (255,255,255)
    t=pygame.font.SysFont('SimHei',32)
    
    #图片
    #地址
    ad = ("D:\\ai创曲+人工智能作品+13+隋顺意\\image\\")
    ad2 =  "D:\\ai创曲+人工智能作品+13+隋顺意\\"
    wuxian = pygame.image.load(ad + "wuxian.png")
        
    b_begin = pygame.image.load(ad + "b_begin.png")
    back = pygame.image.load(ad + "back.png")
    ship = pygame.transform.rotate(pygame.image.load(ad + "ship.png"),-10)
    plane = pygame.transform.rotate(pygame.image.load(ad + "plane.png"),10)
    paizi = pygame.image.load(ad + "jiezou.png")
    diao = pygame.image.load(ad + "diaoxing.png")
    lu = pygame.image.load(ad + "lu.png")
    man = pygame.image.load(ad + "man.png")
    zhong = pygame.image.load(ad + "zhong.png")
    kuai = pygame.image.load(ad + "kuai.png")
    ok = pygame.image.load(ad + "ok.png")
    one_creat = pygame.image.load(ad + "one-creat.png") 
    ming = pygame.image.load(ad + "ming.png")
    over = pygame.image.load(ad + "over.png")
    wenjian = pygame.image.load(ad + "wenjian.png")
    dadiao = pygame.image.load(ad + "dadiao.png")
    xiaodiao = pygame.image.load(ad + "xiaodiao.png")
    chuangzuo = pygame.image.load(ad + "chuangzuo.png")  #AI生成中那个画面
    title = pygame.image.load(ad + "title.png")
    bofang = pygame.image.load(ad + "bofang.png")
    helps = pygame.image.load(ad + "help.png")
    again = pygame.image.load(ad + "again.png")
    lingshi = pygame.transform.scale(pygame.image.load(ad + "lingshi.png"),(100,100))  #####零时
    first()
    
    
    xxx = "                        "
    place = 0
    pai_word = ""
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if place == 0:
                    second()
                    place = 1
                    continue
                if 425 <= x <= 575 and 410 <= y <= 533:
                    if place == 1:
                        webbrowser.open(ad2+"help.html")
                if 0 <= x <= 150 and 0 <= y <= 100:    #back(返回)
                    if place == 1:
                        first()
                        place = 0
                        continue
                    if place == 2:
                        second()
                        place = 1
                        pai_word = ""
                        continue
                    if place == 3:
                        creat_one()
                        if pai_word != "":
                            ttt(xxx,"",(400,200))
                            ttt(pai_word,'',(400,200))
                        place = 2
                        continue
                    if place == 4:
                        creat_diao()
                        if diao_word != "":
                            ttt(xxx,"",(400,200))
                            ttt(diao_word,'',(400,200))
                        place = 3
                        continue
                    if place == 5:
                        creat_lu()
                        if lu_word != "":
                            ttt(xxx,"",(400,200))
                            ttt(lu_word,'',(400,200))
                        place = 4
                        continue
                
                if  400 <= x <= 600 and 100 <= y <= 340:   #进入节奏页面
                    if place == 1:
                        creat_one()
                        place = 2
                        continue
                #离上是195
                #宽74
                if 7 <= x <= 120 and 282 <= y <= 356:    #速度（Grave40)
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '40', (400,200))
                if 7 <= x <= 120 and 368 <= y <= 443:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '50', (400,200))
                if 7 <= x <= 120 and 435 <= y <= 529:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '60', (400,200))
                if 7 <= x <= 120 and 543 <= y <= 617:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '72', (400,200))
                if 149 <= x <= 260 and 282 <= y <= 356:   #速度第二排(Largo)
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '44', (400,200)) 
                if 149 <= x <= 260 and 368 <= y <= 443:   
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '56', (400,200))
                if 149 <= x <= 260 and 435 <= y <= 529:  
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '60', (400,200))
                if 149 <= x <= 260 and 543 <= y <= 617:   
                    if place == 2:
                        xxx = ttt(xxx,"",(400,200))
                        pai_word = ttt(pai_word, '80', (400,200))
                if 363 <= x <= 489 and 412 <= y <= 495:   #中速
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '96', (400,200))
                if 363 <= x <= 489 and 517 <= y <= 601:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '100', (400,200))
                if 511 <= x <= 636 and 412 <= y <= 495:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '108', (400,200))
                if 511 <= x <= 636 and 517 <= y <= 601:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '120', (400,200))
                #高195，左730,宽114
                if 737 <= x <= 851 and 280 <= y <= 354:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '132', (400,200))
                if 737 <= x <= 851 and 367 <= y <= 440:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '160', (400,200))
                if 737 <= x <= 851 and 454 <= y <= 530:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '200', (400,200))
                if 737 <= x <= 851 and 546 <= y <= 622:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '300', (400,200))
                if 880 <= x <= 994 and 280 <= y <= 354:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '144', (400,200))
                if 880 <= x <= 994 and 367 <= y <= 440:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '184', (400,200))
                if 880 <= x <= 994 and 454 <= y <= 530:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '208', (400,200))
                if 880 <= x <= 994 and 546 <= y <= 622:
                    if place == 2:
                        xxx = ttt(xxx,'',(400,200))
                        pai_word = ttt(pai_word, '500', (400,200))
                #调性
                if 181 <= x <= 252 and 305 <= y <= 379:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "G", (400,200))
                if 302 <= x <= 370 and 305 <= y <= 379:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "D", (400,200))
                if 419 <= x <= 492 and 305 <= y <= 379:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "A", (400,200))
                if 532 <= x <= 602 and 305 <= y <= 379:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "E", (400,200))
                if 634 <= x <= 721 and 305 <= y <= 379:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "B", (400,200))
                if 757 <= x <= 828 and 305 <= y <= 379:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "#F", (400,200))
                if 870 <= x <= 943 and 305 <= y <= 379:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "#C", (400,200))
                #大调第二排
                if 231 <= x <= 307 and 383 <= y <= 456:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "F", (400,200))
                if 349 <= x <= 422 and 383 <= y <= 456:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "bB", (400,200))
                if 469 <= x <= 541 and 383 <= y <= 456:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "bE", (400,200))
                if 583 <= x <= 653 and 383 <= y <= 456:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "bA", (400,200))
                if 701 <= x <= 773 and 383 <= y <= 456:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "bD", (400,200))
                if 815 <= x <= 890 and 383 <= y <= 456:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "bG", (400,200))
                #小调
                if 140 <= x <= 216 and 463 <= y <= 583:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "e", (400,200))
                if 265 <= x <= 333 and 463 <= y <= 583:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "b", (400,200))
                if 380 <= x <= 452 and 463 <= y <= 583:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "f", (400,200))
                if 506 <= x <= 579 and 463 <= y <= 583:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "c", (400,200))
                if 630 <= x <= 704 and 463 <= y <= 583:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "#g", (400,200))
                if 755 <= x <= 827 and 463 <= y <= 583:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "#d", (400,200))
                if 877 <= x <= 948 and 463 <= y <= 583:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "#a", (400,200))
                #第二排
                if 198 <= x <= 276 and 538 <= y <= 606:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "d", (400,200))
                if 320 <= x <= 392 and 538 <= y <= 606:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "bf", (400,200))
                if 448 <= x <= 517 and 538 <= y <= 606:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "#c", (400,200))
                if 566 <= x <= 638 and 538 <= y <= 606:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "#f", (400,200))
                if 695 <= x <= 765 and 538 <= y <= 606:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "bb", (400,200))
                if 820 <= x <= 892 and 538 <= y <= 606:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "be", (400,200))
                if 50 <= x <= 151 and 482 <= y <= 576:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "a", (400,200))
                if 67 <= x <= 165 and 341 <= y <= 433:
                    if place == 3:
                        xxx = ttt(xxx,'',(400,200))
                        diao_word = ttt(diao_word, "C", (400,200))
                if 800 <= x <= 950 and 520 <= y <= 584:
                    if place == 6:
                        pygame.quit()
                        exit()
                
                
                if 400 <= x <= 600 and 300 <= y <= 371:   #打开文件夹
                    if place == 4:
                        xxx = ttt(xxx,'',(400,200))
                        lu_word = xiafile()
                        ttt(lu_word,'',(400,200))
            
                
                #ok(选定了)
                if 800 <= x <= 1000 and 0 <= y <= 124:
                    if place == 2:
                        creat_diao()
                        place = 3
                        diao_word = ""
                        continue
                    if place == 3:
                        creat_lu()
                        place = 4
                        lu_word = "D:/"
                        continue
                    if place == 4:
                        creat_ming()
                        place = 5
                        ming_word = ""
                        continue
                
                if 750 <= x <= 1000 and 0 <= y <= 144:    #交给AI生成
                    if place == 5:
                        screen.fill(white)
                        fetch(pai_word,diao_word,lu_word,ming_word)
                        place = 6
                        pygame.display.flip()
    
                if 430 <= x <= 570 and 180 <= y <= 330:   #播放
                    if place == 6:
                        pygame.mixer.init()
                        pylu = lu_word + "/" + ming_word + ".mid"
                        pygame.mixer.music.load(pylu)
                        pygame.mixer.music.play(1)
                        pygame.display.flip()
                
                        
                        
                        
            #键盘处理            
            if event.type == KEYDOWN:
                if place == 2:
                    ttt(xxx,"",(400,200))
                    if event.key == K_BACKSPACE:    #删除
                        pai_word = ttt(pai_word, '', (400,200),True)
                    if event.key == K_1 or event.key == K_KP1:
                        pai_word = ttt(pai_word, '1', (400,200))
                    if event.key == K_2 or event.key == K_KP2:      #2
                        pai_word = ttt(pai_word, '2', (400,200))
                    if event.key == K_3 or event.key == K_KP3:      #3
                        pai_word = ttt(pai_word, '3', (400,200))
                    if event.key == K_4 or event.key == K_KP4:      #4
                        pai_word = ttt(pai_word, '4', (400,200))
                    if event.key == K_5 or event.key == K_KP5:      #5
                        pai_word = ttt(pai_word, '5', (400,200))
                    if event.key == K_6 or event.key == K_KP6:      #6
                        pai_word = ttt(pai_word, '6', (400,200))
                    if event.key == K_7 or event.key == K_KP7:      #7
                        pai_word = ttt(pai_word, '7', (400,200))
                    if event.key == K_8 or event.key == K_KP8:      #8
                        pai_word = ttt(pai_word, '8', (400,200))
                    if event.key == K_9 or event.key == K_KP9:      #9
                        pai_word = ttt(pai_word, '9', (400,200))
                    if event.key == K_0 or event.key == K_KP0:      #0
                        pai_word = ttt(pai_word, '0', (400,200))
                
                if place == 3:
                    ttt(xxx, "                        ", (400,200))
                    if event.key == K_BACKSPACE:    #删除
                        diao_word = ttt(diao_word, '', (400,200),True)
                    elif event.key == K_c:    #c
                        diao_word = ttt(diao_word, 'c', (400,200))
                    elif event.key == K_d:    #d
                        diao_word = ttt(diao_word, 'd', (400,200))
                    elif event.key == K_e:    #e
                        diao_word = ttt(diao_word, 'e', (400,200))
                    elif event.key == K_f:    #f
                        diao_word = ttt(diao_word, 'f', (400,200))
                    elif event.key == K_g:    #g
                        diao_word = ttt(diao_word, 'g', (400,200))
                        pygame.display.flip()
                    elif event.key == K_a:    #a
                        diao_word = ttt(diao_word, 'a', (400,200))
                    elif event.key == K_b:    #b
                        diao_word = ttt(diao_word, 'b', (400,200))
                    else:
                        ttt(diao_word, '', (400,200))
                        
                if place == 4:  #路径
                    ttt(xxx, "                        ", (400,200))
                    if event.key == K_BACKSPACE:    #删除
                        lu_word = ttt(lu_word, '', (400,200),True)
                    elif event.key == K_a:   #a  
                        lu_word = ttt(lu_word, 'a', (400,200))
                    elif event.key == K_b:   #b  
                        lu_word = ttt(lu_word, 'b', (400,200))
                    elif event.key == K_c:   #c  
                        lu_word = ttt(lu_word, 'c', (400,200))
                    elif event.key == K_d:   #d  
                        lu_word = ttt(lu_word, 'd', (400,200))
                    elif event.key == K_e:   #e  
                        lu_word = ttt(lu_word, 'e', (400,200))
                    elif event.key == K_f:   #f  
                        lu_word = ttt(lu_word, 'f', (400,200))
                    elif event.key == K_g:   #g
                        lu_word = ttt(lu_word, 'g', (400,200))
                    elif event.key == K_h:   #h  
                        lu_word = ttt(lu_word, 'h', (400,200))
                    elif event.key == K_i:   #i 
                        lu_word = ttt(lu_word, 'i', (400,200))
                    elif event.key == K_j:   #j  
                        lu_word = ttt(lu_word, 'j', (400,200))
                    elif event.key == K_k:   #k  
                        lu_word = ttt(lu_word, 'k', (400,200))
                    elif event.key == K_l:   #l  
                        lu_word = ttt(lu_word, 'l', (400,200))
                    elif event.key == K_m:   #m  
                        lu_word = ttt(lu_word, 'm', (400,200))
                    elif event.key == K_n:   #n  
                        lu_word = ttt(lu_word, 'n', (400,200))
                    elif event.key == K_o:   #o  
                        lu_word = ttt(lu_word, 'o', (400,200))
                    elif event.key == K_p:   #p  
                        lu_word = ttt(lu_word, 'p', (400,200))
                    elif event.key == K_q:   #q  
                        lu_word = ttt(lu_word, 'q', (400,200))
                    elif event.key == K_r:   #r  
                        lu_word = ttt(lu_word, 'r', (400,200))
                    elif event.key == K_s:   #s  
                        lu_word = ttt(lu_word, 's', (400,200))
                    elif event.key == K_t:   #t  
                        lu_word = ttt(lu_word, 't', (400,200))
                    elif event.key == K_u:   #u  
                        lu_word = ttt(lu_word, 'u', (400,200))
                    elif event.key == K_v:   #v  
                        lu_word = ttt(lu_word, 'v', (400,200))
                    elif event.key == K_w:   #w  
                        lu_word = ttt(lu_word, 'w', (400,200))
                    elif event.key == K_x:   #x  
                        lu_word = ttt(lu_word, 'x', (400,200))
                    elif event.key == K_y:   #y  
                        lu_word = ttt(lu_word, 'y', (400,200))
                    elif event.key == K_z:   #z
                        lu_word = ttt(lu_word, 'z', (400,200))
                    
                    elif event.key == K_1 or event.key == K_KP1:   #1
                        lu_word = ttt(lu_word, '1', (400,200))
                    elif event.key == K_2 or event.key == K_KP2:   #2
                        lu_word = ttt(lu_word, '2', (400,200))
                    elif event.key == K_3 or event.key == K_KP3:   #3
                        lu_word = ttt(lu_word, '3', (400,200))
                    elif event.key == K_4 or event.key == K_KP4:   #4
                        lu_word = ttt(lu_word, '4', (400,200))
                    elif event.key == K_5 or event.key == K_KP5:   #5
                        lu_word = ttt(lu_word, '5', (400,200))
                    elif event.key == K_6 or event.key == K_KP6:   #6
                        lu_word = ttt(lu_word, '6', (400,200))
                    elif event.key == K_7 or event.key == K_KP7:   #7
                        lu_word = ttt(lu_word, '7', (400,200))
                    elif event.key == K_8 or event.key == K_KP8:   #8
                        lu_word = ttt(lu_word, '8', (400,200))
                    elif event.key == K_9 or event.key == K_KP9:   #9
                        lu_word = ttt(lu_word, '9', (400,200))
                    elif event.key == K_0 or event.key == K_KP0:   #0
                        lu_word = ttt(lu_word, '0', (400,200))
                    elif event.key == K_SLASH:   #/
                        lu_word = ttt(lu_word, '/', (400,200))
                    elif event.key == K_BACKSLASH:   #\
                        lu_word = ttt(lu_word, '\\', (400,200))
                    elif event.key == K_COLON or event.key == K_SEMICOLON:
                        lu_word = ttt(lu_word, ':', (400,200))
                    else:
                        lu_word = ttt(lu_word, '', (400,200))
                
                if place == 5:
                    ttt(xxx, "                        ", (400,200))
                    if event.key == K_BACKSPACE:    #删除
                        ming_word = ttt(ming_word, '', (400,200),True)
                    elif event.key == K_a:   #a  
                        ming_word = ttt(ming_word, 'a', (400,200))
                    elif event.key == K_b:   #b  
                        ming_word = ttt(ming_word, 'b', (400,200))
                    elif event.key == K_c:   #c  
                        ming_word = ttt(ming_word, 'c', (400,200))
                    elif event.key == K_d:   #d  
                        ming_word = ttt(ming_word, 'd', (400,200))
                    elif event.key == K_e:   #e  
                        ming_word = ttt(ming_word, 'e', (400,200))
                    elif event.key == K_f:   #f  
                        ming_word = ttt(ming_word, 'f', (400,200))
                    elif event.key == K_g:   #g
                        ming_word = ttt(ming_word, 'g', (400,200))
                    elif event.key == K_h:   #h  
                        ming_word = ttt(ming_word, 'h', (400,200))
                    elif event.key == K_i:   #i 
                        ming_word = ttt(ming_word, 'i', (400,200))
                    elif event.key == K_j:   #j  
                        ming_word = ttt(ming_word, 'j', (400,200))
                    elif event.key == K_k:   #k  
                        ming_word = ttt(ming_word, 'k', (400,200))
                    elif event.key == K_l:   #l  
                        ming_word = ttt(ming_word, 'l', (400,200))
                    elif event.key == K_m:   #m  
                        ming_word = ttt(ming_word, 'm', (400,200))
                    elif event.key == K_n:   #n  
                        ming_word = ttt(ming_word, 'n', (400,200))
                    elif event.key == K_o:   #o  
                        ming_word = ttt(ming_word, 'o', (400,200))
                    elif event.key == K_p:   #p  
                        ming_word = ttt(ming_word, 'p', (400,200))
                    elif event.key == K_q:   #q  
                        ming_word = ttt(ming_word, 'q', (400,200))
                    elif event.key == K_r:   #r  
                        ming_word = ttt(ming_word, 'r', (400,200))
                    elif event.key == K_s:   #s  
                        ming_word = ttt(ming_word, 's', (400,200))
                    elif event.key == K_t:   #t  
                        ming_word = ttt(ming_word, 't', (400,200))
                    elif event.key == K_u:   #u  
                        ming_word = ttt(ming_word, 'u', (400,200))
                    elif event.key == K_v:   #v  
                        ming_word = ttt(ming_word, 'v', (400,200))
                    elif event.key == K_w:   #w  
                        ming_word = ttt(ming_word, 'w', (400,200))
                    elif event.key == K_x:   #x  
                        ming_word = ttt(ming_word, 'x', (400,200))
                    elif event.key == K_y:   #y  
                        ming_word = ttt(ming_word, 'y', (400,200))
                    elif event.key == K_z:   #z
                        ming_word = ttt(ming_word, 'z', (400,200))
                    
                    elif event.key == K_1 or event.key == K_KP1:
                        ming_word = ttt(ming_word, '1', (400,200))
                    elif event.key == K_2 or event.key == K_KP2:
                        ming_word = ttt(ming_word, '2', (400,200))
                    elif event.key == K_3 or event.key == K_KP3:   #3
                        ming_word = ttt(ming_word, '3', (400,200))
                    elif event.key == K_4 or event.key == K_KP4:
                        ming_word = ttt(ming_word, '4', (400,200))
                    elif event.key == K_5 or event.key == K_KP5:
                        ming_word = ttt(ming_word, '5', (400,200))
                    elif event.key == K_6 or event.key == K_KP6:
                        ming_word = ttt(ming_word, '6', (400,200))
                    elif event.key == K_7 or event.key == K_KP7:
                        ming_word = ttt(ming_word, '7', (400,200))
                    elif event.key == K_8 or event.key == K_KP8:
                        ming_word = ttt(ming_word, '8', (400,200))
                    elif event.key == K_9 or event.key == K_KP9:
                        ming_word = ttt(ming_word, '9', (400,200))
                    elif event.key == K_0 or event.key == K_KP0:
                        ming_word = ttt(ming_word, '0', (400,200))
                    elif event.key == K_SPACE:
                        ming_word = ttt(ming_word, '  ', (400,200))
                    else:
                        ttt(ming_word, '', (400,200))
                    
                    

if __name__ == "__main__":  
    midosong()