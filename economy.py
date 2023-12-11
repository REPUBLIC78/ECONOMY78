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
            return round_array(vd2)

def round_array(vd2):
    vd_return = []
    for i in vd2:
        if i != None:
            vd_return.append(round(i, 2))
        else:
            vd_return.append(i)
    return vd_return
            
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

# Q = TC / (AFC + AVC)
# Q = (TR - TC) / (P - ATC)
# Q = PR / (P - ATC)
# Q = TC / ATC
# Q = (FC + VC) / (AFC + AVC)
# Q = FC / AFC
# Q = VC / AVC
# Q = TR / P
# Q = TR / AR

def fQ(vd):
    if vd['Q']!= None:
        return vd['Q']
    elif None not in [vd['Q'], vd['AFC'], vd['AVC']]:
        return vd['TC'] / (vd['AFC'] + vd['AVC'])
    elif None not in [vd['TC'], vd['TR'], vd['P'], vd['ATC']]:
        return (vd['TR'] - vd['TC']) / (vd['P'] - vd['ATC'])
    elif None not in [vd['PR'], vd['P'], vd['ATC']]:
        return (vd['PR'] / (vd['P'] - vd['ATC']))
    elif None not in [vd['TC'], vd['ATC']]:
        return (vd['TC'] / vd['ATC'])
    elif None not in [vd['FC'], vd['VC'], vd['AFC'], vd['AVC']]:
        return (vd['FC'] + vd['VC']) / (vd['AFC'] + vd['AVC'])
    elif None not in [vd['FC'], vd['AFC']]:
        return (vd['FC'] / vd['AFC'])
    elif None not in [vd['VC'], vd['AVC']]:
        return (vd['VC'] / vd['AVC'])
    elif None not in [vd['TR'], vd['P']]:
        return (vd['TR'] / vd['P'])
    elif None not in [vd['TR'], vd['AR']]:
        return (vd['TR'] / vd['AR'])
    else:
        return None

# P = AR
# P = TR / Q
# P = (FC / QCR) + AVC
# P = (PR / Q) + ATC

def fP(vd):
    if vd['P']!= None:
        return vd['P']
    if vd['AR']!= None:
        return vd['AR']
    elif None not in [vd['TR'], vd['Q']]:
        return (vd['TR'] / vd['Q'])
    elif None not in [vd['FC'], vd['QCR'], vd['AVC']]:
        return (vd['FC'] / vd['QCR']) + vd['AVC']
    elif None not in [vd['PR'], vd['Q'], vd['ATC']]:
        return ((vd['PR'] / vd['Q']) + vd['ATC'])
    else:
        return None

# ATC = AFC + AVC
# ATC = P - (PR / Q)
# ATC = TC / Q

def fATC(vd):
    if vd['ATC']!= None:
        return vd['ATC']
    elif None not in [vd['AFC'], vd['AVC']]:
        return (vd['AFC'] + vd['AVC'])
    elif None not in [vd['P'], vd['PR'], vd['Q']]:
        return (vd['P'] - (vd['PR'] / vd['Q']))
    elif None not in [vd['TC'], vd['Q']]:
        return (vd['TC'] / vd['Q'])
    else:
        return None
    
# TR = Q * P
# TR = AR * Q
# TR = TC + PR

def fTR(vd):
    if vd['TR']!= None:
        return vd['TR']
    elif None not in [vd['Q'], vd['P']]:
        return (vd['P'] * vd['Q'])
    elif None not in [vd['AR'], vd['Q']]:
        return (vd['AR'] * vd['Q'])
    elif None not in [vd['TC'], vd['PR']]:
        return (vd['TC'] + vd['PR'])
    else:
        return None

# Pr = TR - TC
# Pr = (P - ATC) * Q

def fPR(vd):
    if vd['PR']!= None:
        return vd['PR']
    elif None not in [vd['TC'], vd['TR']]:
        return (vd['TR'] - vd['TC'])
    elif None not in [vd['P'], vd['ATC'], vd['Q']]:
        return (vd['P'] - vd['ATC'] * vd['Q'])
    else:
        return None

# AR = P
# AR = TR / Q
# AR = (FC / QCR) + AVC
# AR = (PR / Q) + ATC

def fAR(vd):
    if vd['AR']!= None:
        return vd['AR']
    if vd['P']!= None:
        return vd['P']
    elif None not in [vd['TR'], vd['Q']]:
        return (vd['TR'] / vd['Q'])
    elif None not in [vd['FC'], vd['QCR'], vd['AVC']]:
        return (vd['FC'] / vd['QCR']) + vd['AVC']
    elif None not in [vd['PR'], vd['Q'], vd['ATC']]:
        return ((vd['PR'] / vd['Q']) + vd['ATC'])
    else:
        return None

# Qcr = FC/(P - AVC)

def fQCR(vd):
    if vd['QCR']!= None:
        return vd['QCR']
    elif None not in [vd['FC'], vd['P'], vd['AVC']]:
        return (vd['FC'] / (vd['P'] - vd['AVC']))
    else:
        return None