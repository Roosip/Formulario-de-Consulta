# Importando o módulo sqlite3 com um alias
import sqlite3 as lite

# Criando a conexão com o banco de dados (isso cria o arquivo 'data_user.db' se ele não existir)
conexao = lite.connect('data_user.db') # cria o banco de dados

# Criando a tabela dentro de um contexto 'with' para garantir que a conexão será fechada corretamente
with conexao:
    cursor = conexao.cursor() # Cria um cursor para a execução de comandos SQL
    # Executa o comando SQL para criar a tabela 'formulario' com as colunas especificadas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS formulario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        telefone TEXT,
        dia_em DATE,
        estado TEXT,
        assunto TEXT)
    """)
