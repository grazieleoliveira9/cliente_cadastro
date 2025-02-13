import sqlite3
from core.logger import logger

# Conectar ao banco de dados SQLite (ou criar se não existir)
def conectar_banco():
    conn = sqlite3.connect('clientes.db')  # Nome do banco de dados
    
    c = conn.cursor()
    return conn, c

def criar_tabela(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data DATE,
            nome TEXT NOT NULL,
            cpf_cnpj INT,
            fisica_juridica TEXT,
            email TEXT,
            telefone_fixo INT,
            telefone_celular INT,
            endereco TEXT,
            numero INT,
            bairro TEXT,
            cidade TEXT,
            complemento TEXT,
            cep INT,
            uf TEXT,
            RG INT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Valor REAL,
            Data DATE,
            Forma_de_Pagamento INT,
            N°_de_Recibo INT,
            Parcelas INT,
            id_cliente INTEGER,
            nome_cliente TEXT,
            servico TEXT,
            FOREIGN KEY(id_cliente) REFERENCES clientes(id)
        )
    ''')

def adicionar_coluna_nome(cursor):
    cursor.execute('PRAGMA table_info(clientes)')
    colunas = [info[1] for info in cursor.fetchall()] 
    if 'servico' not in colunas:
        cursor.execute('''
            ALTER TABLE pagamentos
            ADD COLUMN servico TEXT
        ''')
        print("Coluna 'Servico' adicionada à tabela 'clientes'.")
        logger.info("Coluna 'Servico' adicionada à tabela 'clientes'.")
    else:
        print("Coluna 'Servico' já existente na tabela 'clientes'.")
        logger.warning("Coluna 'Servico' já existente na tabela 'clientes'.")

# Função para inserir dados no banco de dados
def inserir_cliente(cursor, conn, dados):
    cursor.execute('''
        INSERT INTO clientes (
           data, nome, cpf_cnpj, fisica_juridica, email, telefone_fixo, telefone_celular,
            endereco, numero, bairro, cidade, complemento, cep, uf, rg
        )
        VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        dados['Data'][0], dados['Nome'][0], dados['CPF/CNPJ'][0], dados['Fisica/Juridica'][0],
        dados['Email'][0], dados['Telefone fixo'][0], dados['Telefone celular'][0],
        dados['Endereço'][0], dados['Nº casa/apto'][0], dados['Bairro'][0],
        dados['Cidade'][0], dados['Complemento'][0], dados['CEP'][0], dados['UF'][0], dados['RG'][0]
    ))
    
    conn.commit()

def inserir_pagamento(cursor, conn, dados_pagamento, id_cliente, nome_cliente ):
    cursor.execute('''
        INSERT INTO pagamentos (
            valor, data, Forma_de_Pagamento, N°_de_Recibo, Parcelas, id_cliente, nome_cliente, servico
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        
        
        dados_pagamento['Valor'][0], dados_pagamento['Data'][0], 
        dados_pagamento['Forma_de_Pagamento'][0], dados_pagamento['N°_de_Recibo'][0],
        dados_pagamento['Parcelas'][0],      
        id_cliente, 
        nome_cliente,
        dados_pagamento['servico'][0]
    ))
    conn.commit()

  

def buscar_clientes(cursor):
    cursor.execute('SELECT Nome FROM clientes ORDER BY Nome DESC')
    clientes = [cliente[0] for cliente in cursor.fetchall()]
    # logger.info(f"Clientes encontrados: {clientes}")
    return clientes

def buscar_pagamentos(cursor):
    cursor.execute('SELECT * FROM pagamentos')
    return cursor.fetchall()


def excluir_coluna(cursor):
    cursor.execute('PRAGMA table_info(pagamentos)')
    colunas = [info[1] for info in cursor.fetchall()]  # Lista de colunas existentes
    if 'id_cliente' in colunas:
        cursor.execute('''
            ALTER TABLE pagamentos 
            DROP COLUMN id_cliente
        ''')
        logger.info("Coluna 'id_cliente' excluida da tabela 'pagamentos'.")

    else:
        logger.error("Coluna 'servico' nao existente na tabela 'pagamentos'.")


def colunas_existentes(cursor):
    cursor.execute('PRAGMA table_info(pagamentos)')
    colunas = [info[1] for info in cursor.fetchall()]  # Lista de colunas existentes
    print(colunas)
    return colunas


