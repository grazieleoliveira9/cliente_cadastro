import streamlit as st
import pandas as pd
import numpy as np

from datetime import date
from main import form_cadastro


st.title("Listagem de clientes")

if 'df' in st.session_state:
    st.table(st.session_state['df'])



