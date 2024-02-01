from tkinter import *
from datetime import datetime


janela = Tk()
janela.title('Relógio Digital')
janela.configure(bg='black')
janela.geometry('440x180')
janela.resizable(width=False, height=False)


def relogio():
    tempo = datetime.now()
    hora = tempo.strftime('%H:%M:%S')
    dia_semana = tempo.strftime('%A')
    dia = tempo.day
    mes = tempo.strftime('%b')
    ano = tempo.strftime('%y')
    data = dia_semana + '  ' + str(dia) + '/'+ str(mes)+ '/' + ano

    l1.configure(text=hora)
    l1.after(200,relogio)
    l2.configure(text=data)



l1 = Label(janela, text='', font=('Arial', 80), bg='black', fg='white')
l1.grid(row=0,column=0,sticky=NW)
l2 = Label(janela, text='', font=('Arial', 20), bg='black', fg='white')
l2.grid(row=1,column=0,sticky=NW)

relogio()
janela.mainloop()