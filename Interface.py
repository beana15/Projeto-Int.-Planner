from tkinter import *
from Usuario import *
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
label1=Label(principal,bg=cor3,text='Seja Bem-vinda(o)\n\nO PlanLion é uma ferramenta que planejamos para sua própria organização')
label1.place(x='100',y='100')

def cadastro():
  principal.destroy()
  segunda = Tk()
  segunda.title('PlanLion')
  segunda.configure(bg=cor3)
  segunda.geometry('400x400+200+200')

  def bt_cadastro():
   segunda.destroy()
   realizarCadastro()

  botao2=Button(segunda,command=bt_cadastro,text='CADASTRO')
  botao2.place(x='285',y='150')

  #botao4=Button(telaCadastro,command=bt_Logar,text='ENTRAR')
  #botao4.place(x='295',y='200')
  
  def bt_logar():
    segunda.destroy()
    realizarLogin()
    
  botao3=Button(segunda,command=bt_logar,text='ENTRAR')
  botao3.place(x='295',y='200')
 
  
botao1=Button(principal,command=cadastro,text='Continuar',background=cor1)
botao1.place(x='285',y='200')

