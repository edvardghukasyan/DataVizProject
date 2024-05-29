import streamlit as st
import pandas as pd
import plotly.express as px
import os


import streamlit as st
import pandas as pd
import plotly.express as px
import os

def app():
    st.title("Grades Distribution")

    # Load the data
    base_path = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(base_path, '..', 'student_data 2.csv'))
    df = pd.read_csv(file_path)

    # Dropdown menu for selecting the grade group
    grade_group = st.selectbox(
        'Select the grade group to visualize',
        ('G1', 'G2', 'G3')
    )

    # Display the selected grade group
    st.write(f"Visualizing the distribution of {grade_group}")

    # Histogram for the selected grade group
    fig = px.histogram(df, x=grade_group, nbins=20, title=f"Distribution of {grade_group}")
    st.plotly_chart(fig)

    # Button to save the selection
    if st.button('Save Selection'):
        with open('selected_grade_group.txt', 'w') as f:
            f.write(grade_group)
        st.success(f'Selection saved: {grade_group}')

# Only run the app if this file is executed directly
if __name__ == "__main__":
    app()
