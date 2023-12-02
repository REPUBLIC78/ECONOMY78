#Формулы
# TC = VC + FC
#    = AFC * Q + AVC * Q
#    = TR - ((P - ATC) * Q)
#    = TR - PR

TC = None
VC = 20
FC = 40
AFC = None
AVC = None
Q = None
P = None
ATC = None
TR = None
PR = None

def fTC(VC, FC, AFC, AVC, Q, P, ATC, TR, PR):
    if TC != None:
        return
    elif VC and FC != None:
        return VC + FC
    elif (AFC and AVC and Q) != None:
        return AFC * Q + AVC * Q
    elif TR and PR != None:
        return TR - PR
    elif TR and Q and ATC and P:
        return TR - ((P - ATC) * Q)
    else:
        return 'Недостаточно данных'