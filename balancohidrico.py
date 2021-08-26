#!/usr/bin/env python

from tkinter import *
from tkinter import ttk

def vp(vmin, vmax):
    vpv = (vmax-vmin)/vmin*100
    return abs(vpv)

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
    qrem = float(qrem.replace('.','').replace(',','.'))
    
    qref = textbox3.get()
    qref = float(qref.replace('.','').replace(',','.'))
    
    qcap = textbox4.get()
    qcap = float(qcap.replace('.','').replace(',','.'))

    horascap = textboxhoras.get()
    horascap = float(horascap.replace('.','').replace(',','.'))
    diascap = int(textboxdias.get())

    unidade =  comboExample.get()
    
    p = float(textbox5.get())
    
    maxout = qref * (1 - (p/100))
    maxcapt = qref - maxout
    print('máxima outorgável: {}'.format(round(maxout,5)))
    print('máxima captação: {}'.format(round(maxcapt,5)))
    
    if qrem > maxout:
        qremresult = 'A vazão remanescente é inferior ao máximo outorgável.'
    else:
        perct = vp(maxout, qrem)
        qremresult = 'A vazão remanescente é {}% menor do que máximo outorgável.'.format(round(perct, 1))

    resultado3.set(qremresult)  
    
    if unidade == "m³/h":
        qcap = qcap/(60*60)
        print('vazão de captação transformada: ',qcap)
    
    if qcap < maxcapt:
        qcapresult = 'A vazão captada é menor do que o máximo permitido.'
    else:
        perct = vp(maxcapt, qcap)
        qcapresult = 'A vazão captada é {}% maior do que o máximo permitido'.format(round(abs(perct), 2))
        
    resultado1.set(qcapresult)
    
    qvert = qref - (qrem + qcap)
    
    if qvert < 0:
        t = v/abs(qvert)
        t = t/(60*60)
        r = 'O reservatório será esvaziado em {} horas - vazão vertida: {}.'.format(round(t,0), round(qvert, 2))
    else:
        r = 'O reservatário não será esvaziado - vazão vertida: {}.'.format(round(qvert, 2))
        
    resultado.set(r)

    if v_anual > v:
        r = 'A captação anual é {} vezes o volume armazenado'.format(round(v_anual/v,2))
    else:
        r = 'A captação anual é menor do que o volume armazenado.'

    resultado2.set(r)
    
root = Tk()
root.protocol("WM_DELETE_WINDOW", quit_me)
root.title("Balanço hídrico")
#root.geometry("500x500")
root.resizable(False, False)

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

label_4 = Label(root, text="Vazão de captação")
label_4.grid(row=5, column=0, sticky=W, padx=(5, 5), pady=(5, 5))
textbox4 = Entry(root, width=8)
textbox4.grid(row=5, column=1, sticky=E, padx=(5, 5), pady=(5, 5))
units=["m³/s", "m³/h"]
comboExample = ttk.Combobox(root, values=units, width=8)
comboExample.grid(row=5, column=2, sticky=E, padx=(5, 5), pady=(5, 5))

label_horas = Label(root, text="Horas de captação por dia")
label_horas.grid(row=6, column=0, sticky=W, padx=(5, 5), pady=(5, 5))
textboxhoras = Entry(root, width=8)
textboxhoras.grid(row=6, column=1, sticky=E, padx=(5, 5), pady=(5, 5))
textboxhoras.insert(END, '24')

label_dias = Label(root, text="Dias de captação por ano")
label_dias.grid(row=7, column=0, sticky=W, padx=(5, 5), pady=(5, 5))
textboxdias = Entry(root, width=8)
textboxdias.grid(row=7, column=1, sticky=E, padx=(5, 5), pady=(5, 5))
textboxdias.insert(END, '365')

resultado = StringVar()
label_5 = Label(root, textvariable=resultado)
label_5.grid(row=10, column=0, sticky=W, columnspan=3, padx=(5, 5), pady=(5, 5))

resultado1 = StringVar()
label_6 = Label(root, textvariable=resultado1)
label_6.grid(row=11, column=0, sticky=W, columnspan=3, padx=(5, 5), pady=(5, 5))

resultado2 = StringVar()
label_7 = Label(root, textvariable=resultado2)
label_7.grid(row=12, column=0, padx=(5, 5), pady=(5, 5), sticky=W, columnspan=3)

resultado3 = StringVar()
label_8 = Label(root, textvariable=resultado3)
label_8.grid(row=13, column=0, padx=(5, 5), pady=(5, 5), sticky=W, columnspan=3)

label_dummy = Label(root, text="*"*35+str('Resultado')+"*"*35)
label_dummy.grid(row=9, column=0, sticky=W, columnspan=3, padx=(5, 5), pady=(5, 5))

#botao
btn = Button(root, text="Calcular", command=btn_click)
btn.grid(row=8, column=2, sticky=E, padx=(5, 5), pady=(5, 5))

root.mainloop()