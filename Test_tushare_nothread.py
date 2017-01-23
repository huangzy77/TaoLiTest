import tushare as ts
import time

ISOTIMEFORMAT='%Y-%m-%d %X'
start=time.clock()
jycb_buy=0.00015
jycb_sell=0.00015
data={'502000':{'M':[],'A':[],'B':[]},\
      '502003':{'M':[],'A':[],'B':[]},\
      '502006':{'M':[],'A':[],'B':[]},\
      '502010':{'M':[],'A':[],'B':[]},\
      '502013':{'M':[],'A':[],'B':[]},\
      '502016':{'M':[],'A':[],'B':[]},\
      '502020':{'M':[],'A':[],'B':[]},\
      '502023':{'M':[],'A':[],'B':[]},\
      '502026':{'M':[],'A':[],'B':[]},\
      '502030':{'M':[],'A':[],'B':[]},\
      '502036':{'M':[],'A':[],'B':[]},\
      '502040':{'M':[],'A':[],'B':[]},\
      '502048':{'M':[],'A':[],'B':[]},\
      '502053':{'M':[],'A':[],'B':[]},\
      '502056':{'M':[],'A':[],'B':[]},\
      }


ts.set_token('6a67ac9bfe7f0f5ca103409a7af4f8002bfb97639b988d4a5e3ab80319f0dc46')

###################got the real time data#######################

def get_000_500dq():
    #502000,500dq
    a_b=1

    tk_502000_M=ts.get_realtime_quotes('502000')
    tk_502000_A=ts.get_realtime_quotes('502001')
    tk_502000_B=ts.get_realtime_quotes('502002')

    try:
        bp1_502000_M=float(tk_502000_M['b1_p'])  #bid_price
        bv1_502000_M=float(tk_502000_M['b1_v'])
        ap1_502000_M=float(tk_502000_M['a1_p'])  #ask_price
        av1_502000_M=float(tk_502000_M['a1_v'])

        bp1_502000_A=float(tk_502000_A['b1_p'])  #bid_price
        bv1_502000_A=float(tk_502000_A['b1_v'])
        ap1_502000_A=float(tk_502000_A['a1_p'])  #ask_price
        av1_502000_A=float(tk_502000_A['a1_v'])

        bp1_502000_B=float(tk_502000_B['b1_p'])  #bid_price
        bv1_502000_B=float(tk_502000_B['b1_v'])
        ap1_502000_B=float(tk_502000_B['a1_p'])  #ask_price
        av1_502000_B=float(tk_502000_B['a1_v'])

        data['502000']['M']=[bp1_502000_M,bv1_502000_M,ap1_502000_M,av1_502000_M]
        data['502000']['A']=[bp1_502000_A,bv1_502000_A,ap1_502000_A,av1_502000_A]
        data['502000']['B']=[bp1_502000_B,bv1_502000_B,ap1_502000_B,av1_502000_B]

        if (ap1_502000_A+ap1_502000_B)*a_b*(1+jycb_buy)<bp1_502000_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502000 hebing Chance,profil:%f" %(bp1_502000_M*2*(1-jycb_sell)-(ap1_502000_A+ap1_502000_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502000_M*2*(1+jycb_buy)<(bp1_502000_A+bp1_502000_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502000 fenchai Chance,profil:%f" %(ap1_502000_M*2*(1+jycb_buy)-(bp1_502000_A+bp1_502000_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502000 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e


def get_003_jqfj():
    #502003,jqfj
    a_b=1

    tk_502003_M=ts.get_realtime_quotes('502003')
    tk_502003_A=ts.get_realtime_quotes('502004')
    tk_502003_B=ts.get_realtime_quotes('502005')

    try:
        bp1_502003_M=float(tk_502003_M['b1_p'])  #bid_price
        bv1_502003_M=float(tk_502003_M['b1_v'])
        ap1_502003_M=float(tk_502003_M['a1_p'])  #ask_price
        av1_502003_M=float(tk_502003_M['a1_v'])

        bp1_502003_A=float(tk_502003_A['b1_p'])  #bid_price
        bv1_502003_A=float(tk_502003_A['b1_v'])
        ap1_502003_A=float(tk_502003_A['a1_p'])  #ask_price
        av1_502003_A=float(tk_502003_A['a1_v'])

        bp1_502003_B=float(tk_502003_B['b1_p'])  #bid_price
        bv1_502003_B=float(tk_502003_B['b1_v'])
        ap1_502003_B=float(tk_502003_B['a1_p'])  #ask_price
        av1_502003_B=float(tk_502003_B['a1_v'])

        data['502003']['M']=[bp1_502003_M,bv1_502003_M,ap1_502003_M,av1_502003_M]
        data['502003']['A']=[bp1_502003_A,bv1_502003_A,ap1_502003_A,av1_502003_A]
        data['502003']['B']=[bp1_502003_B,bv1_502003_B,ap1_502003_B,av1_502003_B]

        if (ap1_502003_A+ap1_502003_B)*a_b*(1+jycb_buy)<bp1_502003_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502003 hebing Chance,profil:%f" %(bp1_502003_M*2*(1-jycb_sell)-(ap1_502003_A+ap1_502003_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502003_M*2*(1+jycb_buy)<(bp1_502003_A+bp1_502003_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502003 fenchai Chance,profil:%f" %(ap1_502003_M*2*(1+jycb_buy)-(bp1_502003_A+bp1_502003_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502003 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def get_006_gqgg():
    #502006,gqgg
    a_b=1

    tk_502006_M=ts.get_realtime_quotes('502006')
    tk_502006_A=ts.get_realtime_quotes('502007')
    tk_502006_B=ts.get_realtime_quotes('502008')

    try:
        bp1_502006_M=float(tk_502006_M['b1_p'])  #bid_price
        bv1_502006_M=float(tk_502006_M['b1_v'])
        ap1_502006_M=float(tk_502006_M['a1_p'])  #ask_price
        av1_502006_M=float(tk_502006_M['a1_v'])

        bp1_502006_A=float(tk_502006_A['b1_p'])  #bid_price
        bv1_502006_A=float(tk_502006_A['b1_v'])
        ap1_502006_A=float(tk_502006_A['a1_p'])  #ask_price
        av1_502006_A=float(tk_502006_A['a1_v'])

        bp1_502006_B=float(tk_502006_B['b1_p'])  #bid_price
        bv1_502006_B=float(tk_502006_B['b1_v'])
        ap1_502006_B=float(tk_502006_B['a1_p'])  #ask_price
        av1_502006_B=float(tk_502006_B['a1_v'])

        data['502006']['M']=[bp1_502006_M,bv1_502006_M,ap1_502006_M,av1_502006_M]
        data['502006']['A']=[bp1_502006_A,bv1_502006_A,ap1_502006_A,av1_502006_A]
        data['502006']['B']=[bp1_502006_B,bv1_502006_B,ap1_502006_B,av1_502006_B]

        if (ap1_502006_A+ap1_502006_B)*a_b*(1+jycb_buy)<bp1_502006_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502006 hebing Chance,profil:%f" %(bp1_502006_M*2*(1-jycb_sell)-(ap1_502006_A+ap1_502006_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502006_M*2*(1+jycb_buy)<(bp1_502006_A+bp1_502006_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502006 fenchai Chance,profil:%f" %(ap1_502006_M*2*(1+jycb_buy)-(bp1_502006_A+bp1_502006_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502006 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def get_010_zqfj():
    #502010,zqfj
    a_b=1

    tk_502010_M=ts.get_realtime_quotes('502010')
    tk_502010_A=ts.get_realtime_quotes('502011')
    tk_502010_B=ts.get_realtime_quotes('502012')

    try:
        bp1_502010_M=float(tk_502010_M['b1_p'])  #bid_price
        bv1_502010_M=float(tk_502010_M['b1_v'])
        ap1_502010_M=float(tk_502010_M['a1_p'])  #ask_price
        av1_502010_M=float(tk_502010_M['a1_v'])

        bp1_502010_A=float(tk_502010_A['b1_p'])  #bid_price
        bv1_502010_A=float(tk_502010_A['b1_v'])
        ap1_502010_A=float(tk_502010_A['a1_p'])  #ask_price
        av1_502010_A=float(tk_502010_A['a1_v'])

        bp1_502010_B=float(tk_502010_B['b1_p'])  #bid_price
        bv1_502010_B=float(tk_502010_B['b1_v'])
        ap1_502010_B=float(tk_502010_B['a1_p'])  #ask_price
        av1_502010_B=float(tk_502010_B['a1_v'])

        data['502010']['M']=[bp1_502010_M,bv1_502010_M,ap1_502010_M,av1_502010_M]
        data['502010']['A']=[bp1_502010_A,bv1_502010_A,ap1_502010_A,av1_502010_A]
        data['502010']['B']=[bp1_502010_B,bv1_502010_B,ap1_502010_B,av1_502010_B]

        if (ap1_502010_A+ap1_502010_B)*a_b*(1+jycb_buy)<bp1_502010_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502010 hebing Chance,profil:%f" %(bp1_502010_M*2*(1-jycb_sell)-(ap1_502010_A+ap1_502010_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502010_M*2*(1+jycb_buy)<(bp1_502010_A+bp1_502010_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502010 fenchai Chance,profil:%f" %(ap1_502010_M*2*(1+jycb_buy)-(bp1_502010_A+bp1_502010_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502010 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def get_013_ydyl():
    #502013,ydyl
    a_b=1

    tk_502013_M=ts.get_realtime_quotes('502013')
    tk_502013_A=ts.get_realtime_quotes('502014')
    tk_502013_B=ts.get_realtime_quotes('502015')

    try:
        bp1_502013_M=float(tk_502013_M['b1_p'])  #bid_price
        bv1_502013_M=float(tk_502013_M['b1_v'])
        ap1_502013_M=float(tk_502013_M['a1_p'])  #ask_price
        av1_502013_M=float(tk_502013_M['a1_v'])

        bp1_502013_A=float(tk_502013_A['b1_p'])  #bid_price
        bv1_502013_A=float(tk_502013_A['b1_v'])
        ap1_502013_A=float(tk_502013_A['a1_p'])  #ask_price
        av1_502013_A=float(tk_502013_A['a1_v'])

        bp1_502013_B=float(tk_502013_B['b1_p'])  #bid_price
        bv1_502013_B=float(tk_502013_B['b1_v'])
        ap1_502013_B=float(tk_502013_B['a1_p'])  #ask_price
        av1_502013_B=float(tk_502013_B['a1_v'])

        data['502013']['M']=[bp1_502013_M,bv1_502013_M,ap1_502013_M,av1_502013_M]
        data['502013']['A']=[bp1_502013_A,bv1_502013_A,ap1_502013_A,av1_502013_A]
        data['502013']['B']=[bp1_502013_B,bv1_502013_B,ap1_502013_B,av1_502013_B]

        if (ap1_502013_A+ap1_502013_B)*a_b*(1+jycb_buy)<bp1_502013_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502013 hebing Chance,profil:%f" %(bp1_502013_M*2*(1-jycb_sell)-(ap1_502013_A+ap1_502013_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502013_M*2*(1+jycb_buy)<(bp1_502013_A+bp1_502013_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502013 fenchai Chance,profil:%f" %(ap1_502013_M*2*(1+jycb_buy)-(bp1_502013_A+bp1_502013_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502013 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def get_016_dlfj():
    #502016,dlfj
    a_b=1

    tk_502016_M=ts.get_realtime_quotes('502016')
    tk_502016_A=ts.get_realtime_quotes('502017')
    tk_502016_B=ts.get_realtime_quotes('502018')

    try:
        bp1_502016_M=float(tk_502016_M['b1_p'])  #bid_price
        bv1_502016_M=float(tk_502016_M['b1_v'])
        ap1_502016_M=float(tk_502016_M['a1_p'])  #ask_price
        av1_502016_M=float(tk_502016_M['a1_v'])

        bp1_502016_A=float(tk_502016_A['b1_p'])  #bid_price
        bv1_502016_A=float(tk_502016_A['b1_v'])
        ap1_502016_A=float(tk_502016_A['a1_p'])  #ask_price
        av1_502016_A=float(tk_502016_A['a1_v'])

        bp1_502016_B=float(tk_502016_B['b1_p'])  #bid_price
        bv1_502016_B=float(tk_502016_B['b1_v'])
        ap1_502016_B=float(tk_502016_B['a1_p'])  #ask_price
        av1_502016_B=float(tk_502016_B['a1_v'])

        data['502016']['M']=[bp1_502016_M,bv1_502016_M,ap1_502016_M,av1_502016_M]
        data['502016']['A']=[bp1_502016_A,bv1_502016_A,ap1_502016_A,av1_502016_A]
        data['502016']['B']=[bp1_502016_B,bv1_502016_B,ap1_502016_B,av1_502016_B]

        if (ap1_502016_A+ap1_502016_B)*a_b*(1+jycb_buy)<bp1_502016_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502016 hebing Chance,profil:%f" %(bp1_502016_M*2*(1-jycb_sell)-(ap1_502016_A+ap1_502016_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502016_M*2*(1+jycb_buy)<(bp1_502016_A+bp1_502016_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502016 fenchai Chance,profil:%f" %(ap1_502016_M*2*(1+jycb_buy)-(bp1_502016_A+bp1_502016_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502016 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def get_020_gj50():
    #502020,gj50
    a_b=1

    tk_502020_M=ts.get_realtime_quotes('502020')
    tk_502020_A=ts.get_realtime_quotes('502021')
    tk_502020_B=ts.get_realtime_quotes('502022')

    try:
        bp1_502020_M=float(tk_502020_M['b1_p'])  #bid_price
        bv1_502020_M=float(tk_502020_M['b1_v'])
        ap1_502020_M=float(tk_502020_M['a1_p'])  #ask_price
        av1_502020_M=float(tk_502020_M['a1_v'])

        bp1_502020_A=float(tk_502020_A['b1_p'])  #bid_price
        bv1_502020_A=float(tk_502020_A['b1_v'])
        ap1_502020_A=float(tk_502020_A['a1_p'])  #ask_price
        av1_502020_A=float(tk_502020_A['a1_v'])

        bp1_502020_B=float(tk_502020_B['b1_p'])  #bid_price
        bv1_502020_B=float(tk_502020_B['b1_v'])
        ap1_502020_B=float(tk_502020_B['a1_p'])  #ask_price
        av1_502020_B=float(tk_502020_B['a1_v'])

        data['502020']['M']=[bp1_502020_M,bv1_502020_M,ap1_502020_M,av1_502020_M]
        data['502020']['A']=[bp1_502020_A,bv1_502020_A,ap1_502020_A,av1_502020_A]
        data['502020']['B']=[bp1_502020_B,bv1_502020_B,ap1_502020_B,av1_502020_B]

        if (ap1_502020_A+ap1_502020_B)*a_b*(1+jycb_buy)<bp1_502020_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502020 hebing Chance,profil:%f" %(bp1_502020_M*2*(1-jycb_sell)-(ap1_502020_A+ap1_502020_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502020_M*2*(1+jycb_buy)<(bp1_502020_A+bp1_502020_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502020 fenchai Chance,profil:%f" %(ap1_502020_M*2*(1+jycb_buy)-(bp1_502020_A+bp1_502020_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502020 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def get_023_qtfj():
    #502023,qtfj
    a_b=1

    tk_502023_M=ts.get_realtime_quotes('502023')
    tk_502023_A=ts.get_realtime_quotes('502024')
    tk_502023_B=ts.get_realtime_quotes('502025')

    try:
        bp1_502023_M=float(tk_502023_M['b1_p'])  #bid_price
        bv1_502023_M=float(tk_502023_M['b1_v'])
        ap1_502023_M=float(tk_502023_M['a1_p'])  #ask_price
        av1_502023_M=float(tk_502023_M['a1_v'])

        bp1_502023_A=float(tk_502023_A['b1_p'])  #bid_price
        bv1_502023_A=float(tk_502023_A['b1_v'])
        ap1_502023_A=float(tk_502023_A['a1_p'])  #ask_price
        av1_502023_A=float(tk_502023_A['a1_v'])

        bp1_502023_B=float(tk_502023_B['b1_p'])  #bid_price
        bv1_502023_B=float(tk_502023_B['b1_v'])
        ap1_502023_B=float(tk_502023_B['a1_p'])  #ask_price
        av1_502023_B=float(tk_502023_B['a1_v'])

        data['502023']['M']=[bp1_502023_M,bv1_502023_M,ap1_502023_M,av1_502023_M]
        data['502023']['A']=[bp1_502023_A,bv1_502023_A,ap1_502023_A,av1_502023_A]
        data['502023']['B']=[bp1_502023_B,bv1_502023_B,ap1_502023_B,av1_502023_B]

        if (ap1_502023_A+ap1_502023_B)*a_b*(1+jycb_buy)<bp1_502023_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502023 hebing Chance,profil:%f" %(bp1_502023_M*2*(1-jycb_sell)-(ap1_502023_A+ap1_502023_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502023_M*2*(1+jycb_buy)<(bp1_502023_A+bp1_502023_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502023 fenchai Chance,profil:%f" %(ap1_502023_M*2*(1+jycb_buy)-(bp1_502023_A+bp1_502023_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502023 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def get_026_xsl():
    #502026,xsl
    a_b=1

    tk_502026_M=ts.get_realtime_quotes('502026')
    tk_502026_A=ts.get_realtime_quotes('502027')
    tk_502026_B=ts.get_realtime_quotes('502028')

    try:
        bp1_502026_M=float(tk_502026_M['b1_p'])  #bid_price
        bv1_502026_M=float(tk_502026_M['b1_v'])
        ap1_502026_M=float(tk_502026_M['a1_p'])  #ask_price
        av1_502026_M=float(tk_502026_M['a1_v'])

        bp1_502026_A=float(tk_502026_A['b1_p'])  #bid_price
        bv1_502026_A=float(tk_502026_A['b1_v'])
        ap1_502026_A=float(tk_502026_A['a1_p'])  #ask_price
        av1_502026_A=float(tk_502026_A['a1_v'])

        bp1_502026_B=float(tk_502026_B['b1_p'])  #bid_price
        bv1_502026_B=float(tk_502026_B['b1_v'])
        ap1_502026_B=float(tk_502026_B['a1_p'])  #ask_price
        av1_502026_B=float(tk_502026_B['a1_v'])

        data['502026']['M']=[bp1_502026_M,bv1_502026_M,ap1_502026_M,av1_502026_M]
        data['502026']['A']=[bp1_502026_A,bv1_502026_A,ap1_502026_A,av1_502026_A]
        data['502026']['B']=[bp1_502026_B,bv1_502026_B,ap1_502026_B,av1_502026_B]

        if (ap1_502026_A+ap1_502026_B)*a_b*(1+jycb_buy)<bp1_502026_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502026 hebing Chance,profil:%f" %(bp1_502026_M*2*(1-jycb_sell)-(ap1_502026_A+ap1_502026_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502026_M*2*(1+jycb_buy)<(bp1_502026_A+bp1_502026_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502026 fenchai Chance,profil:%f" %(ap1_502026_M*2*(1+jycb_buy)-(bp1_502026_A+bp1_502026_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502026 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def get_030_gtfj():
    #502030,gtfj
    a_b=1

    tk_502030_M=ts.get_realtime_quotes('502030')
    tk_502030_A=ts.get_realtime_quotes('502031')
    tk_502030_B=ts.get_realtime_quotes('502032')

    try:
        bp1_502030_M=float(tk_502030_M['b1_p'])  #bid_price
        bv1_502030_M=float(tk_502030_M['b1_v'])
        ap1_502030_M=float(tk_502030_M['a1_p'])  #ask_price
        av1_502030_M=float(tk_502030_M['a1_v'])

        bp1_502030_A=float(tk_502030_A['b1_p'])  #bid_price
        bv1_502030_A=float(tk_502030_A['b1_v'])
        ap1_502030_A=float(tk_502030_A['a1_p'])  #ask_price
        av1_502030_A=float(tk_502030_A['a1_v'])

        bp1_502030_B=float(tk_502030_B['b1_p'])  #bid_price
        bv1_502030_B=float(tk_502030_B['b1_v'])
        ap1_502030_B=float(tk_502030_B['a1_p'])  #ask_price
        av1_502030_B=float(tk_502030_B['a1_v'])

        data['502030']['M']=[bp1_502030_M,bv1_502030_M,ap1_502030_M,av1_502030_M]
        data['502030']['A']=[bp1_502030_A,bv1_502030_A,ap1_502030_A,av1_502030_A]
        data['502030']['B']=[bp1_502030_B,bv1_502030_B,ap1_502030_B,av1_502030_B]

        if (ap1_502030_A+ap1_502030_B)*a_b*(1+jycb_buy)<bp1_502030_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502030 hebing Chance,profil:%f" %(bp1_502030_M*2*(1-jycb_sell)-(ap1_502030_A+ap1_502030_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502030_M*2*(1+jycb_buy)<(bp1_502030_A+bp1_502030_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502030 fenchai Chance,profil:%f" %(ap1_502030_M*2*(1+jycb_buy)-(bp1_502030_A+bp1_502030_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502030 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def get_036_hljr():
    #502036,hljr
    a_b=1

    tk_502036_M=ts.get_realtime_quotes('502036')
    tk_502036_A=ts.get_realtime_quotes('502037')
    tk_502036_B=ts.get_realtime_quotes('502038')

    try:
        bp1_502036_M=float(tk_502036_M['b1_p'])  #bid_price
        bv1_502036_M=float(tk_502036_M['b1_v'])
        ap1_502036_M=float(tk_502036_M['a1_p'])  #ask_price
        av1_502036_M=float(tk_502036_M['a1_v'])

        bp1_502036_A=float(tk_502036_A['b1_p'])  #bid_price
        bv1_502036_A=float(tk_502036_A['b1_v'])
        ap1_502036_A=float(tk_502036_A['a1_p'])  #ask_price
        av1_502036_A=float(tk_502036_A['a1_v'])

        bp1_502036_B=float(tk_502036_B['b1_p'])  #bid_price
        bv1_502036_B=float(tk_502036_B['b1_v'])
        ap1_502036_B=float(tk_502036_B['a1_p'])  #ask_price
        av1_502036_B=float(tk_502036_B['a1_v'])

        data['502036']['M']=[bp1_502036_M,bv1_502036_M,ap1_502036_M,av1_502036_M]
        data['502036']['A']=[bp1_502036_A,bv1_502036_A,ap1_502036_A,av1_502036_A]
        data['502036']['B']=[bp1_502036_B,bv1_502036_B,ap1_502036_B,av1_502036_B]

        if (ap1_502036_A+ap1_502036_B)*a_b*(1+jycb_buy)<bp1_502036_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502036 hebing Chance,profil:%f" %(bp1_502036_M*2*(1-jycb_sell)-(ap1_502036_A+ap1_502036_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502036_M*2*(1+jycb_buy)<(bp1_502036_A+bp1_502036_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502036 fenchai Chance,profil:%f" %(ap1_502036_M*2*(1+jycb_buy)-(bp1_502036_A+bp1_502036_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502036 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def get_040_s50():
    #502040,s50
    a_b=1

    tk_502040_M=ts.get_realtime_quotes('502040')
    tk_502040_A=ts.get_realtime_quotes('502041')
    tk_502040_B=ts.get_realtime_quotes('502042')

    try:
        bp1_502040_M=float(tk_502040_M['b1_p'])  #bid_price
        bv1_502040_M=float(tk_502040_M['b1_v'])
        ap1_502040_M=float(tk_502040_M['a1_p'])  #ask_price
        av1_502040_M=float(tk_502040_M['a1_v'])

        bp1_502040_A=float(tk_502040_A['b1_p'])  #bid_price
        bv1_502040_A=float(tk_502040_A['b1_v'])
        ap1_502040_A=float(tk_502040_A['a1_p'])  #ask_price
        av1_502040_A=float(tk_502040_A['a1_v'])

        bp1_502040_B=float(tk_502040_B['b1_p'])  #bid_price
        bv1_502040_B=float(tk_502040_B['b1_v'])
        ap1_502040_B=float(tk_502040_B['a1_p'])  #ask_price
        av1_502040_B=float(tk_502040_B['a1_v'])

        data['502040']['M']=[bp1_502040_M,bv1_502040_M,ap1_502040_M,av1_502040_M]
        data['502040']['A']=[bp1_502040_A,bv1_502040_A,ap1_502040_A,av1_502040_A]
        data['502040']['B']=[bp1_502040_B,bv1_502040_B,ap1_502040_B,av1_502040_B]

        if (ap1_502040_A+ap1_502040_B)*a_b*(1+jycb_buy)<bp1_502040_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502040 hebing Chance,profil:%f" %(bp1_502040_M*2*(1-jycb_sell)-(ap1_502040_A+ap1_502040_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502040_M*2*(1+jycb_buy)<(bp1_502040_A+bp1_502040_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502040 fenchai Chance,profil:%f" %(ap1_502040_M*2*(1+jycb_buy)-(bp1_502040_A+bp1_502040_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502040 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def get_048_50fj():
    #502048,50fj
    a_b=1

    tk_502048_M=ts.get_realtime_quotes('502048')
    tk_502048_A=ts.get_realtime_quotes('502049')
    tk_502048_B=ts.get_realtime_quotes('502050')

    try:
        bp1_502048_M=float(tk_502048_M['b1_p'])  #bid_price
        bv1_502048_M=float(tk_502048_M['b1_v'])
        ap1_502048_M=float(tk_502048_M['a1_p'])  #ask_price
        av1_502048_M=float(tk_502048_M['a1_v'])

        bp1_502048_A=float(tk_502048_A['b1_p'])  #bid_price
        bv1_502048_A=float(tk_502048_A['b1_v'])
        ap1_502048_A=float(tk_502048_A['a1_p'])  #ask_price
        av1_502048_A=float(tk_502048_A['a1_v'])

        bp1_502048_B=float(tk_502048_B['b1_p'])  #bid_price
        bv1_502048_B=float(tk_502048_B['b1_v'])
        ap1_502048_B=float(tk_502048_B['a1_p'])  #ask_price
        av1_502048_B=float(tk_502048_B['a1_v'])

        data['502048']['M']=[bp1_502048_M,bv1_502048_M,ap1_502048_M,av1_502048_M]
        data['502048']['A']=[bp1_502048_A,bv1_502048_A,ap1_502048_A,av1_502048_A]
        data['502048']['B']=[bp1_502048_B,bv1_502048_B,ap1_502048_B,av1_502048_B]

        if (ap1_502048_A+ap1_502048_B)*a_b*(1+jycb_buy)<bp1_502048_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502048 hebing Chance,profil:%f" %(bp1_502048_M*2*(1-jycb_sell)-(ap1_502048_A+ap1_502048_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502048_M*2*(1+jycb_buy)<(bp1_502048_A+bp1_502048_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502048 fenchai Chance,profil:%f" %(ap1_502048_M*2*(1+jycb_buy)-(bp1_502048_A+bp1_502048_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502048 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def get_053_qsfj():
    #502053,qsfj
    a_b=1

    tk_502053_M=ts.get_realtime_quotes('502053')
    tk_502053_A=ts.get_realtime_quotes('502054')
    tk_502053_B=ts.get_realtime_quotes('502055')

    try:
        bp1_502053_M=float(tk_502053_M['b1_p'])  #bid_price
        bv1_502053_M=float(tk_502053_M['b1_v'])
        ap1_502053_M=float(tk_502053_M['a1_p'])  #ask_price
        av1_502053_M=float(tk_502053_M['a1_v'])

        bp1_502053_A=float(tk_502053_A['b1_p'])  #bid_price
        bv1_502053_A=float(tk_502053_A['b1_v'])
        ap1_502053_A=float(tk_502053_A['a1_p'])  #ask_price
        av1_502053_A=float(tk_502053_A['a1_v'])

        bp1_502053_B=float(tk_502053_B['b1_p'])  #bid_price
        bv1_502053_B=float(tk_502053_B['b1_v'])
        ap1_502053_B=float(tk_502053_B['a1_p'])  #ask_price
        av1_502053_B=float(tk_502053_B['a1_v'])

        data['502053']['M']=[bp1_502053_M,bv1_502053_M,ap1_502053_M,av1_502053_M]
        data['502053']['A']=[bp1_502053_A,bv1_502053_A,ap1_502053_A,av1_502053_A]
        data['502053']['B']=[bp1_502053_B,bv1_502053_B,ap1_502053_B,av1_502053_B]

        if (ap1_502053_A+ap1_502053_B)*a_b*(1+jycb_buy)<bp1_502053_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502053 hebing Chance,profil:%f" %(bp1_502053_M*2*(1-jycb_sell)-(ap1_502053_A+ap1_502053_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502053_M*2*(1+jycb_buy)<(bp1_502053_A+bp1_502053_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502053 fenchai Chance,profil:%f" %(ap1_502053_M*2*(1+jycb_buy)-(bp1_502053_A+bp1_502053_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502053 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def get_056_ylfj():
    #502056,ylfj
    a_b=1

    tk_502056_M=ts.get_realtime_quotes('502056')
    tk_502056_A=ts.get_realtime_quotes('502057')
    tk_502056_B=ts.get_realtime_quotes('502058')

    try:
        bp1_502056_M=float(tk_502056_M['b1_p'])  #bid_price
        bv1_502056_M=float(tk_502056_M['b1_v'])
        ap1_502056_M=float(tk_502056_M['a1_p'])  #ask_price
        av1_502056_M=float(tk_502056_M['a1_v'])

        bp1_502056_A=float(tk_502056_A['b1_p'])  #bid_price
        bv1_502056_A=float(tk_502056_A['b1_v'])
        ap1_502056_A=float(tk_502056_A['a1_p'])  #ask_price
        av1_502056_A=float(tk_502056_A['a1_v'])

        bp1_502056_B=float(tk_502056_B['b1_p'])  #bid_price
        bv1_502056_B=float(tk_502056_B['b1_v'])
        ap1_502056_B=float(tk_502056_B['a1_p'])  #ask_price
        av1_502056_B=float(tk_502056_B['a1_v'])

        data['502056']['M']=[bp1_502056_M,bv1_502056_M,ap1_502056_M,av1_502056_M]
        data['502056']['A']=[bp1_502056_A,bv1_502056_A,ap1_502056_A,av1_502056_A]
        data['502056']['B']=[bp1_502056_B,bv1_502056_B,ap1_502056_B,av1_502056_B]

        if (ap1_502056_A+ap1_502056_B)*a_b*(1+jycb_buy)<bp1_502056_M*2*(1-jycb_sell):
            stime1=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_hebing=stime1+" 502056 hebing Chance,profil:%f" %(bp1_502056_M*2*(1-jycb_sell)-(ap1_502056_A+ap1_502056_B))*(1+jycb_buy)
            print s_hebing
            WriteInFile(s_hebing)

        elif ap1_502056_M*2*(1+jycb_buy)<(bp1_502056_A+bp1_502056_B)*a_b*(1-jycb_sell):
            stime2=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_fenchai=stime2+" 502056 fenchai Chance,profil:%f" %(ap1_502056_M*2*(1+jycb_buy)-(bp1_502056_A+bp1_502056_B))*(1-jycb_sell)
            print s_fenchai
            WriteInFile(s_fenchai)
        else:
            stime3=time.strftime(ISOTIMEFORMAT,time.localtime())
            s_nochance=stime3+' 502056 No chance!'
            print s_nochance
    except Exception,e:
        print Exception,':',e

def WriteInFile(s):
    target=open('20160413.txt','a')
    s=s+'\n'
    target.write(s)
    target.close()


if __name__ == '__main__':
    i=0
    while True:
        try:
            get_000_500dq()
            get_003_jqfj()
            get_006_gqgg()
            get_010_zqfj()
            get_013_ydyl()
            get_016_dlfj()
            get_020_gj50()
            get_023_qtfj()
            get_026_xsl()
            get_030_gtfj()
            get_036_hljr()
            get_040_s50()
            get_048_50fj()
            get_053_qsfj()
            get_056_ylfj()
        except Exception,e:
            print Exception,':',e
        i+=1
    end=time.clock()









