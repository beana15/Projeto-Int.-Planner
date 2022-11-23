import sqlite3

arquivo = "banco.bd"

def iniciar_bdplanner():
  bdplanner = None
  try:
    bdplanner = sqlite3.connect(arquivo_banco)
    
  except sqlite3.Error as e:
    print("Erro na conexão",e)
    
  return bdplanner

def criar_tabela(bdplanner,sql_criar_tabela):
  try:
    cursor = bdplanner.cursor()
    cursor.execute(sql_criar_tabela)
  except sqlite3.Error as e:
    print("Erro ao criar a tabela",e)
    

    def inserir_usuario(bdplanner, sql_inserir_usuario):
      try:
        cursor = bdplanner.cursor()
        cursor.execute(sql_inserir_usuario)
        bdplanner.commit()
        print('Conexão estabelecida')
      except sqlite3.Error as e:
        print('Erro na inserção de dados:', e)

def buscar_usuario(bdplanner, sql_buscar_usuario):
  usuario = None
  try:
    cursor = bdplanner.cursor()
    cursor.execute(sql_buscar_usuario)
    usuario = cursor.fetchall()
    print('exibição de dados concedida.')
  except sqlite3.Error as e:
    print('Erro exibindo os dados:', e)
  finally:
    return usuario
    