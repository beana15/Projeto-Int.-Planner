from tkinter import *
from Interface import *

class Usuario:
  def __init__(self, nome, email, senha, user):
    self.nome=nome
    self.email=email
    self.senha=senha
    self.user=user

  def realizarCadastro(self, nome, email, senha, login):
    #self.nome = ''
    #self.email = ''
    #self.senha = ''
    #self.login = ''

    telaCadastro = Tk()
    telaCadastro.title("Cadastro - PlanLion")
    telaCadastro.configure(bg=cor3)
    telaCadastro.geometry('400x400+200+200')
    
    labelCadN = Label(telaCadastro,bg=cor3,text=self.nome)
    labelCadN.place(x='70',y='60')    
    entradaNome = Entry(telaCadastro)
    entradaNome.place(x='105',y='60')
    
    labelCadE = Label(telaCadastro,bg=cor3,text=self.email)
    labelCadE.place(x='70',y='90')
    entradaEmail = Entry(telaCadastro)
    entradaEmail.place(x='105',y='90')
    
    labelCadS = Label(telaCadastro,bg=cor3,text=self.senha)
    labelCadS.place(x='70',y='120')
    entradaSenha = Entry(telaCadastro)
    entradaSenha.place(x='105',y='120')
    
    labelCadL = Label(telaCadastro,bg=cor3,text=self.login)
    labelCadL.place(x='70',y='160')
    entradaLogin = Entry(telaCadastro)
    entradaLogin.place(x='105',y='160')

    telaCadastro.mainloop()

  def realizarLogin(self,login,senha):
    telaLogin = Tk()
    telaLogin.title("Login - PlanLion")
    telaLogin.configure(bg=cor3)
    telaLogin.geometry('400x400+200+200')

    labelLogL = Label(telaLogin,bg=cor3,text=self.login)
    labelLogL.place(x='80',y='70')
    entradaLogin = Entry(telaLogin)
    entradaLogin.place(x='105',y='70')

    labelLogS = Label(telaLogin,bg=cor3,text=self.login)
    labelLogS.place(x='80',y='90')
    entradaSenha = Entry(telaLogin)
    entradaSenha.place(x='105',y='90')

    
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

