import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def app():
    # st.title("Correlation Analysis")
    # script_path = os.path.dirname(__file__)
    # file_path = os.path.join(script_path, '../student_data 2.csv')

    df = pd.read_csv('student_data.csv')
    st.write("Dataframe Preview:", df.head())
    
    # Select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=['number'])
    
    # Handle missing values (if any)
    numeric_df = numeric_df.dropna()
    
    # Compute the correlation matrix
    corr = numeric_df.corr()
    
    # Plot the correlation matrix
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.write(fig)

