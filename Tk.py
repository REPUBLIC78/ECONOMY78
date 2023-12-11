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
    'QCR': None,
    'MC': None,
    'MR': None
}

vl, cl, rl = list(vd), [], []#список ключей, пустой список для наименований полей, список с полями ввода

def Cliсked():
    for i in range(12):
        try:
            vd[vl[i]] = int(rl[i].get())
        except:
            vd[vl[i]] = None
    if fTC(vd) == None:
        ANSlbl.configure(text='Н/д')
    else:
        ANSlbl.configure(text=f'TC = {fTC(vd)}')

window = Tk()
window.title('Рассчёт TC')
window.geometry('640x360')
window.minsize(500,300)
window.maxsize(1280,720)

label_style = ttk.Style()
label_style.configure("main.TLabel",     # имя стиля
                    font="helvetica 14",    # шрифт
                    foreground="#ffffff",   # цвет текста
                    padding=0,              # отступы
                    background="#36393e")   # фоновый цвет

label_style.configure("button.TButton",     # имя стиля
                    font="helvetica 14",    # шрифт
                    foreground="#000000",   # цвет текста
                    padding=0,              # отступы
                    background="#424549")   # фоновый цвет

label_style.configure('My.TFrame', background='#424549')
mail1 = ttk.Frame(window, style='My.TFrame')
mail1.place(height=1080, width=1920, x=0, y=0)
mail1.config()

for c in range(len(vd)): window.columnconfigure(index=c, weight=1) #Адаптив
for r in range(4): window.rowconfigure(index=r, weight=1)

for i in range(len(vd)):
    cl.append(ttk.Label(window, text=vl[i], style="main.TLabel")) #названия полей ввода
    cl[i].grid(column=i, row=0)

for i in range(12):
    rl.append(Entry(window, width=6)) #поля ввода
    rl[i].grid(column=i, row=1)

btn = ttk.Button(window, text='Рассчитать', command=Cliсked, width=9, style="button.TButton") #кнопка рассчитать
btn.grid(column=5, row=2, columnspan=2)

ANSlbl = ttk.Label(window, text='TC = ', style="main.TLabel") #вывод ответа
ANSlbl.grid(column=5, row=3, columnspan=2)

window.mainloop()