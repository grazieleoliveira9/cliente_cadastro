import streamlit as st
import pandas as pd


st.title("Cadastro de cliente")

def form_cadastro():
    
    st.text_input("Nome do cliente", key="name", placeholder="Nome/Razão Social", max_chars=50)
    col1, col2 = st.columns(2)

    with col1: st.radio("Digite o tipo de pessoa", key="tipo", options=["Pessoa Física", "Pessoa Jurídica"]),
    

    with col2:
        st.text_input("CPF/CNPJ", key="cpf_cnpj", placeholder="000.000.000-00 ou 00.000.000/0000-00", max_chars=15,)




    st.text_input("Email:", key="email", placeholder="joao@gmail.com", max_chars=50)
    col3, col4 = st.columns(2)

    with col3:
        st.text_input("Telefone fixo:", key="fixo", placeholder="Ex: (XX) XXXX-XXXX", max_chars=15)


    with col4:

        st.text_input("Telefone celular:", key="celular", placeholder="Ex: (XX) XXXX-XXXX", max_chars=14)

    st.text_input("Endereço:", key="endereço", placeholder="Rua, Avenida", max_chars=50)


    col4, col5 = st.columns(2)

    with col4:
        st.text_input("Nº casa/apto:", key="casa", placeholder="Número", max_chars=10)

    
    st.text_input("Bairro:", key="bairro", placeholder="Bairro", max_chars=40)


    st.text_input("Cidade:", key="cidade", placeholder="Cidade", max_chars=40)

    with col5:
        st.text_input("Complemento:", key="complemento", placeholder="", max_chars=50)



    col6, col7 = st.columns(2)

    with col6:
        st.text_input("CEP:", key="cep", placeholder="Ex: 00000-000", max_chars=8)

    with col7:
        st.text_input("UF:", key="uf", placeholder="UF", max_chars=2)
    


    
    
  
    
    





form_cadastro()



# if col1 == "Pessoa Física":
#     st.text_input("CPF", key="cpf")
# elif col1 == "Pessoa Juridica":
#     st.text_input("CNPJ", key="cnpj")



