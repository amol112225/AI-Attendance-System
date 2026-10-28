import streamlit as st
from src.components.header import render_header

def student_screen():
    render_header(
        title="Student Dashboard",
        description="View your enrolled subjects and track your attendance records."
    )

    # Security & placeholder notice
    st.info("Placeholder Mode: This dashboard is not yet connected to Supabase Auth or database records. No personal student data is loaded.")

    if st.button("← Back to Home", key="btn_back_home_student"):
        if "pages" in st.session_state and "Home" in st.session_state["pages"]:
            st.switch_page(st.session_state["pages"]["Home"])


    # 1. Join a Subject
    with st.container(border=True):
        st.subheader("Join a Subject")
        st.write("Enter an invitation code or paste an invite link provided by your teacher.")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.text_input("Subject Code / Link", placeholder="e.g. CS501-2026 or https://...", disabled=True)
        with col2:
            st.button("Join Subject", disabled=True, use_container_width=True)
        st.caption("Subject enrollment will be available once the database is connected.")

    # 2. Enrolled Subjects
    with st.container(border=True):
        st.subheader("Enrolled Subjects")
        st.caption("Placeholder: When connected to the database, your active subjects will appear here.")
        subjects = ["Artificial Intelligence (CS501)", "Computer Networks (CS502)", "Database Systems (CS503)"]
        for subj in subjects:
            st.text(f"• {subj} (Sample)")

    # 3. Attendance Summary & History
    col_sum, col_hist = st.columns(2)
    with col_sum:
        with st.container(border=True):
            st.subheader("Attendance Summary")
            st.caption("Placeholder: Overall attendance metrics will display here.")
            st.metric(label="Overall Attendance", value="-- %")

    with col_hist:
        with st.container(border=True):
            st.subheader("Attendance History")
            st.caption("Placeholder: Recent session dates, photo/voice status, and timestamps will appear here.")
            st.text("No records loaded in placeholder mode.")

if __name__ == "__main__":
    student_screen()
