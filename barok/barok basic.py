def dao(yin):                 #计算倒影
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
    for i in range(len(xuanlu)):
        if type(xuanlu[i]) == str:
            xuanlu[i] = num(xuanlu[i])
    if type(base) == str:
        base = num(base)
    xuanlu = dao(xuanlu)
    high = base - xuanlu[0]
    for i in range(len(xuanlu)):
        xuanlu[i] += high
    return xuanlu

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

