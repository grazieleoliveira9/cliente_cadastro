import sqlite3

# Conectar ao banco de dados SQLite (ou criar se não existir)
def conectar_banco():
    conn = sqlite3.connect('clientes.db')  # Nome do banco de dados
    
    c = conn.cursor()
    return conn, c

# Criar a tabela de clientes (se não existir)
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
            uf TEXT
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
            FOREIGN KEY(id_cliente) REFERENCES clientes(id)
        )
    ''')

def adicionar_coluna_nome(cursor):
    cursor.execute('PRAGMA table_info(clientes)')
    colunas = [info[1] for info in cursor.fetchall()] 
    if 'Nome' not in colunas:
        cursor.execute('''
            ALTER TABLE clientes
            ADD COLUMN Nome TEXT
        ''')
        print("Coluna 'Nome' adicionada à tabela 'clientes'.")
    else:
        print("Coluna 'Nome' já existente na tabela 'clientes'.")

# Função para inserir dados no banco de dados
def inserir_cliente(cursor, conn, dados):
    cursor.execute('''
        INSERT INTO clientes (
           data, nome, cpf_cnpj, fisica_juridica, email, telefone_fixo, telefone_celular,
            endereco, numero, bairro, cidade, complemento, cep, uf
        )
        VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        dados['Data'][0], dados['Nome'][0], dados['CPF/CNPJ'][0], dados['Fisica/Juridica'][0],
        dados['Email'][0], dados['Telefone fixo'][0], dados['Telefone celular'][0],
        dados['Endereço'][0], dados['Nº casa/apto'][0], dados['Bairro'][0],
        dados['Cidade'][0], dados['Complemento'][0], dados['CEP'][0], dados['UF'][0]
    ))
    
    conn.commit()

def inserir_pagamento(cursor, conn, dados_pagamento, id_cliente, nome_cliente ):
    cursor.execute('''
        INSERT INTO pagamentos (
            valor, data, Forma_de_Pagamento, N°_de_Recibo, Parcelas, id_cliente, nome_cliente
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        
        
        dados_pagamento['Valor'][0], dados_pagamento['Data'][0], 
        dados_pagamento['Forma_de_Pagamento'][0], dados_pagamento['N°_de_Recibo'][0],
        dados_pagamento['Parcelas'][0], id_cliente, nome_cliente
    ))
    conn.commit()

  

def buscar_clientes(cursor):
    cursor.execute('SELECT * FROM clientes')
    return cursor.fetchall()

def buscar_pagamentos(cursor):
    cursor.execute('SELECT * FROM pagamentos')
    return cursor.fetchall()


def excluir_coluna(cursor):
    cursor.execute('PRAGMA table_info(pagamentos)')
    colunas = [info[1] for info in cursor.fetchall()]  # Lista de colunas existentes
    if 'data_prevista' in colunas:
        cursor.execute('''
            ALTER TABLE pagamentos
            DROP COLUMN data_prevista
        ''')
        print("Coluna 'data_prevista' excluida da tabela 'pagamentos'.")

    else:
        print("Coluna 'data_prevista' nao existente na tabela 'pagamentos'.")


def colunas_existentes(cursor):
    cursor.execute('PRAGMA table_info(pagamentos)')
    colunas = [info[1] for info in cursor.fetchall()]  # Lista de colunas existentes
    print(colunas)
    return colunas


