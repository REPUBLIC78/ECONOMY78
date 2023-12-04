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

vl, cl, rl = list(vd), [], []#список ключей, пустой список для наименований полей, список с полями ввода

def Cliсked():
    for i in range(12):
        try:
            vd[vl[i]] = int(rl[i].get())
        except:
            vd[vl[i]] = None
    if fTC(vd) == 'Недостаточно данных':
        ANSlbl.configure(text='Н/д')
    else:
        ANSlbl.configure(text=f'TC = {fTC(vd)}')

window = Tk()
window.title('Рассчёт TC')
window.geometry('640x360')
window.minsize(500,300)
window.maxsize(640,360)

for c in range(len(vd)): window.columnconfigure(index=c, weight=1) #Адаптив
for r in range(4): window.rowconfigure(index=r, weight=1)

for i in range(len(vd)):
    cl.append(Label(window, text=vl[i], font=('Arial Bold', 14))) #названия полей ввода
    cl[i].grid(column=i, row=0)

for i in range(12):
    rl.append(Entry(window, width=6)) #поля ввода
    rl[i].grid(column=i, row=1)

btn = Button(window, text='Рассчитать', command=Cliсked, width=8) #кнопка рассчитать
btn.grid(column=5, row=2, columnspan=2)

ANSlbl = Label(window, text='TC = ', font=('Arial Bold', 14)) #вывод ответа
ANSlbl.grid(column=5, row=3, columnspan=2)

window.mainloop()