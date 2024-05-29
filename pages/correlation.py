import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def app():
    st.title("Correlation Analysis")
    script_path = os.path.dirname(__file__)
    file_path = os.path.join(script_path, '../student_data 2.csv')

    df = pd.read_csv(file_path)
    corr = df.corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.write(fig)