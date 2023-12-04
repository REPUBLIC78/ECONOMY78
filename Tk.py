from tkinter import *
from tkinter import ttk
from economy import fTC

vl = ['TC', 'VC', 'FC', 'AFC', 'AVC', 'Q', 'P', 'ATC', 'TR', 'PR']

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

VClbl = Label(window, text='VC', font=('Arial Bold', 14))
VClbl.grid(column=0, row=0)
VCtxt = Entry(window, width=6)
VCtxt.grid(column=0, row=1)

FClbl = Label(window, text='FC', font=('Arial Bold', 14))
FClbl.grid(column=1, row=0)
FCtxt = Entry(window, width=6)
FCtxt.grid(column=1, row=1)

AFClbl = Label(window, text='AFC', font=('Arial Bold', 14))
AFClbl.grid(column=2, row=0)
AFCtxt = Entry(window, width=6)
AFCtxt.grid(column=2, row=1)

AVClbl = Label(window, text='AVC', font=('Arial Bold', 14))
AVClbl.grid(column=3, row=0)
AVCtxt = Entry(window, width=6)
AVCtxt.grid(column=3, row=1)

Qlbl = Label(window, text='Q', font=('Arial Bold', 14))
Qlbl.grid(column=4, row=0)
Qtxt = Entry(window, width=6)
Qtxt.grid(column=4, row=1)

Plbl = Label(window, text='P', font=('Arial Bold', 14))
Plbl.grid(column=5, row=0)
Ptxt = Entry(window, width=6)
Ptxt.grid(column=5, row=1)

ATClbl = Label(window, text='ATC', font=('Arial Bold', 14))
ATClbl.grid(column=6, row=0)
ATCtxt = Entry(window, width=6)
ATCtxt.grid(column=6, row=1)

TRlbl = Label(window, text='TR', font=('Arial Bold', 14))
TRlbl.grid(column=7, row=0)
TRtxt = Entry(window, width=6)
TRtxt.grid(column=7, row=1)

PRlbl = Label(window, text='PR', font=('Arial Bold', 14))
PRlbl.grid(column=8, row=0)
PRtxt = Entry(window, width=6)
PRtxt.grid(column=8, row=1)

ARlbl = Label(window, text='AR', font=('Arial Bold', 14))
ARlbl.grid(column=9, row=0)
ARtxt = Entry(window, width=6)
ARtxt.grid(column=9, row=1)

QCRlbl = Label(window, text='QCR', font=('Arial Bold', 14))
QCRlbl.grid(column=9, row=0)
QCRtxt = Entry(window, width=6)
QCRtxt.grid(column=9, row=1)

btn = Button(window, text='Рассчитать', command=Cliсked, width=8)
btn.grid(column=4, row=2)

ANSlbl = Label(window, text='TC = ', font=('Arial Bold', 14))
ANSlbl.grid(column=4, row=3)

window.mainloop()