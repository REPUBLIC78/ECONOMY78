from economy import findA, round_array

vd = {
    'TC': None,
    'VC': 64,
    'FC': 36,
    'AFC': None,
    'AVC': None,
    'Q': 6,
    'P': None,
    'ATC': None,
    'TR': None,
    'PR': 5,
    'AR': None,
    'QCR': None
}

tl = []
for i in range(31):
    tl.append(i)
tl.insert(0, None)

print(round_array(findA(vd)))

def test():
    pass