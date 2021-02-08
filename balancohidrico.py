#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
import numpy as np

def quit_me():
    print('quit')
    root.quit()
    root.destroy()

def btn_click():
    v = textbox1.get()
    v = float(v.replace('.','').replace(',','.'))

    v_anual = textbox12.get()
    v_anual =  float(v_anual.replace('.','').replace(',','.'))
    
    qrem = textbox2.get()
    qrem = float(qrem.replace(',','.'))
    
    qref = textbox3.get()
    qref = float(qref.replace(',','.'))
    
    qcap = textbox4.get()
    qcap = float(qcap.replace(',','.'))
    
    p = float(textbox5.get())
    
    maxout = qref * (1 - (p/100))
    maxcapt = qref - maxout
    print('máxima outorgável: {}'.format(round(maxout,5)))
    print('máxima captação: {}'.format(round(maxcapt,5)))
    
    if qrem > maxout:
        qremresult = 'OK'
        #if qrem > qref:
        #    qremresult = 'qrem > qref'
    else:
        perct = 100 - qrem/maxout * 100
        qremresult = 'Não OK em {}%'.format(round(perct, 1))
        
    if qcap < maxcapt:
        qcapresult = 'OK'
    else:
        perct = 100 - qcap/maxcapt * 100
        qcapresult = 'Não OK em {}%'.format(round(np.abs(perct), 2))
        
    r1 = '''vazão remanescente proposta: {}\nvazão de captação proposta: {}'''.format(qremresult, qcapresult)
    resultado1.set(r1)
    
    qvert = qref - (qrem + qcap)
    
    if qvert < 0:
        t = v/np.abs(qvert)
        t = t/(60*60)
        r = '''esvaziamento em {} horas\nvazão vertida: {}'''.format(round(t,0), round(qvert, 2))
    else:
        r = 'vazão vertida: {}'.format(round(qvert, 2))
        
    resultado.set(r)

    if v_anual > v:
        r = 'Volume anual = {} x volume armazenado'.format(round(v_anual/v,2))
    else:
        r = 'Volume anual OK'

    resultado2.set(r)
    
root = Tk()
root.protocol("WM_DELETE_WINDOW", quit_me)
root.title("Balanço hídrico")
root.resizable(True, True)

label_1 = Label(root, text="Volume armazenado (m³)")
label_1.grid(row=0, column=0, sticky=W, padx=(5, 5), pady=(5, 5))
textbox1 = Entry(root, width=8)
textbox1.grid(row=0, column=1, sticky=E, padx=(5, 5), pady=(5, 5))

label_12 = Label(root, text="Volume total anual (m³)")
label_12.grid(row=1, column=0, sticky=W, padx=(5, 5), pady=(5, 5))
textbox12 = Entry(root, width=8)
textbox12.grid(row=1, column=1, sticky=E, padx=(5, 5), pady=(5, 5))

label_2 = Label(root, text="Vazão remanescente (m³/s)")
label_2.grid(row=2, column=0, sticky=W, padx=(5, 5), pady=(5, 5))
textbox2 = Entry(root, width=8)
textbox2.grid(row=2, column=1, sticky=E, padx=(5, 5), pady=(5, 5))

label_3 = Label(root, text="Vazão de referência (m³/s)")
label_3.grid(row=3, column=0, sticky=W, padx=(5, 5), pady=(5, 5))
textbox3 = Entry(root, width=8)
textbox3.grid(row=3, column=1, sticky=E, padx=(5, 5), pady=(5, 5))

label_5 = Label(root, text="Percentual máximo outorgável")
label_5.grid(row=4, column=0, sticky=W, padx=(5, 5), pady=(5, 5))
textbox5 = Entry(root, width=8)
textbox5.grid(row=4, column=1, sticky=E, padx=(5, 5), pady=(5, 5))
textbox5.insert(END, '50')

label_4 = Label(root, text="Vazão de captação (m³/s)")
label_4.grid(row=5, column=0, sticky=W, padx=(5, 5), pady=(5, 5))
textbox4 = Entry(root, width=8)
textbox4.grid(row=5, column=1, sticky=E, padx=(5, 5), pady=(5, 5))

resultado = StringVar()
label_5 = Label(root, textvariable=resultado)
label_5.grid(row=8, column=0, columnspan = 2, padx=(5, 5), pady=(5, 5))

resultado1 = StringVar()
label_6 = Label(root, textvariable=resultado1)
label_6.grid(row=7, column=0, columnspan = 2, padx=(5, 5), pady=(5, 5))

resultado2 = StringVar()
label_7 = Label(root, textvariable=resultado2)
label_7.grid(row=9, column=0, columnspan = 2, padx=(5, 5), pady=(5, 5))

#botao
btn = Button(root, text="Calcular", command=btn_click)
btn.grid(row=6, column=1, sticky=E, padx=(5, 5), pady=(5, 5))

root.mainloop()
