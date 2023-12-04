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
    if vd['TC']:
        return vd['TC']
    elif vd['VC'] and vd['FC']:
        return vd['VC'] + vd['FC']
    elif vd['AFC'] and vd['AVC'] and vd['Q']:
        return vd['AFC'] * vd['Q'] + vd['AVC'] * vd['Q']
    elif vd['TR'] and vd['PR']:
        return vd['TR'] - vd['PR']
    elif vd['TR'] and vd['Q'] and vd['ATC'] and vd['P']:
        return vd['TR'] - ((vd['P'] - vd['ATC']) * vd['Q'])
    else:
        return 'Недостаточно данных'

def fFC(vd):
    if vd['FC']:
        return
    elif vd['TC'] and vd['VC']:
        return vd['TC'] - vd['VC']
    elif vd['AFC'] and vd['Q'] and vd['AVC'] and vd['VC']:
        return (vd['AFC'] * vd['Q'] + vd['AVC'] * ['Q']) - vd['VC']
    elif vd['AFC'] and ['Q']:
        return vd['AFC'] * vd['Q']
    elif vd['QCR'] and vd['P'] and vd['AVC']:
        return vd['QCR'] * (vd['P'] - vd['AVC'])
    else:
        return 'Недостаточно данных'
    
def fVC(vd):
    if vd['VC']:
        return vd['VC']
    elif vd['TC'] and vd['FC']:
        return vd['TC'] - vd['FC']
    elif vd['AVC'] and vd['Q']:
        return vd['AVC'] * vd['Q']
    elif vd['AFC'] and vd['Q'] and vd['AVC'] and vd['FC']:
        return (vd['AFC'] * vd['Q'] + vd['AVC'] * vd['Q']) - vd['FC']
    else:
        return 'Недостаточно данных'

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