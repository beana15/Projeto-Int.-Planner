import sqlite3

bd = sqlite3.connect ("banco de dados")

def iniciar_bdplanner():
  bdplanner = None
  try:
    bdplanner = sqlite3.connect(arquivo.banco)
    
  except sqlite3.error as Erro:
    print("Erro na conexão",Erro)
    
  return bdplanner

def criar_tabela(bdplanner,sql_criar_tabela):
  try:
    cursor = bdplanner.cursor()
    cursor.execute(sql_criar_tabela)
  except sqlite3.Error as Erro:
    print("Erro ao criar a tabela",Erro)
    

    def inserir_usuario(bdplanner, sql_inserir_usuario):
      try:
        cursor = bdplanner.cursor()
        cursor.execute(sql_inserir_usuario)
        bdplanner.commit()
        print('Conexão estabelecida')
      except sqlite3.Error as Erro:
        print('Erro na inserção de dados:', Erro)

def buscar_usuario(bdplanner, sql_buscar_usuario):
  usuario = None
  try:
    cursor = bdplanner.cursor()
    cursor.execute(sql_buscar_usuario)
    usuario = cursor.fetchall()
    print('cadastro concedido.')
  except sqlite3.Error as Erro:
    print('Erro exibindo ao conectar:', Erro)
  finally:
    return usuario 

import sqlite3
from bdplanner import *

#tabela Usuário 

bdplanner = iniciar_conexão()

sql_criar_tabela = """ CREAT TABLE usuario(
                        id integer PRIMERY
KEY AUTOINCREMENT,
                      nome varchar(50) NOT NULL,
                      email varchar(30) NOT NULL,
                      senha varchar(30) NOT NULL
                    ); """

criar_tabela(bdplanner,sql_criar_tabela)

sql_inserir_usuario_Bruno = "INSERT INTO usuario(nome,email)VALUES ('Bruno,@bruninhocarreirinha')"

sql_inserir_usuario_Fernando = "INSERT INTO usuario(nome,email)VALUES ('Fernando,@fernandinho')"

sql_inserir_usuario_Carla = "INSERT INTO usuario(nome,email)VALUES ('Carla,@barbiezinhacarlinha')"

inserir_usuario(bdplanner,sql_inserir_usuario_Bruno)
inserir_usuario(bdplanner,sql_inserir_usuario_Fernando)
inserir_usuario(bdplanner,sql_inserir_usuario_Carla)

sql_buscar_usuario = "SELECT * FROM usuario"
usuario = buscar_usuario(bdplanner,sql_buscar_usuario)



#tabela agendamento

slq_criar_tabela = """CREAT TABLE agendamento(
                        id integer PRIMARY
KEY AUTOINCREMENT,
                      resp_agendamento varchar(50) NOT NULL
                      lista_eventos varchar(50)
                      ); """

criar_tabela(bdplanner,sql_criar_tabela)

sql_adicionar_tabela = """ALTER TABLE agendamento(
                        add column usuario usuario int
                        ); """

#tabela calendário

sql_criar_tabela = """CREAT TABLE agendamento(
                      id calendario PRIMARY 
KEY AUTOINCREMENT,
                    ano date,
                    mes date,
                    dia date,
                    hora time
                      );"""

#tabela compromisso

sql_criar_tabela = """CREAT TABLE compromisso(
                      id cod_compromisso PRIMARY 
KEY AUTOINCREMENT, 
                    ano_compromisso date,
                    mes_compromisso date,
                    dia_compromisso date,
                    hora_compromisso time,
                    titulo_compromisso varchar(50),
                    descricao_compromisso text
                    );"""

fechar_conexao(bdplanner)