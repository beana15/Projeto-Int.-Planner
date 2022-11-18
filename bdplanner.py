import sqlite3

arquivo = "banco.bd"

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
    