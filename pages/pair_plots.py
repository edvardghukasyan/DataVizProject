import streamlit as st
import pandas as pd
import seaborn as sns
import os

def app():
    # st.title("Pair Plots")
    # script_path = os.path.dirname(__file__)
    # file_path = os.path.join(script_path, '../student_data 2.csv')

    df = pd.read_csv('student_data.csv')
    fig = sns.pairplot(df, hue='G3')
    st.pyplot(fig)
