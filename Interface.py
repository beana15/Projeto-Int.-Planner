from tkinter import *
from Usuario import *
import os

global usuariosp,nome,email,logar
usuariosp = []
nome = []
email = []
logar = {}

cor1 = '#ff8826'
cor2 = '#fed35b'
cor3 = '#ffd78f'
cor4 = '#c1cdf4'
cor5 = '#fd90a0'
cor6 = '#651366'
cor7 = '#2c9fa3'

def inicial():
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
    telaCadastro = Tk()
    telaCadastro.title("Cadastro - PlanLion")
    telaCadastro.configure(bg=cor3)
    telaCadastro.geometry('400x400+200+200')
    
    labelCadN = Label(telaCadastro,bg=cor3,text='Nome')
    labelCadN.place(x='70',y='60')    
    entradaNome = Entry(telaCadastro)
    entradaNome.place(x='115',y='60')
    
    labelCadE = Label(telaCadastro,bg=cor3,text='Email')
    labelCadE.place(x='70',y='90')
    entradaEmail = Entry(telaCadastro)
    entradaEmail.place(x='115',y='90')
    
    labelCadS = Label(telaCadastro,bg=cor3,text='Senha')
    labelCadS.place(x='70',y='120')
    entradaSenha = Entry(telaCadastro)
    entradaSenha.place(x='115',y='120')
    
    labelCadL = Label(telaCadastro,bg=cor3,text='User')
    labelCadL.place(x='70',y='150')
    entradaUser = Entry(telaCadastro)
    entradaUser.place(x='115',y='150')

    nome = entradaNome.get()
    usuariosp.append(nome)
    email = entradaEmail.get()
    usuariosp.append(email)
    logar[entradaUser.get()] = entradaSenha.get()
   

    def bt_cadrealizado():
      telaCadastro.destroy()
      inicial()
     #usuario = str(bt_cadastro.get())

    botaocad=Button(telaCadastro,command=bt_cadrealizado,text='FINALIZAR') 
    botaocad.place(x='185',y='200')

   botao2=Button(segunda,command=bt_cadastro,text='CADASTRO')
   botao2.place(x='285',y='150')
  
   def bt_logar():
    segunda.destroy()
    telaLogin = Tk()
    telaLogin.title('Login - PlanLion')
    telaLogin.configure(bg=cor3)
    telaLogin.geometry('400x400+200+200')

    labelUser = Label(telaLogin,bg=cor3,text='User:')
    labelUser.place(x='70',y='60')
    entradaUser = Entry(telaLogin)
    entradaUser.place(x='115',y='60')

    labelSenha = Label(telaLogin,bg=cor3,text='Senha:')
    labelSenha.place(x='70',y='90')
    entradaSenha = Entry(telaLogin)
    entradaSenha.place(x='115',y='90')

    def bt_entrar():
      telaLogin.destroy()


    botaoent=Button(telaLogin,command=bt_entrar,text='Entrar')
    botaoent.place(x='175',y='150')
    
   botao3=Button(segunda,command=bt_logar,text='ENTRAR')
   botao3.place(x='295',y='200')

   
  
 botao1=Button(principal,command=cadastro,text='Continuar',background=cor1)
 botao1.place(x='285',y='200')

 principal.mainloop()

inicial()