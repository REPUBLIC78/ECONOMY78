from tkinter import *
from tkinter import ttk
from economy import findA

vd = {
    'TC': None,
    'VC': None,
    'FC': None,
    'AFC': None,
    'AVC': None,
    'ATC': None,
    'Q': None,
    'P': None,
    'TR': None,
    'PR': None,
    'AR': None,
    'QCR': None
}

vl, cl, rl, al = list(vd), [], [], []#список ключей, пустой список для наименований полей, список с полями ввода, список с ответами

window = Tk()
window.title('Рассчёты')
window.geometry('640x360')
window.minsize(640,360)
window.maxsize(1280,720)


def Cliсked():
    for i in range(len(vd)):
        try:
            vd[vl[i]] = float(rl[i].get())
        except:
            vd[vl[i]] = None
    avd = findA(vd)
    for i in range(len(vd)):
        if avd[vl[i]] != None:
            al[i].configure(text=str(avd[vl[i]]), style="main.TLabel")
        else:
            al[i].configure(text='н/д', style="main.TLabel")


label_style = ttk.Style()
label_style.configure("main.TLabel",     # имя стиля
                    font="helvetica 14",    # шрифт
                    foreground="#ffffff",   # цвет текста
                    padding=0,              # отступы
                    background="#36393e")   # фоновый цвет

label_style.configure("main1.TLabel",     # имя стиля
                    font="helvetica 14",    # шрифт
                    foreground="#ffffff",   # цвет текста
                    padding=0,              # отступы
                    background="#424549")   # фоновый цвет

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

for i in range(len(vd)): #названия полей ввода
    cl.append(ttk.Label(window, text=vl[i], style="main.TLabel"))
    cl[i].grid(column=i, row=0)

for i in range(len(vd)): #поля ввода
    rl.append(Entry(window, width=6))
    rl[i].grid(column=i, row=1)

for i in range(len(vd)): #поля для вывода
    al.append(ttk.Label(window, text=vd[vl[i]], style="main1.TLabel"))
    al[i].grid(column=i, row=2)

btn = ttk.Button(window, text='Рассчитать', command=Cliсked, width=9, style="button.TButton") #кнопка рассчитать

if len(vd) % 2 == 0: #адаптив для кнопки
    btn.grid(column=(int(len(vd) / 2)) - 1, row=3, columnspan=2)
else:
    btn.grid(column=(len(vd) // 2) - 1, row=3, columnspan=3)
window.mainloop()