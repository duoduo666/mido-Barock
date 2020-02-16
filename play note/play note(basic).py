import mido
from mido import Message, MidiFile, MidiTrack
#训练
#测试
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

def yin(yin,pai,qian=0,unit=track,tong=0,liang=64,qi=2):              #yin是指哪个音，pai是指时间（节拍），qian是noteon里的time，liang是指音量，tong是通道，
    if type(yin)== str:
        yin = num(yin)
    unit.append(Message('program_change',channel=0,program=qi,time=0))  #pi是乐器 默认钢琴（2）
    unit.append(Message('note_on', note=yin, velocity=liang, time=qian,channel=tong))  #音开始
    unit.append(Message('note_off', note=yin, velocity=liang, time=pai,channel=tong))

def beat(time):                  #与mido的拍子互换
    time /= 60 * 1000
    time = 1/time
    return time

def myin(fu,pai,time=120,chord=None,bef=None,note="geng",yue=2):   #和声版
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
            if chord == None:
                yin(fu[i],pai[i]*pig,qi=yue)
            else:
                if chord == "dasan":     #大三和弦
                    if note == "geng":
                        fu[i] = b_three(fu[i])
                    elif note == "zhong":
                        fu[i] = b_three(zhong=fu[i])
                    elif note == "wu":
                        fu[i] = b_three(zhong=fu[i])
                elif chord == "xiaosan":    #小三（没骂人）
                    if note == "geng":
                        fu[i] = s_three(fu[i])
                    elif note == "zhong":
                        fu[i] = s_three(zhong=fu[i])
                    elif note == "wu":
                        fu[i] = s_three(zhong=fu[i])
                elif chord == "zengsan":    #增三
                    if note == "geng":
                        fu[i] = z_three(fu[i])
                    elif note == "zhong":
                        fu[i] = z_three(zhong=fu[i])
                    elif note == "wu":
                        fu[i] = z_three(zhong=fu[i])
                elif chord == "jiansan":    #减三
                    if note == "geng":
                        fu[i] = j_three(fu[i])
                    elif note == "zhong":
                        fu[i] = j_three(zhong=fu[i])
                    elif note == "wu":
                        fu[i] = j_three(zhong=fu[i])
                elif chord == "dasi":      #大四
                    if note == "geng":
                        fu[i] = b_four(fu[i])
                    elif note == "zhong":
                        fu[i] = b_four(zhong=fu[i])
                    elif note == "wu":
                        fu[i] = b_four(zhong=fu[i])
                elif chord == "xiaosi":    #小四(没骂人)
                    if note == "geng":
                        fu[i] = s_four(fu[i])
                    elif note == "zhong":
                        fu[i] = s_four(zhong=fu[i])
                    elif note == "wu":
                        fu[i] = s_four(zhong=fu[i])
                elif chord == "zengsi":    #增四
                    if note == "geng":
                        fu[i] = z_four(fu[i])
                    elif note == "zhong":
                        fu[i] = z_four(zhong=fu[i])
                    elif note == "wu":
                        fu[i] = z_four(zhong=fu[i])
                elif chord == "jiansi":    #减四
                    if note == "geng":
                        fu[i] = j_four(fu[i])
                    elif note == "zhong":
                        fu[i] = j_four(zhong=fu[i])
                    elif note == "wu":
                        fu[i] = j_four(zhong=fu[i])
                elif chord == "daliu":     #大四六
                    if note == "geng":
                        fu[i] = b_six(fu[i])
                    elif note == "zhong":
                        fu[i] = b_six(zhong=fu[i])
                    elif note == "wu":
                        fu[i] = b_six(zhong=fu[i])
                elif chord == "xiaoliu":   #小四六
                    if note == "geng":
                        fu[i] = s_six(fu[i])
                    elif note == "zhong":
                        fu[i] = s_six(zhong=fu[i])
                    elif note == "wu":
                        fu[i] = s_six(zhong=fu[i])
                elif chord == "zengliu":   #增四六
                    if note == "geng":
                        fu[i] = z_six(fu[i])
                    elif note == "zhong":
                        fu[i] = z_six(zhong=fu[i])
                    elif note == "wu":
                        fu[i] = z_six(zhong=fu[i])
                elif chord == "jianliu":   #减四六
                    if note == "geng":
                        fu[i] = j_six(fu[i])
                    elif note == "zhong":
                        fu[i] = j_six(zhong=fu[i])
                    elif note == "wu":
                        fu[i] = j_six(zhong=fu[i])
                for x in range(len(fu[i])):
                    if bef == None:
                        yin(fu[i][x],int(pai[i]*pig),unit=tra[x],qi=yue)
                    if bef:
                        yin(fu[i][x],int(pai[i]*pig),bef[i],tra[x],qi=yue)

def myin1(fu,pai,time=120,bef=None,yue=2):   #多声部版
    pig = int(beat(time))
    for i in range(len(pai)):
        if type(pai[i]) == list:
            for j in range(len(pai[i])):
                if bef == None:
                    yin(fu[i][j],pai[i][j]*pig,unit=tra[j],qi=yue)
                elif bef and len(bef) == 1:
                    yin(fu[i][j],pai[i][j]*pig,bef,unit=tra[j],qi=yue)
                else:
                    yin(fu[i][j],pai[i][j]*pig,bef[i][j],unit=tra[j],qi=yue)
        else:
            if bef == None:
                yin(fu[i],pai[i]*pig,qi=yue)
            elif bef and len(bef) == 1:
                yin(fu[i],pai[i]*pig,bef,qi=yue)
            else:
                yin(fu[i],pai[i]*pig,bef[i],qi=yue)

def myin2(fu,pai,time,qian=None,yue=2):   #最老版，单声部
    pig = int(beat(time))                 
    if qian == None:
        x = len(pai)
        for i in range(x):
            yin(fu[i],pai[i]*pig,qi=yue)
    elif qian and len(qian) == 1:
        x = len(pai)
        for i in range(x):
            yin(fu[i],pai[i]*pig,qian,qi=yue)
    else:
        x = len(pai)
        for i in range(x):
            yin(fu[i],pai[i]*pig,qian[i],qi=yue)
                
