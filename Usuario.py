class Usuario:
  def __init__(self, nome, email, senha, login):
    self.__nome = input('Nome: ')
    self.__email = input('Email: ')
    self.__senha = input('Senha: ')
    self.login = input('Login: ')

  def realizarCadastro(self, nome, email, senha, login):
    self.__nome = nome
    self.__email = email
    self.__senha = senha
    self.login = login

  def getconsultarUsuario(self,login):
    print(login)

  def consultarLogin(self,login,senha):
    conf = {' :'+self.login+ ' ' +self.__senha}
    
    if conf.get(login):
     print('Esse login está em uso.')
 
    else:
     conf[login] = senha

  #def dicioLogin(self, login, senha):
   # conf2 = {' :'+self.__login+ ' ' +self.__senha}

    #try:
      
  def getconsultarInfo(self):
    return 'NOME: ' +self.__nome+ '\nE-MAIL: ' +self.__email+ '\nSENHA: ' +self.__senha+ '\nLOGIN: ' +self.login

