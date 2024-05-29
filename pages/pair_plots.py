import streamlit as st
import pandas as pd
import seaborn as sns
import os

def app():
    # st.title("Pair Plots")
    # script_path = os.path.dirname(__file__)
    # file_path = os.path.join(script_path, '../student_data 2.csv')

    # df = pd.read_csv('student_data.csv')
    # fig = sns.pairplot(df, hue='G3')
    # st.pyplot(fig)

    subset_columns = ['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']  # Adjust the column names as needed
    subset_df = df[subset_columns]
    
    # Generate the pair plot for the selected subset of columns
    pair_plot = sns.pairplot(subset_df)
    
    # Display the pair plot
    st.pyplot(pair_plot.fig)
