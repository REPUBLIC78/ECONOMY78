TC = None
VC = None
FC = None
AFC = None
AVC = None
Q = None
P = None
ATC = None
TR = None
PR = None
AR = None
QCR = None

def fTC(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR):
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

def fFC(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR):
    if FC != None:
        return
    elif TC and VC != 0:
        return TC - VC
    elif (AFC and Q and AVC and VC) != 0:
        return (AFC * Q + AVC * Q) - VC
    elif AFC and Q != 0:
        return AFC * Q
    elif (QCR and P and AVC) != 0:
        return QCR * (P - AVC)
    
def fVC(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR):
    if VC != 0:
        return
    elif TC and FC != 0:
        return TC - FC
    elif AVC and Q != 0:
        return AVC * Q
    elif (AFC and Q and AVC and FC) != 0:
        return (AFC * Q + AVC * Q) - FC

def fAFC(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR):
    pass

def fAVC(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR):
    pass

def fQ(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR):
    if Q != 0:
        return

def fP(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR):
    pass

def fATC(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR):
    pass

def fTR(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR):
    pass

def fPR(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR):
    pass

def fAR(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR):
    pass

def fQCR(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR):
    pass