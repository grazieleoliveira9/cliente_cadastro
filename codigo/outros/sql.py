import sqlite3

con = sqlite3.connect('dados.db')
con.execute("PRAGMA foreign_keys = ON;")

instructions = """\
CREATE TABLE if not exists Cliente (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(50) DEFAULT 'Varchar(50)'
);

CREATE TABLE if not exists Servico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INT,
    id_servico INT,
    nome VARCHAR(50),
    data_prevista DATE,
    data_real DATE,
    FOREIGN KEY(id_cliente) REFERENCES Cliente(id_cliente)
);

CREATE TABLE if not exists Pagamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INT,
    id_servico INT,
    id_pgto INT,
    valor FLOAT,
    data_pgto DATE,
    num_parcelas INT,
    id_tipo_de_pgto INT,
    FOREIGN KEY(id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY(id_servico) REFERENCES Servico(id_servico),
    FOREIGN KEY(id_tipo_de_pgto) REFERENCES Tipo_pgto(id_tipo_de_pgto)
);

CREATE TABLE if not exists Tipo_pgto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_tipo_pgto INT,
    ds_tipo_pgto VARCHAR(50)
);

CREATE TABLE if not exists Contato (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INT,
    id_contato INT,
    contato VARCHAR(50),
    id_tipo_contato INT,
    FOREIGN KEY(id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY(id_tipo_contato) REFERENCES Tipo_contato(id_tipo_contato)
);

CREATE TABLE if not exists Tipo_contato (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_tipo_contato INT,
    ds_tipo_contato VARCHAR(50)
);

CREATE TABLE if not exists Pessoa_fisica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INT,
    cpf VARCHAR(11),
    RG VARCHAR(20),
    FOREIGN KEY(id_cliente) REFERENCES Cliente(id_cliente)
);

CREATE TABLE if not exists Pessoa_juridica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INT,
    inscricao_estad VARCHAR(20),
    CNPJ VARCHAR(14),
    FOREIGN KEY(id_cliente) REFERENCES Cliente(id_cliente)
);

CREATE TABLE if not exists Endereco (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INT,
    id_endereco INT,
    avenida VARCHAR(50),
    cep VARCHAR(8),
    complemento VARCHAR(50),
    numero VARCHAR(10),
    bairro VARCHAR(50),
    rua VARCHAR(50),
    uf VARCHAR(2),
    FOREIGN KEY(id_cliente) REFERENCES Cliente(id_cliente)
);
"""

for instruction in instructions.split(";"):
    if instruction.strip():
        con.execute(instruction)

con.close()