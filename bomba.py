#!/usr/bin/env python

from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 8


def quit_me():
    print('quit')
    root.quit()
    root.destroy()

def btn_click():
    #reading variables
    pp = textbox1.get()
    pp = float(pp.replace(',','.'))
    vmin = textbox2.get()
    vmin = float(vmin.replace(',','.'))
    h = textbox3.get()
    h = float(h.replace(',','.'))
    vcap = textbox4.get()
    vcap = float(vcap.replace(',','.'))

    vmin_conv = vmin / 3600
    vmin_s = vmin / 3.6
    pt = vmin_s * h / 75 / 0.7
    resultado.set("Potência teórica (kW) {}".format(round(pt, 2)))

    plt.clf()
    
    fig, axs = plt.subplots(nrows=1, ncols=2)
    axs[0].set_title("Potência")
    axs[1].set_title("Vazão")
    axs[0].grid(linestyle='--')
    axs[1].grid(linestyle='--')
    axs[0].set_xticks([])
    axs[1].set_xticks([])
    axs[0].set_ylabel("kW")
    axs[1].set_ylabel("m³/s")
 
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().grid(row=3, columnspan=6)
    
    axs[0].bar([0,1], [pp, pt], color="gray")
    axs[0].axhline(y=pp, color='black', linestyle="--")
    axs[0].axhline(y=pp*(1-0.05), color='green')
    axs[0].annotate("-5%", xy=(0, pp*(1-0.05)), fontsize=7, color="green")
    axs[0].axhline(y=pp*(1+0.05), color='green')
    axs[0].annotate("+5%", xy=(0, pp*(1+0.05)), fontsize=7, color="green")
    axs[0].axhline(y=pp*(1-0.1), color='yellow')
    axs[0].annotate("-10%", xy=(0, pp*(1-0.1)), fontsize=7, color="yellow")
    axs[0].axhline(y=pp*(1+0.1), color='yellow')
    axs[0].annotate("+10%", xy=(0, pp*(1+0.1)), fontsize=7, color="yellow")
    axs[0].axhline(y=pp*(1-0.2), color='red')
    axs[0].annotate("-20%", xy=(0, pp*(1-0.2)), fontsize=7, color="red")
    axs[0].axhline(y=pp*(1+0.2), color='red')
    axs[0].annotate("+20%", xy=(0, pp*(1+0.2)), fontsize=7, color="red")
    axs[0].set_xticks([0,1])
    axs[0].set_xticklabels(["Proposta", "Teórica"])

    axs[1].bar([0,1], [vcap, vmin_conv], color="gray")
    axs[1].axhline(y=vcap, color='black', linestyle="--")
    axs[1].axhline(y=vcap*(1-0.05), color='green')
    axs[1].annotate("-5%", xy=(0, vcap*(1-0.05)), fontsize=7, color="green")
    axs[1].axhline(y=vcap*(1+0.05), color='green')
    axs[1].annotate("+5%", xy=(0, vcap*(1+0.05)), fontsize=7, color="green")
    axs[1].axhline(y=vcap*(1-0.1), color='yellow')
    axs[1].annotate("-10%", xy=(0, vcap*(1-0.1)), fontsize=7, color="yellow")
    axs[1].axhline(y=vcap*(1+0.1), color='yellow')
    axs[1].annotate("+10%", xy=(0, vcap*(1+0.1)), fontsize=7, color="yellow")
    axs[1].axhline(y=vcap*(1-0.2), color='red')
    axs[1].annotate("-20%", xy=(0, vcap*(1-0.2)), fontsize=7, color="red")
    axs[1].axhline(y=vcap*(1+0.2), color='red')
    axs[1].annotate("+20%", xy=(0, vcap*(1+0.2)), fontsize=7, color="red")
    axs[1].set_xticks([0,1])
    axs[1].set_xticklabels(["Captação", "Bomba"])

    plt.tight_layout()

    plt.draw()

root = Tk()
root.protocol("WM_DELETE_WINDOW", quit_me)
root.title("pumpcheck")
root.resizable(False, False)
#root.iconbitmap('icon_SxK_icon.ico')

#labels 
label_1 = Label(root, text="Potência da bomba (kW)")
label_1.grid(row=0, column=0, sticky=W, padx=(10, 10), pady=(5, 5))
textbox1 = Entry(root, width=8)
textbox1.grid(row=0, column=1, sticky=W, padx=(10, 10), pady=(5, 5))
textbox1.focus()

label_2 = Label(root, text="Vazão máxima (m³/h)")
label_2.grid(row=0, column=2, sticky=W, padx=(10, 10), pady=(5, 5))
textbox2 = Entry(root, width=8)
textbox2.grid(row=0, column=3, sticky=W, padx=(10, 10), pady=(5, 5))

label_3 = Label(root, text="Altura manométrica (m)")
label_3.grid(row=0, column=4, sticky=W, padx=(10, 10), pady=(5, 5))
textbox3 = Entry(root, width=8)
textbox3.grid(row=0, column=5, sticky=W, padx=(10, 10), pady=(5, 5))

label_4 = Label(root, text="Vazão captação (m³/s)")
label_4.grid(row=1, column=0, sticky=W, padx=(10, 10), pady=(5, 5))
textbox4 = Entry(root, width=8)
textbox4.grid(row=1, column=1, sticky=W, padx=(10, 10), pady=(5, 5))

resultado = StringVar()
label_5 = Label(root, textvariable=resultado)
label_5.grid(row=2, column=0, sticky=W, padx=(10, 10), pady=(5, 5))

fig, axs = plt.subplots(nrows=1, ncols=2)
axs[0].set_title("Potência")
axs[1].set_title("Vazão")
axs[0].grid(linestyle='--')
axs[1].grid(linestyle='--')
axs[0].set_xticks([])
axs[1].set_xticks([])
axs[0].set_ylabel("kW")
axs[1].set_ylabel("m³/s")
plt.tight_layout()
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().grid(row=3, columnspan=6, padx=(10, 10), pady=(10, 10))

#botao
btn = Button(root, text="Calcular", command=btn_click)
btn.grid(row=2, column=5, sticky=E, padx=(10, 10), pady=(5, 5))

root.mainloop()
