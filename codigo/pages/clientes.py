import streamlit as st



st.title("Listagem de clientes")

if 'df' in st.session_state:
    st.table(st.session_state['df'])



