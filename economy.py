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

vl = list(vd)

def findA(vd):
    vd2 = vd
    while True:
        for i in range(len(vd)):
            if vl[i] == 'TC':
                vd2[vl[i]] = fTC(vd)
            if vl[i] == 'VC':
                vd2[vl[i]] = fVC(vd)
            if vl[i] == 'FC':
                vd2[vl[i]] = fFC(vd)
            if vl[i] == 'AFC':
                vd2[vl[i]] = fAFC(vd)
            if vl[i] == 'AVC':
                vd2[vl[i]] = fAVC(vd)
            if vl[i] == 'Q':
                vd2[vl[i]] = fQ(vd)
            if vl[i] == 'P':
                vd2[vl[i]] = fP(vd)
            if vl[i] == 'ATC':
                vd2[vl[i]] = fATC(vd)
            if vl[i] == 'TR':
                vd2[vl[i]] = fTR(vd)
            if vl[i] == 'PR':
                vd2[vl[i]] = fPR(vd)
            if vl[i] == 'AR':
                vd2[vl[i]] = fAR(vd)
            if vl[i] == 'QCR':
                vd2[vl[i]] = fQCR(vd)
        if vd != vd2:
            vd = vd2
            continue
        else:
            return vd2

            

def fTC(vd):
    if vd['TC'] != None:
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
    if vd['FC'] != None:
        return vd['FC']
    elif vd['TC'] and vd['VC']:
        return vd['TC'] - vd['VC']
    elif vd['AFC'] and vd['Q'] and vd['AVC'] and vd['VC']:
        return (vd['AFC'] * vd['Q'] + vd['AVC'] * vd['Q']) - vd['VC']
    elif vd['AFC'] and ['Q']:
        return vd['AFC'] * vd['Q']
    elif vd['QCR'] and vd['P'] and vd['AVC']:
        return vd['QCR'] * (vd['P'] - vd['AVC'])
    else:
        return 'Недостаточно данных'

def fVC(vd):
    if vd['VC'] != None:
        return vd['VC']
    elif vd['TC'] and vd['FC']:
        return vd['TC'] - vd['FC']
    elif vd['AVC'] and vd['Q']:
        return vd['AVC'] * vd['Q']
    elif vd['AFC'] and vd['Q'] and vd['AVC'] and vd['FC']:
        return (vd['AFC'] * vd['Q'] + vd['AVC'] * vd['Q']) - vd['FC']
    else:
        return 'Недостаточно данных'

def fAFC(vd):
    if vd['AFC'] != None:
        return vd['AFC']

def fAVC(vd):
    if vd['AVC']!= None:
        return vd['AVC']

def fQ(vd):
    if vd['Q']!= None:
        return vd['Q']

def fP(vd):
    if vd['P']!= None:
        return vd['P']

def fATC(vd):
    if vd['ATC']!= None:
        return vd['ATC']

def fTR(vd):
    if vd['TR']!= None:
        return vd['TR']

def fPR(vd):
    if vd['PR']!= None:
        return vd['PR']

def fAR(vd):
    if vd['AR']!= None:
        return vd['AR']

def fQCR(vd):
    if vd['QCR']!= None:
        return vd['QCR']