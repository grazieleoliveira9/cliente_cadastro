import streamlit as st
import pandas as pd
from core.db import conectar_banco, criar_tabela, inserir_cliente, adicionar_coluna_nome,  excluir_coluna, colunas_existentes
import streamlit as st
import pandas as pd
from core.logger import logger
from datetime import datetime

conn, c = conectar_banco()
# criar_tabela(c)
# adicionar_coluna_nome(c) 
# colunas_existentes(c)
# ordernar_colunas(c)


try: 


    st.title("Cadastro de cliente")
    # st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
    st.subheader ("Insira os dados do cliente", divider=True)


    def limpar_campos():
        st.session_state['Nome'] = ""
        st.session_state['cpf_cnpj'] = ""
        st.session_state['fisica_juridica'] = ""
        st.session_state['email'] = ""
        st.session_state['telefone_fixo'] = ""
        st.session_state['telefone_celular'] = ""
        st.session_state['endereco'] = ""
        st.session_state['numero'] = ""
        st.session_state['bairro'] = ""
        
        st.session_state['cidade'] = ""
        st.session_state['complemento'] = ""
        st.session_state['cep'] = ""
        st.session_state['uf'] = ""

    if 'df' not in st.session_state:
        st.session_state['df'] = pd.DataFrame(columns=['Data','Nome', 'CPF/CNPJ', 'Fisica/Juridica', 'Email', 'Telefone fixo', 'Telefone celular', 'Endereço', 'Nº casa/apto', 'Bairro', 'Cidade', 'Complemento', 'CEP', 'UF'])

    def salvar_dados_txt(dados, filename='clientes.txt'):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"Data: {dados['Data'][0]}\n")
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
    
        col10 = st.columns(2)
        with col10[0]:
            data = st.date_input("Data de Cadastro", format="DD/MM/YYYY")
            data_obj = data.strftime("%Y-%m-%d")
        


        nome =st.text_input("Nome do cliente",  placeholder="Nome/Razão Social", max_chars=50)


        col1, col2 = st.columns(2)

        with col1: pessoa = st.radio("Escolha uma opção", options=["Pessoa Física", "Pessoa Jurídica"])


        with col2:

            if pessoa == "Pessoa Física":
                cpf_cnpj = st.text_input("CPF:", placeholder="000.000.000-00", max_chars=11)

            else:
                cpf_cnpj = st.text_input("CNPJ:", placeholder="00.000.000/0000-00", max_chars=14)
        
            

        # col9, col10 = st.columns(2)

        email = st.text_input("Email:", placeholder="Ex: joao@gmail.com", max_chars=50)
        

        # with col10: codigo = random.randint(1000, 9999)


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
            logger.info("Cadastrando dados do cliente...")

            novo_cadastro = pd.DataFrame({
                'Data': [str(data_obj)],
                'Nome': [str(nome)],
                'CPF/CNPJ': [str(cpf_cnpj)],
                'Fisica/Juridica': [str(pessoa)],
                'Email': [str(email)],
                'Telefone fixo': [str(telefone_fixo)],
                'Telefone celular': [str(telefone_celular)],
                'Endereço': [str(endereco)],
                'Nº casa/apto': [str(numero)],
                'Bairro': [str(bairro)],
                'Cidade': [str(cidade)],
                'Complemento': [str(complemento)],
                'CEP': [str(cep)],
                'UF': [str(uf)]
            })
        
       
        if not nome or not cpf_cnpj or not pessoa or not email or not telefone_fixo or not telefone_celular or not endereco or not numero or not bairro or not cidade or not complemento or not cep or not uf:
            st.warning('Preencha todos os campos!', icon="⚠️")
            logger.warning('Campos nao preenchidos, cadastro nao realizado!')

        else:
            st.success('Cadastrado com sucesso!', icon="✅")

        


            st.session_state['df'] = pd.concat([st.session_state['df'], novo_cadastro], ignore_index=True)
            salvar_dados_txt(novo_cadastro)

            # Inserir no banco de dados SQLite
            inserir_cliente(c, conn, novo_cadastro)
            limpar_campos()
            logger.info('Cadastrado de cliente feito com sucesso!')

            


            # if 'nome' not in st.session_state:
            #     limpar_campos()

            # limpar_campos()

    form_cadastro()

    conn.close()
except Exception as e:
    logger.error(f"Erro ao cadastrar cliente: {str(e)}", exc_info=True)









