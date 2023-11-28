#Формулы
# TC = Vc + Fc
#    = AFc * Q + AVc * Q
#    = TR - ((P - ATc) * Q)
#    = TR - PR
TC = None
Vc = 20
Fc = 40
AFc = None
AVc = None
Q = None
P = None
ATc = None
TR = None
PR = None

def fTC(Vc, Fc, AFc, AVc, Q, P, ATc, TR, PR):
    if TC != None:
        return
    elif Vc and Fc != None:
        return Vc + Fc
    elif (AFc and AVc and Q) != None:
        return AFc * Q + AVc * Q
    elif TR and PR != None:
        return TR - PR
    elif TR and Q and ATc and P:
        return TR - ((P - ATc) * Q)
    else:
        return 'Недостаточно данных'