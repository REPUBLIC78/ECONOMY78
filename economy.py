vd = {
    'TC': None,
    'FC': None,
    'VC': None,
    'Q': None,
    'P': None,
    'AFC': None,
    'AVC': None,
    'ATC': None,
    'TR': None,
    'AR': None,
    'PR': None,
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

            
#TC = VC + FC 
#TC = AFC * Q + AVC * Q
#TC = TR - ((P - ATC) * Q)
#TC = TR - Pr
#TC = ATC * Q
def fTC(vd):
    if vd['TC'] != None:
        return vd['TC']
    elif None not in [vd['VC'], vd['FC']]:
        return vd['VC'] + vd['FC']
    elif None not in [vd['AFC'], vd['AVC'], vd['Q']]:
        return vd['AFC'] * vd['Q'] + vd['AVC'] * vd['Q']
    elif None not in [vd['TR'], vd['PR']]:
        return vd['TR'] - vd['PR']
    elif None not in [vd['TR'], vd['Q'], vd['ATC'], vd['P']]:
        return vd['TR'] - ((vd['P'] - vd['ATC']) * vd['Q'])
    elif None not in [vd['ATC'], vd['Q']]:
        return vd['ATC'] * vd['Q']
    else:
        return None

#FC = TC - VC
#FC = (AFC * Q + AVC * Q) - VC
#FC = AFC * Q
#FC = Qcr * (P - AVC)
def fFC(vd):
    if vd['FC'] != None:
        return vd['FC']
    elif None not in [vd['TC'], vd['VC']]:
        return vd['TC'] - vd['VC']
    elif None not in [vd['AFC'], vd['Q'], vd['AVC'], vd['VC']]:
        return (vd['AFC'] * vd['Q'] + vd['AVC'] * vd['Q']) - vd['VC']
    elif None not in [vd['AFC'], ['Q']]:
        return vd['AFC'] * vd['Q']
    elif None not in [vd['QCR'], vd['P'], vd['AVC']]:
        return vd['QCR'] * (vd['P'] - vd['AVC'])
    else:
        return None

#VC = TC - FC
#VC = AVC * Q
#VC = (AFC * Q + AVC * Q) - FC
def fVC(vd):
    if vd['VC'] != None:
        return vd['VC']
    elif None not in [vd['TC'], vd['FC']]:
        return vd['TC'] - vd['FC']
    elif None not in [vd['AVC'], vd['Q']]:
        return vd['AVC'] * vd['Q']
    elif None not in [vd['AFC'], vd['Q'], vd['AVC'], vd['FC']]:
        return (vd['AFC'] * vd['Q'] + vd['AVC'] * vd['Q']) - vd['FC']
    else:
        return None

# AFC = (TC - (AVC * Q)) / Q
# AFC = FC / Q
# AFC = ATC - AVC
def fAFC(vd):
    if vd['AFC'] != None:
        return vd['AFC']
    elif None not in [vd['TC'], vd['AVC'], vd['Q']]:
        return (vd['TC'] - (vd['AVC'] * vd['Q'])) / (vd['Q'])
    elif None not in [vd['FC'], vd['Q']]:
        return vd['FC'] / vd['Q']
    elif None not in [vd['ATC'], vd['AVC']]:
        return (vd['ATC'] - vd['AVC'])
    else:
        return None

# AVC = VC / Q
# AVC = ATC - AFC
# AVC = P - (FC / QCR)
# AVC = (TC - (AFC / Q)) / Q
def fAVC(vd):
    if vd['AVC']!= None:
        return vd['AVC']
    elif None not in [vd['VC'], vd['Q']]:
        return vd['VC'] / vd['Q']
    elif None not in [vd['ATC'], vd['AFC']]:
        return vd['ATC'] - vd['AFC']
    elif None not in [vd['P'], vd['FC'], vd['QCR']]:
        return vd['P'] - (vd['FC'] / vd['QCR'])
    elif None not in [vd['TC'], vd['AFC'], vd['Q']]:
        return (vd['TC'] - (vd['AFC'] / vd['Q'])) / vd['Q']
    else:
        return None

def fQ(vd):
    if vd['Q']!= None:
        return vd['Q']

def fP(vd):
    if vd['P']!= None:
        return vd['P']
    if vd['AR']!= None:
        return vd['AR']

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
    if vd['P']!= None:
        return vd['P']

def fQCR(vd):
    if vd['QCR']!= None:
        return vd['QCR']