from tkinter import *
from Interface import *

class Usuario:
  def __init__(self, nome, email, senha, login):
    self.nome = input('Nome: ')
    self.email = input('Email: ')
    self.senha = input('Senha: ')
    self.login = input('Login: ')

  def realizarCadastro(self, nome, email, senha, login):
    self.nome = ''
    self.email = ''
    self.senha = ''
    self.login = ''

    telaCadastro = Tk()
    telaCadastro.title("Cadastro - PlanLion")
    telaCadastro.configure(bg=cor3)
    telaCadastro.geometry('400x400+200+200')
    
    labelCadN = Label(telaCadastro,bg=cor3,text='Nome: ')
    labelCadN.place(x='80',y='70')    
    entradaNome = Entry(telaCadastro)
    entradaNome.place(x='150',y='70')
    
    labelCadE = Label(telaCadastro,bg=cor3,text='Email: ')
    labelCadE.place(x='80',y='70')
    entradaEmail = Entry(telaCadastro)
    entradaEmail.place(x='150',y='70')
    
    labelCadS = Label(telaCadastro,bg=cor3,text='Senha: ')
    labelCadS.place(x='80',y='70')
    entradaSenha = Entry(telaCadastro)
    entradaSenha.place(x='150',y='70')
    
    labelCadL = Label(telaCadastro,bg=cor3,text='Login: ')
    labelCadL.place(x='80',y='70')
    entradaLogin = Entry(telaCadastro)
    entradaLogin.place(x='150',y='70')

  #def getconsultarUsuario(self,login):
   # print(login)

  #def consultarLogin(self,login,senha):
   # conf = {' :'+self.login+ ' ' +self.senha}
    
    #if conf.get(login):
     #print('Esse login está em uso.')
 
    #else:
     #conf[login] = senha

  #def dicioLogin(self, login, senha):
   # conf2 = {' :'+self.__login+ ' ' +self.__senha}

    #try:
      
  #def getconsultarInfo(self):
   # return 'NOME: ' +self.nome+ '\nE-MAIL: ' +self.email+ '\nSENHA: ' +self.senha+ '\nLOGIN: ' +self.login

