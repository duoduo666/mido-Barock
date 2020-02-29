import mido
from mido import Message, MidiFile, MidiTrack
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

def yin(yin,pai,qian=0,unit=track,tong=0,liang=64,qi=2):              #yin是指哪个音，pai是指时间（节拍），qian是noteon里的time，liang是指音量，tong是通道，
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
                
