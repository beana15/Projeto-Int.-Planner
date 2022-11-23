from tkinter import *

class Usuario():
  def __init__(self):
    self.cadastro = Tk()
    self.cadastro.title('cadastro')
    self.cadastro.geometry('400x400+80+80')

    self.n = Label(self.cadastro,text='Nome')
    self.n.place(x='70',y='60')
    self.nome = Entry(self.cadastro)
    self.nome.place(x='115',y='60')
    
    self.e = Label(self.cadastro,text='Email')
    self.e.place(x='70',y='90')
    self.email = Entry(self.cadastro)
    self.email.place(x='115',y='90')
    
    self.s = Label(self.cadastro,text='Senha')
    self.s.place(x='70',y='120')
    self.senha = Entry(self.cadastro)
    self.senha.place(x='115',y='120')
    
    self.u = Label(self.cadastro,text='Nome de \nusuário')
    self.u.place(x='70',y='150')
    self.user = Entry(self.cadastro)
    self.user.place(x='130',y='150')

    self.mano = Label(self.cadastro,text='')
    self.mano.place(x='205',y='300')

    self.bt = Button(self.cadastro,text='entrar',command=self.realizarlogin)
    self.bt.place(x='285',y='300')

    #self.usuario_nome = self.nome.get()
    #self.usuario_email = self.email.get()
    #self.usuario_senha = self.senha.get()
    #self.usuario_user = self.user.get()

    self.cadastro.mainloop()

  def realizarcadastro(self):
    self.usuario = Usuario()
    self.usuario_nome = self.nome.get()
    self.usuario_email = self.email.get()
    self.usuario_senha = self.senha.get()
    self.usuario_user = self.user.get()
    #self.mostra = self.usuario_nome+'\n'+self.usuario_email+'\n'+self.usuario_senha+'\n'+self.usuario_user
    #self.mano['text'] = self.mostra
    
    realizarlogin()

  def realizarlogin(self):
    #self.cadastro.destroy()
    self.login = Tk()
    self.login.title('login')
    self.login.geometry('400x400+80+80')

    self.u = Label(self.login,text='Nome de \nusuário')
    self.u.place(x='70',y='150')
    self.user = Entry(self.login)
    self.user.place(x='130',y='150')

    self.s = Label(self.login,text='Senha')
    self.s.place(x='70',y='120')
    self.senha = Entry(self.login)
    self.senha.place(x='115',y='120')

    self.bt1 = Button(self.login,text='entrar',command=self.menu)
    self.bt1.place(x='285',y='300')

    self.login.mainloop()

    
  def menu():
    self.menu = Tk()
    self.menu.title('login')
    self.menu.geometry('400x400+80+80')
    self.label = Label(self.menu,text='socorro Deus')
    self.label.place(x='115',y='120')

    self.menu.mainloop()
  
#usuario = Usuario()    
#usuario.usuario_nome = ''
#usuario.usuario_email = ''
#usuario.usuario_senha = ''
#usuario.usuario_user = ''
#usuario.__dict__