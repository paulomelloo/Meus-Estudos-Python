from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Relógio")

def relogio():
    horario = strftime('%H:%M:%S')
    label.config(text=horario)
    label.after(1000, relogio) #atualiza a cada 1s

label = Label(root, font=('Helvetica', 60), background="#39393A", foreground="#ffffff") # cor do fundo preto, cor do texto verde
label.pack(anchor="center")

relogio()

mainloop()