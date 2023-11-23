# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:36:07 2023

@author: jperezr
"""



import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

# Configure the Streamlit page
st.set_page_config(
    page_title="",
    layout="wide"
)

# Add a title
st.title("Creado por: Javier Horacio Pérez Ricárdez")

# Import your data
df = pd.read_csv("Libro1.csv")

# Generate the HTML using Pygwalker
pyg_html = pyg.walk(df, return_html=True)

# Embed the generated HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)