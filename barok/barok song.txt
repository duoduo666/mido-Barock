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
    myin(qian,qiantime,track=track2)
    myin(qiandiba,qiantime,track=track2)
    myin(qiantiwu,qiantime,track=track2)
    myin(qiandiwu,qiantime,track=track2)
    
    myin(qian,qiantime,track=track3)
    myin(qiandiba,qiantime,track=track3)
    myin(qiantiwu,qiantime,track=track3)
    myin(qiandiwu,qiantime,track=track3)
    myin(qiandao1,qiantime,track=track3)
    myin(qiandao2,qiantime,track=track3)
    #一声部
    myin(qian,qiantime)
    myin(qiandiba,qiantime)
    myin(qiantiwu,qiantime)
    myin(qiandiwu,qiantime)
    
    myin(qiandao1,qiantime,du="chunwu",note="high")
    myin(qiandao2,qiantime,du="daliu",note="high")
    myin(qiandao3,qiantime,chord="dasan",note="wu")
    myin(qiandao4,qiantime,chord="dasi",note="zhong")
    
    #二声部
    myin(qiantier,qiantime,track=track2)
    myin(hou,houtime,track=track2)
    myin(qiantier,qiantime,track=track3)
    myin(hou,houtime,track=track3)
    myin(qiandao5,qiantime,track=track3)
    myin(qiandao6,qiantime,track=track3)
    
    #返回一声部
    myin(qiantier,qiantime)
    myin(hou,houtime)
    
    
    #倒影
    myin(qiandao5,qiantime,du="chunwu",note="high")
    myin(qiandao6,qiantime,du="dasan",note="high")
    myin(qiandao7,qiantime,chord="xiaosan",note="wu")
    myin(qiandao8,qiantime,chord="dasi",note="zhong")
    
    
    #二声部
    myin(qian,qiantime,track=track4) #先重复，占第二声部的位
    myin(hou,houtime,track=track4)
    myin(houdiba,houtime,track=track4)
    myin(houtiwu,houtime,track=track4)
    
    myin(qiandao1,qiantime,track=track4)
    myin(qiandao2,qiantime,track=track4)
    myin(qiandao3,qiantime,track=track4)
    myin(qiandao4,qiantime,track=track4)

    myin(houzhong,houtime,track=track4)

    
  
    xxxx = [0.5,0.5,0.5]
    lastyin = [b_three(".do"),b_three(".mi"),b_three(".so"),b_three("do"),b_three("mi"),b_three("so"),'so','mi','do',"do","si"]
    lastpai = [xxxx,xxxx,xxxx,xxxx,xxxx,xxxx,0.5,0.5,1.5,5]
    myin(lastyin,lastpai)
    myin(["do"],[10],high=120)