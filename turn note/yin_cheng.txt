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