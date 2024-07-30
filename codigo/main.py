import streamlit as st
import pandas as pd


st.title("Cadastro de cliente")

if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame(columns=['Nome', 'CPF/CNPJ', 'Fisica/Juridica', 'Email', 'Telefone fixo', 'Telefone celular', 'Endereço', 'Nº casa/apto', 'Bairro', 'Cidade', 'Complemento', 'CEP', 'UF'])

def salvar_dados_txt(dados, filename='clientes.txt'):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"Nome: {dados['Nome'][0]}\n")
        f.write(f"CPF/CNPJ: {dados['CPF/CNPJ'][0]}\n")
        f.write(f"Fisica/Juridica: {dados['Fisica/Juridica'][0]}\n")
        f.write(f"Email: {dados['Email'][0]}\n")
        f.write(f"Telefone fixo: {dados['Telefone fixo'][0]}\n")
        f.write(f"Telefone celular: {dados['Telefone celular'][0]}\n")
        f.write(f"Endereço: {dados['Endereço'][0]}\n")
        f.write(f"Nº casa/apto: {dados['Nº casa/apto'][0]}\n")
        f.write(f"Bairro: {dados['Bairro'][0]}\n")
        f.write(f"Cidade: {dados['Cidade'][0]}\n")
        f.write(f"Complemento: {dados['Complemento'][0]}\n")
        f.write(f"CEP: {dados['CEP'][0]}\n")
        f.write(f"UF: {dados['UF'][0]}\n")
        f.write("\n")

def form_cadastro():
    
    nome =st.text_input("Nome do cliente",  placeholder="Nome/Razão Social", max_chars=50)

    col1, col2 = st.columns(2)

    with col1: pessoa = st.radio("Digite o tipo de pessoa", options=["Pessoa Física", "Pessoa Jurídica"])


    

    with col2:
        # cpf_cnpj = st.text_input("CPF/CNPJ", placeholder="000.000.000-00 ou 00.000.000/0000-00", max_chars=15,)

        if pessoa == "Pessoa Física":
            st.text_input("CPF:", placeholder="000.000.000-00", max_chars=11)

        else:
            st.text_input("CNPJ:", placeholder="00.000.000/0000-00", max_chars=14)
      







    email = st.text_input("Email:", placeholder="joao@gmail.com", max_chars=50)

    col3, col4 = st.columns(2)

    with col3:
        telefone_fixo = st.text_input("Telefone fixo:", placeholder="Ex: (XX) XXXX-XXXX", max_chars=15)


    with col4:

       telefone_celular = st.text_input("Telefone celular:",  placeholder="Ex: (XX) XXXX-XXXX", max_chars=14)

    endereco = st.text_input("Endereço:",  placeholder="Rua, Avenida", max_chars=50)


    col4, col5 = st.columns(2)

    with col4:
        numero = st.text_input("Nº casa/apto:", placeholder="Número", max_chars=10)

    
    bairro = st.text_input("Bairro:", placeholder="Bairro", max_chars=40)


    cidade = st.text_input("Cidade:", placeholder="Cidade", max_chars=40)

    with col5:
        complemento = st.text_input("Complemento:", placeholder="", max_chars=50)



    col6, col7 = st.columns(2)

    with col6:
        cep = st.text_input("CEP:", placeholder="Ex: 00000-000", max_chars=8)

    with col7:
        uf = st.text_input("UF:", placeholder="UF", max_chars=2)
    


    botao_cadastro = st.button("Cadastrar")

    if botao_cadastro:

        novo_cadastro = pd.DataFrame({
            'Nome': [nome],
            'CPF/CNPJ': [col2],
            'Fisica/Juridica': [pessoa],
            'Email': [email],
            'Telefone fixo': [telefone_fixo],
            'Telefone celular': [telefone_celular],
            'Endereço': [endereco],
            'Nº casa/apto': [numero],
            'Bairro': [bairro],
            'Cidade': [cidade],
            'Complemento': [complemento],
            'CEP': [cep],
            'UF': [uf]
        })
        st.session_state['df'] = pd.concat([st.session_state['df'], novo_cadastro], ignore_index=True)
        salvar_dados_txt(novo_cadastro)
        st.success('Cadastrado com sucesso!', icon="✅")



form_cadastro()






