from tkinter import *
from tkinter import ttk
from economy import fTC

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
cl = []

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

def Cliсked():
    if TCtxt.get() != '':TC = int(TCtxt.get())
    else:TC = None
    if VCtxt.get() != '':VC = int(VCtxt.get())
    else:VC = None
    if FCtxt.get() != '':FC = int(FCtxt.get())
    else:FC = None
    if AFCtxt.get() != '':AFC = int(AFCtxt.get())
    else:AFC = None
    if AVCtxt.get() != '':AVC = int(AVCtxt.get())
    else:AVC = None
    if Qtxt.get() != '':Q = int(Qtxt.get())
    else:Q = None
    if Ptxt.get() != '':P = int(Ptxt.get())
    else:P = None
    if ATCtxt.get() != '':ATC = int(ATCtxt.get())
    else:ATC = None
    if TRtxt.get() != '':TR = int(TRtxt.get())
    else:TR = None
    if PRtxt.get() != '':PR = int(PRtxt.get())
    else:PR = None
    if ARtxt.get() != '':AR = int(PRtxt.get())
    else:AR = None
    if QCRtxt.get() != '':QCR = int(PRtxt.get())
    else:QCR = None
    if fTC(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR) == 'Недостаточно данных':
        ANSlbl.configure(text='Н/д')
    else:
        ANSlbl.configure(text=f'TC = {fTC(TC, VC, FC, AFC, AVC, Q, P, ATC, TR, PR, AR, QCR)}')

window = Tk()
window.title('Рассчёт TC')
window.geometry('640x360')
window.minsize(500,300)
window.maxsize(640,360)

for c in range(9): window.columnconfigure(index=c, weight=1)
for r in range(4): window.rowconfigure(index=r, weight=1)

for i in range(12): cl.append(Label(window, text=vl[i], font=('Arial Bold', 14)))
for i in range(12): cl[i].grid(column=i, row=0)

TCtxt = Entry(window, width=6)
TCtxt.grid(column=0, row=1)

VCtxt = Entry(window, width=6)
VCtxt.grid(column=1, row=1)

FCtxt = Entry(window, width=6)
FCtxt.grid(column=2, row=1)

AFCtxt = Entry(window, width=6)
AFCtxt.grid(column=3, row=1)

AVCtxt = Entry(window, width=6)
AVCtxt.grid(column=4, row=1)

Qtxt = Entry(window, width=6)
Qtxt.grid(column=5, row=1)

Ptxt = Entry(window, width=6)
Ptxt.grid(column=6, row=1)

ATCtxt = Entry(window, width=6)
ATCtxt.grid(column=7, row=1)

TRtxt = Entry(window, width=6)
TRtxt.grid(column=8, row=1)

PRtxt = Entry(window, width=6)
PRtxt.grid(column=9, row=1)

ARtxt = Entry(window, width=6)
ARtxt.grid(column=10, row=1)

QCRtxt = Entry(window, width=6)
QCRtxt.grid(column=11, row=1)

btn = Button(window, text='Рассчитать', command=Cliсked, width=8)
btn.grid(column=5, row=2)

ANSlbl = Label(window, text='TC = ', font=('Arial Bold', 14))
ANSlbl.grid(column=5, row=3)

window.mainloop()