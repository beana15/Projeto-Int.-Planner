from Compromisso import *

class Calendario:
  def __init__(self, ano, mes, dia, hora,descricao):
   self.ano = input('Ano: ')
   self.mes = input('Mês: ')
   self.dia = input('Dia: ')
   self.hora = input('Hora: ')
   self.descricao = Compromisso()

  #def getdataCalendario(self, ano, mes, dia, hora):
   # return self.__ano 
    #return self.__mes 
    #return self.__dia 
    #return self.__hora
    
  def getconsultarCalendario(self):
   print('Compromisso: ' +self.__descricao)
   print('Às ' +self.data.hora+ ' horas')
   print('Dia: ' +self.data.dia)
   print('Mês: ' +self.data.mes)
   print('Ano: ' +self.data.ano)
   
  def marcarCompromisso(self,compromisso):
   deseja = int(input('Deseja: \n1 - Marcar compromisso \n2 - Editar um compromisso \n\n')
   if deseja == 1:
    comp1 = Compromisso( ',' ',' ',' ',' ')
   else:
    setCompromisso()