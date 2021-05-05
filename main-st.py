import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# %matplotlib inline



st.title("streamlit超入門")

st.write("DataFrame")

tokyo_latlon = [35.69,139.70]

df = pd.DataFrame(
    np.random.randn(1000,2)/[10,10] + tokyo_latlon,
    columns=["lat","lon"]
)

if st.sidebar.checkbox("show data"):
    st.write(df)

if st.sidebar.checkbox("show map"):
    st.map(df)

if st.sidebar.checkbox("show image"):
    img = Image.open("Climber-1.jpg")
    st.image(img,caption="フーバー兄弟",use_column_width=True)



text = st.sidebar.text_input("あなたの趣味を教えて下さい")
condition = st.sidebar.slider("あなたの今の調子は？",0,100,50)

"あなたの趣味は：",text
"condition:",condition



