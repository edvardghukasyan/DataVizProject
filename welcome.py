import streamlit as st

# Define the sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Pages", ["Welcome", "Correlation Analysis", "Grades Distribution", "Pair Plots", "Ages and Groups Analysis"])

# Navigation in the main section
if page == "Welcome":
    st.title("Welcome to the Student Performance Dashboard")
    st.write("""
    This dashboard provides an analysis of student performance data.
    Use the navigation sidebar to explore different aspects of the data.

    ### Data Overview
    The dataset includes various aspects of student performance, such as:
    - **Grades**: First period (G1), second period (G2), and final grade (G3)
    - **Demographic Information**: Age, sex, and address
    - **Family Background**: Parental education levels, family size, and status
    - **Study Information**: Study time, failures, and absences
    - **Extra Activities**: Participation in extracurricular activities, going out with friends, and health

    For more details, you can view the data [here](https://github.com/edvardghukasyan/DataVizProject/blob/main/student_data.csv).
    """)

# Import pages dynamically
elif page == "Correlation Analysis":
    from pages import correlation
    correlation.app()

elif page == "Grades Distribution":
    from pages import grades
    grades.app()

elif page == "Pair Plots":
    from pages import pair_plots
    pair_plots.app()

elif page == "Ages and Groups Analysis":
    from pages import ages
    ages.app()
