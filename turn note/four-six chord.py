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