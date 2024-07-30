import sqlite3

con = sqlite3.connect('dados.db')
con.execute("PRAGMA foreign_keys = ON;")

instructions = """\
SELECT id, col2, NOME, EMAIL, TELEFONE_FIXO, TELEFONE_CELULAR, ENDERECO, NUMERO, BAIRRO, CIDADE, COMPLEMENTO, CEP, UF
FROM CLIENTES;
"""

cur = con.cursor()
result = cur.execute(instructions)
# con.close()
for row in result:
    print(row)



