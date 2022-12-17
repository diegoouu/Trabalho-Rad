#Abra o Banco e Depois execute o arquivo do trabalho


import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port)
        print("Conexão com o banco ", db_name, " foi bem sucedida")
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")
    return connection
    

def create_table(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Tabela criada com sucesso!")
        cursor.close()
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")

#--------------------------------------------------------------------------------------
#======================================================================================
#--------------------------------------------------------------------------------------


# Conexão com o banco de dados teste
connection = create_connection("banco", "postgres", "admin157", "127.0.0.1", "5432")

table_Pessoa_query = """CREATE TABLE Pessoa(
    ID  SERIAL PRIMARY KEY,
    cpf char(15),
    primeiroNome varchar(50) NOT NULL,
    meioNome varchar(50),
    sobrenome varchar(50) NOT NULL,
    idade int CONSTRAINT idade_positiva CHECK (idade >= 0),
    peso real CONSTRAINT peso_positivo CHECK (peso > 0)
)
"""

table_Conta_query = """CREATE TABLE Conta(
    id SERIAL PRIMARY KEY,
    numero int NOT NULL,
    agencia int NOT NULL,
    saldo int NOT NULL,
    gerente varchar(50),
    titular varchar(50),
    estado varchar(50)
)
"""
table_Endereco_query = """CREATE TABLE Endereco(
    rua varchar(50),
    numero int NOT NULL,
    bairro varchar(50),
    cep int NOT NULL,
    cidade varchar(50)
)
"""


create_table(connection, table_Endereco_query)
create_table(connection, table_Conta_query)
create_table(connection, table_Pessoa_query)


connection.close()