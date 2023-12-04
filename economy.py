vd = {
    'TC': None,
    'VC': None,
    'FC': None,
    'AFC': None,
    'AVC': None,
    'Q': None,
    'P': None,
    'ATC': None,
    'TR': None,
    'PR': None,
    'AR': None,
    'QCR': None
}

def fTC(vd):
    if vd['TC'] != None:
        return vd['TC']
    elif vd['VC'] and vd['FC'] != None:
        return vd['VC'] + vd['FC']
    elif (vd['AFC'] and vd['AVC'] and vd['Q']) != None:
        return vd['AFC'] * vd['Q'] + vd['AVC'] * vd['Q']
    elif vd['TR'] and vd['PR'] != None:
        return vd['TR'] - vd['PR']
    elif vd['TR'] and vd['Q'] and vd['ATC'] and vd['P']:
        return vd['TR'] - ((vd['P'] - vd['ATC']) * vd['Q'])
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