from economy import findA
from itertools import permutations

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

tl = []
for i in range(31):
    tl.append(i)
tl.insert(0, None)

print(tl)

def test():
    pass