from bdplanner import *

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

fechar_conexao(bdplanner)