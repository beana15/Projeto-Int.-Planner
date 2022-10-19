from Calendario import *

class Compromisso:
  def __init__(self,descricao,ano,mes,dia,hora):
   self.__descricao = input('Escreva qual o seu compromisso: ')
   self.__data = Calendario('', '', '','')

  #def marcarCompromisso(self, descricao, data):
    #self.__descricao = input('Escreva qual o seu compromisso: ')06
    #self.__data = input('Data do seu compromisso: ')

  def getconsultarCompromisso(self, descricao,ano,mes,dia,hora):
   print('Compromisso: ' +self.__descricao)
   print('Às ' +self.__data.hora+ ' horas')
   print('Dia: ' +self.__data.dia)
   print('Mês: ' +self.__data.mes)
   print('Ano: ' +self.__data.ano)
   
   #return self.__hora
    #+self.__data+ '\nÀs '+self.__hora+ '\n' +self.__dia+ '/' +self.__mes+ '/' +self.__ano
   #return self.__data+ '\nÀs '+self.__hora+ '\n' +self.__dia+ '/' +self.__mes+ '/' +self.__ano
   
  def setCompromisso(self, data):
   self.__descricao = input('Escreva seu compromisso: ')
   self.__data = input('Escreva a data: ')