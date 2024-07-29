import streamlit as st
import pandas as pd
import numpy as np

from datetime import date

df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)

st.table(df)

