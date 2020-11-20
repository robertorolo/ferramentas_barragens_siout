from tkinter import *

def btn_click():
    #reading variables
    pp = textbox1.get()
    pp = float(pp.replace(',','.'))
    vmin = textbox1.get()
    vmin = float(vmin.replace(',','.'))
    h = textbox3.get()
    h = float(h.replace(',','.'))
    vcap = textbox3.get()
    vcamp = float(vcap.replace(',','.'))

    vmin_s = vmin / 3.6
    pt = vmin_s * h / 75 / 0.7
    resultado.set("Potência teórica (kW) {}".format(round(pt, 2)))


root = Tk()
root.title("pumpcheck")
#root.geometry("750x400")
root.resizable(False, False)
root.iconbitmap('icon_SxK_icon.ico')

#labels 
label_1 = Label(root, text="Potência da bomba (kW)")
label_1.grid(row=0, column=0, sticky=W)
textbox1 = Entry(root, width=8)
textbox1.grid(row=0, column=1, sticky=W)
textbox1.focus()

label_2 = Label(root, text="Vazão máxima (m³/h)")
label_2.grid(row=0, column=2, sticky=W)
textbox1 = Entry(root, width=8)
textbox1.grid(row=0, column=3, sticky=W)

label_3 = Label(root, text="Altura manométrica (m)")
label_3.grid(row=0, column=4, sticky=W)
textbox3 = Entry(root, width=8)
textbox3.grid(row=0, column=5, sticky=W)

label_4 = Label(root, text="Vazão captação (m³/s)")
label_4.grid(row=1, column=0, sticky=W)
textbox4 = Entry(root, width=8)
textbox4.grid(row=1, column=1, sticky=W)

resultado = StringVar()
label_5 = Label(root, textvariable=resultado)
label_5.grid(row=2, column=0, sticky=W)

#botao
btn = Button(root, text="Calcular", command=btn_click)
btn.grid(row=2, column=5, sticky=E)

root.mainloop()