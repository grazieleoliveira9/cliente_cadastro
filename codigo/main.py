import streamlit as st
import pandas as pd
from core.db import conectar_banco, criar_tabela, inserir_cliente, adicionar_coluna_nome,  excluir_coluna, colunas_existentes
import streamlit as st
import pandas as pd
from core.logger import logger

conn, c = conectar_banco()
criar_tabela(c)
# excluir_coluna(c)
# adicionar_coluna_nome(c) 
# colunas_existentes(c)
# ordernar_colunas(c)


try: 


    st.title("Cadastro de cliente")
    # st.subheader ("Insira os dados do cliente", divider=True)


    if 'df' not in st.session_state:
        st.session_state['df'] = pd.DataFrame(columns=['Data','Nome', 'CPF/CNPJ', 'Fisica/Juridica', 'Email', 'Telefone fixo', 'Telefone celular', 
                                                       'Endereço', 'Nº casa/apto', 'Bairro', 'Cidade', 'Complemento', 'CEP', 'UF', 'RG']
                                                       )

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
            f.write(f"RG: {dados['RG'][0]}\n")
            f.write("\n")



    def form_cadastro():
    
        col13 = st.columns(2)
        with col13[0]:
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
        
            

        st.subheader ("Contatos", divider=True)

        col3, col4 = st.columns(2)

        with col3:
            email = st.text_input("Email:", placeholder="Ex: joao@gmail.com", max_chars=50)
        
        with col4:
            rg = st.text_input("RG:", placeholder="Ex: 0.000.000", max_chars=7)
        
        



        col5, col6 = st.columns(2)

        with col5:
            telefone_fixo = st.text_input("Telefone fixo:", placeholder="Ex: (XX) XXXX-XXXX", max_chars=15)


        with col6:

            telefone_celular = st.text_input("Telefone celular:",  placeholder="Ex: (XX) XXXX-XXXX", max_chars=14)


        endereco = st.text_input("Endereço:",  placeholder="Rua, Avenida", max_chars=50)

        col7, col8 = st.columns(2)

        with col7:
            cep = st.text_input("CEP:", placeholder="Ex: 00000-000", max_chars=8)

        with col8:
            uf = st.selectbox(
                "UF:", placeholder="UF", options=["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", 
                                                  "RS", "RO", "RR", "SC", "SP", "SE", "TO"])



        col9, col10 = st.columns(2)

        with col9:
            numero = st.text_input("Nº casa/apto:", placeholder="Número", max_chars=10)

        with col10:
            bairro = st.text_input("Bairro:", placeholder="Bairro", max_chars=40)


        col11, col12 = st.columns(2)

        with col11:
            cidade = st.text_input("Cidade:", placeholder="Cidade", max_chars=40)

        with col12:
            complemento = st.text_input("Complemento:", placeholder="", max_chars=50)


        
        botao_cadastro = st.button("Cadastrar") 

        if botao_cadastro:
            logger.info("Cadastrando dados do cliente...")

        if not nome or not cpf_cnpj or not pessoa or not email or not telefone_fixo or not telefone_celular or not endereco or not numero or not bairro or not cidade or not cep or not uf:
            st.warning('Preencha todos os campos!', icon="⚠️")
            logger.error('Campos nao preenchidos, cadastro nao realizado!')

        else:
            if cpf_cnpj in st.session_state['df']['CPF/CNPJ'].values:
                st.warning('Cliente com este CPF/CNPJ já cadastrado!', icon="⚠️")
            else:
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
                    'UF': [str(uf)],
                    'RG': [str(rg)]
                })

                st.session_state['df'] = pd.concat([st.session_state['df'], novo_cadastro], ignore_index=True)
                salvar_dados_txt(novo_cadastro)
                inserir_cliente(c, conn, novo_cadastro)
                st.success('Cadastrado com sucesso!', icon="✅")
                logger.info("Cadastro foi efetuado com sucesso!")


            


    form_cadastro()

finally:
    conn.close()









