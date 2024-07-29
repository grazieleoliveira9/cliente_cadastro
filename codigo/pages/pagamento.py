import streamlit as st
import pandas as pd




st.title("Pagamento")

if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame(columns=['Tabela de Pagamento', 'Valor', 'Data', 'Forma de Pagamento', 'N° de Recibo', 'Parcelas'])

def salvar_dados_txt(dados, filename='dados_pagamento.txt'):
    with open(filename, 'a') as f:
        f.write(f"Tabela de Pagamento: {dados['Tabela de Pagamento'][0]}\n")
        f.write(f"Valor: {dados['Valor'][0]}\n")
        f.write(f"Data: {dados['Data'][0]}\n")
        f.write(f"Forma de Pagamento: {dados['Forma de Pagamento'][0]}\n")
        f.write(f"N° de Recibo: {dados['N° de Recibo'][0]}\n")
        f.write(f"Parcelas: {dados['Parcelas'][0]}\n")
        f.write("\n")


def pagamento():
   
    col1, col2, col3 = st.columns(3)

    with col1: form_pgto = st.radio("Forma de pagamento", options=["Cartão de Crédito", "Cartão de Débito", "Pix", "Dinheiro"])
    
    parcelas = ''
    if form_pgto == "Cartão de Crédito":
        parcelas = st.radio("Número de parcelas", options=["1x", "2x", "3x", "4x"], horizontal=True)

    

    with col2:
        d = st.date_input("Data de Pagamento", format="DD/MM/YYYY")


    with col3:
        numero = st.text_input("Número do recibo/nota fiscal",  placeholder="", max_chars=10)



    valor = st.text_input("Valor do pagamento",  placeholder="", max_chars=10)

    botao =st.button("Concluir pedido")

    if botao:
         novo_pgto = pd.DataFrame({
            'Tabela de Pagamento': [''],
            'Valor': [valor],
            'Data': [d], 
            'Forma de Pagamento': [form_pgto],
            'N° de Recibo': [numero],
            'Parcelas': [parcelas]
        })
         st.session_state['df'] = pd.concat([st.session_state['df'], novo_pgto], ignore_index=True)
         salvar_dados_txt(novo_pgto)
         st.success('Pagamento concluído!', icon="✅")


        

    st.dataframe(st.session_state['df'])




pagamento()







