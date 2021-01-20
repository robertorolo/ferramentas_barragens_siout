#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
import numpy as np

def quit_me():
    print('quit')
    root.quit()
    root.destroy()

def btn1_click():
    q = textbox1.get()
    q = float(q.replace(',','.'))
    v = float(combobox2.get())
    a = q/v
    d = 2 * np.sqrt((a/np.pi)) * 1000
    d = round(d,2)
    resultado1.set("Diâmtro interno teórico (mm) {}".format(d))
    
def btn2_click():
    qc = textbox1c.get()
    qc = float(qc.replace(',','.'))
    vc = float(combobox2c.get())
    ac = qc/vc
    ac = round(ac,2)
    resultado2c.set("Área da seção teórica (m²) {}".format(ac))

root = Tk()
root.protocol("WM_DELETE_WINDOW", quit_me)
root.title("channelpipecheck")
root.resizable(True, True)

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Tubulação')
tabControl.add(tab2, text='Canal')

tabControl.pack(expand=1, fill="both")

#tubulacao
label_1 = Label(tab1, text="Vazão Requerida (m³/s)")
label_1.grid(row=0, column=0, sticky=W, padx=(5, 5), pady=(5, 5))
textbox1 = Entry(tab1, width=8)
textbox1.grid(row=0, column=1, sticky=E, padx=(5, 5), pady=(5, 5))

label_2 = Label(tab1, text="Velocidade da água (m/s)")
label_2.grid(row=1, column=0, sticky=W, padx=(5, 5), pady=(5, 5))
combobox2 = ttk.Combobox(tab1, width=8, 
                         values=[
                                0.2, 
                                0.3,
                                0.5,
                                0.8])
combobox2.grid(row=1, column=1, sticky=E, padx=(5, 5), pady=(5, 5))

resultado1 = StringVar()
label_51 = Label(tab1, textvariable=resultado1)
label_51.grid(row=3, column=1, sticky=E, padx=(5, 5), pady=(5, 5))

#botao
btn1 = Button(tab1, text="Calcular", command=btn1_click)
btn1.grid(row=3, column=0, sticky=W, padx=(5, 5), pady=(5, 5))

#canal
label_1c = Label(tab2, text="Vazão Requerida (m³/s)")
label_1c.grid(row=0, column=0, sticky=W, padx=(5, 5), pady=(5, 5))
textbox1c = Entry(tab2, width=8)
textbox1c.grid(row=0, column=1, sticky=E, padx=(5, 5), pady=(5, 5))

label_2c = Label(tab2, text="Velocidade da água (m/s)")
label_2c.grid(row=1, column=0, sticky=W, padx=(5, 5), pady=(5, 5))
combobox2c = ttk.Combobox(tab2, width=8, 
                         values=[
                                0.2, 
                                0.3,
                                0.5,
                                0.8])
combobox2c.grid(row=1, column=1, sticky=E, padx=(5, 5), pady=(5, 5))

resultado2c = StringVar()
label_51c = Label(tab2, textvariable=resultado2c)
label_51c.grid(row=3, column=1, sticky=E, padx=(5, 5), pady=(5, 5))

#botao
btn1c = Button(tab2, text="Calcular", command=btn2_click)
btn1c.grid(row=3, column=0, sticky=W, padx=(5, 5), pady=(5, 5))


root.mainloop()
