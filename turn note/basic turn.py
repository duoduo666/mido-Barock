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

def c_jiang(yin):                 #重降 bb
    if type(yin) == str:
        return num(yin) - 2
    else:
        return yin - 2