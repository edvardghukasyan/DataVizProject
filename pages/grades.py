import streamlit as st
import pandas as pd
import plotly.express as px
import os


def app():
    st.title("Grades Distribution")

    script_path = os.path.dirname(__file__)
    file_path = os.path.join(script_path, '../student_data 2.csv')

    df = pd.read_csv(file_path)

    fig = px.histogram(df, x='G3', nbins=20, title="Final Grade Distribution (G3)")
    st.plotly_chart(fig)