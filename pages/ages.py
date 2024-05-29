import streamlit as st
import pandas as pd
import plotly.express as px
import os

def app():
    st.title("Ages and Groups Analysis")

    # Load the data
    df = pd.read_csv('student_data.csv')


    # Histogram for age distribution
    fig_age = px.histogram(df, x='age', nbins=20, title="Distribution of Ages")
    st.plotly_chart(fig_age)

    # Boxplot for ages by group (e.g., sex, address)
    group_by = st.selectbox(
        'Select the group to visualize ages by',
        ('sex', 'address', 'Pstatus')
    )

    fig_group = px.box(df, x=group_by, y='age', title=f"Ages by {group_by.capitalize()}")
    st.plotly_chart(fig_group)

    # Save the selection
    if st.button('Save Selection'):
        with open('selected_age_group.txt', 'w') as f:
            f.write(group_by)
        st.success(f'Selection saved: {group_by}')

# Only run the app if this file is executed directly
if __name__ == "__main__":
    app()
