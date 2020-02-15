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
            geng = zhog-4
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