import streamlit as st

# Define the sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Pages", ["Welcome", "Correlation Analysis", "Grades Distribution", "Pair Plots"])

# Welcome page
if page == "Welcome":
    st.title("Welcome to the Student Performance Dashboard")
    st.write("""
    This dashboard provides an analysis of student performance data.
    Use the navigation sidebar to explore different aspects of the data.
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