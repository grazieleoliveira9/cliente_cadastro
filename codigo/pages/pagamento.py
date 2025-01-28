import streamlit as st
import pandas as pd
from core.db import conectar_banco, criar_tabela, inserir_pagamento, buscar_clientes, atualizar_tabela_pagamentos
from core.logger import logger

conn, c = conectar_banco()
criar_tabela(c)
atualizar_tabela_pagamentos(c)

st.title("Pagamento")

if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame(columns=['Valor', 'Data', 'Forma de Pagamento', 'N° de Recibo', 'Parcelas', 'Nome'])

def salvar_dados_txt(dados, filename='dados_pagamento.txt'):
    with open(filename, 'a') as f:
        f.write(f"Valor: {dados['Valor'][0]}\n")
        f.write(f"Data: {dados['Data'][0]}\n")
        f.write(f"Forma de Pagamento: {dados['Forma de Pagamento'][0]}\n")
        f.write(f"N° de Recibo: {dados['N° de Recibo'][0]}\n")
        f.write(f"Parcelas: {dados['Parcelas'][0]}\n")
        f.write(f"Nome: {dados['Nome'][0]}\n")
        f.write("\n")


def pagamento():
    clientes = buscar_clientes(c)
    clientes_dict = {cliente[1]: cliente[0] for cliente in clientes} 
   
    cliente_selecionado = st.selectbox("Selecione o cliente", options=list(clientes_dict.keys()))

    col1, col2, col3 = st.columns(3)

    with col1: forma_pagamento = st.radio("Forma de pagamento", options=["Cartão de Crédito", "Cartão de Débito", "Pix", "Dinheiro"])
    
    parcelas = ''
    if forma_pagamento == "Cartão de Crédito":
        parcelas = st.radio("Número de parcelas", options=["1x", "2x", "3x", "4x"], horizontal=True)

    

    with col2:
        data = st.date_input("Data de Pagamento", format="DD/MM/YYYY")
        data_formatada = data.strftime('%d/%m/%Y')


    with col3:
        numero_recibo  = st.text_input("Número do recibo/nota fiscal",  placeholder="", max_chars=10)



    valor = st.text_input("Valor do pagamento",  placeholder="", max_chars=10)

    botao =st.button("Concluir pedido")

    if botao:
        id_cliente = clientes_dict[cliente_selecionado]
        nome_cliente = cliente_selecionado

        try:

            inserir_pagamento(c, conn, {
                    'Valor': [valor],  # Converte o valor para float
                    'Data': [data_formatada],  # Converte a data para string
                    'Forma_de_Pagamento': [forma_pagamento],
                    'N°_de_Recibo': [numero_recibo ],
                    'Parcelas': [int(parcelas[0]) if parcelas else None]
                }, id_cliente, nome_cliente)
            
            novo_pagamento = pd.DataFrame({
                'Valor': [valor],
                'Data': [data_formatada],
                'Forma de Pagamento': [forma_pagamento],
                'N° de Recibo': [numero_recibo],
                'Parcelas': [parcelas],
                'Nome': [nome_cliente]
          })
            st.session_state['df'] = pd.concat([st.session_state['df'], novo_pagamento], ignore_index=True)
            st.success('Pagamento concluído!', icon="✅")
            logger.info("Pagamento concluído")
        except Exception as e:
            st.error(f"Erro ao salvar pagamento no banco de dados: {e}")
            logger.error(f"Erro ao salvar pagamento: {e}")

    st.dataframe(st.session_state['df'])


pagamento()
conn.close()







