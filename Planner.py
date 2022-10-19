from Calendario import *
from Compromisso import *

class Planner:
  def __init__(self, eventos, lista_compromissos, lista_usuarios, item_planner,item_comp):
    self.__eventos = eventos
    self.__lista_compromissos = lista_compromissos
    self.__lista_usuarios = lista_usuarios
    self.item_planner = Calendario()
    self.item_comp = Compromisso()

  def entrarPlanner(self, eventos,lista_compromissos, lista_usuarios, item_planner):
    self.__eventos = input('1. Marcar evento')
    self.__lista_compromissos = input('2. Consultar seus compromissos')
    self.__lista_usuarios = input('4. Consultar compartilhamento do Planner')
    self.__item_planner = input('5. Ir para o calendário')

  def setmodificarAgenda(self, lista_compromissos):
    self.item_comp = int(input('Deseja: \n1 - Editar compromisso \n2 - Excluir compromisso\n\n'))
    if item_comp == 1:
      setCompromisso()
    #self.__lista_compromissos = input('1. Editar compromisso'))
    #self.__lista_compromissos = input('2. Excluir compromisso\n'))