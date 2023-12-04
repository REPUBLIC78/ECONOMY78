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

def Cliсked():
    if TCtxt.get() != '':vd['TC'] = int(TCtxt.get())
    else:vd['TC'] = None
    if VCtxt.get() != '':vd['VC'] = int(VCtxt.get())
    else:vd['VC'] = None
    if FCtxt.get() != '':vd['FC'] = int(FCtxt.get())
    else:vd['FC'] = None
    if AFCtxt.get() != '':vd['AFC'] = int(AFCtxt.get())
    else:vd['AFC'] = None
    if AVCtxt.get() != '':vd['AVC'] = int(AVCtxt.get())
    else:vd['AVC'] = None
    if Qtxt.get() != '':vd['Q'] = int(Qtxt.get())
    else:vd['Q'] = None
    if Ptxt.get() != '':vd['P'] = int(Ptxt.get())
    else:vd['P'] = None
    if ATCtxt.get() != '':vd['ATC'] = int(ATCtxt.get())
    else:vd['ATC'] = None
    if TRtxt.get() != '':vd['TR'] = int(TRtxt.get())
    else:vd['TR'] = None
    if PRtxt.get() != '':vd['PR'] = int(PRtxt.get())
    else:vd['PR'] = None
    if ARtxt.get() != '':vd['AR'] = int(PRtxt.get())
    else:vd['AR'] = None
    if QCRtxt.get() != '':vd['QCR'] = int(PRtxt.get())
    else:vd['QCR'] = None
    if fTC(vd) == 'Недостаточно данных':
        ANSlbl.configure(text='Н/д')
    else:
        ANSlbl.configure(text=f'TC = {fTC(vd)}')

window = Tk()
window.title('Рассчёт TC')
window.geometry('640x360')
window.minsize(500,300)
window.maxsize(640,360)

for c in range(12): window.columnconfigure(index=c, weight=1)
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
btn.grid(column=5, row=2, columnspan=2)

ANSlbl = Label(window, text='TC = ', font=('Arial Bold', 14))
ANSlbl.grid(column=5, row=3, columnspan=2)

window.mainloop()