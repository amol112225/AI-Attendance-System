import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen

# Configure main application entry point
st.set_page_config(
    page_title="AI Attendance System",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Define native pages using Streamlit's multipage navigation API
pages = {
    "Home": st.Page(home_screen, title="Home", icon=":material/home:", default=True),
    "Student Dashboard": st.Page(student_screen, title="Student Dashboard", icon=":material/school:"),
    "Teacher Dashboard": st.Page(teacher_screen, title="Teacher Dashboard", icon=":material/co_present:"),
}

# Store page references in session state so on-page buttons can trigger st.switch_page
st.session_state["pages"] = pages

# Register native navigation
pg = st.navigation(
    {
        "Overview": [pages["Home"]],
        "Dashboards (Placeholders)": [pages["Student Dashboard"], pages["Teacher Dashboard"]],
    }
)

# Run active page
pg.run()
