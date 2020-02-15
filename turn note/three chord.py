#和弦
#三和弦

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
    if yin_type == "yin":   #若要返回音符
        yin = "" 
        pass                #以后还会做专门一个函数
    

    
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
    if yin_type == "yin":   #若要返回音符
        yin = ""
        pass                #以后还会做专门一个函数
            
#增三和弦
def z_three(geng = None,zhong=None,wu=None,yin_type="num"):
    if geng == None and zhong == None and w_yin == None:
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
        if z_yin and geng == None and wu == None:      #知道中音
            geng = zhong - 4
            wu = zhong + 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
        if w_yin and geng == None and zhong == None:      #知道五音
            zhong = wu - 4
            geng = zhong - 4
            yin.append(geng)
            yin.append(zhong)
            yin.append(wu)
            return yin
    if yin_type == "yin":   #若要返回音符
        yin = ""
        pass                #以后还会做专门一个函数
        
        
        
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
    if yin_type == "yin":   #若要返回音符
        yin = ""
        pass                #以后还会做专门一个函数