from tkinter import *
import os
cor1 = '#ff8826'
cor2 = '#fed35b'
cor3 = '#ffd78f'
cor4 = '#c1cdf4'
cor5 = '#fd90a0'
cor6 = '#651366'
cor7 = '#2c9fa3'

principal = Tk()
principal.title('PlanLion')
principal.configure(bg = cor3)
principal.geometry('400x400+200+200')
label1=Label(text='Seja Bem-vinda(o)\n\nO PlanLion é uma ferramenta que planejamos para sua própria organização',bg=cor3)
label1.place(x='100',y='100')

def bt_click():
  os.system("clear")

botao1=Button(principal,command=bt_click,text='Continuar',background=cor1)
botao1.place(x='285',y='200')