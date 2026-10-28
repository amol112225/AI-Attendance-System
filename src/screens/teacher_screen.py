import streamlit as st
from src.components.header import render_header

def teacher_screen():
    render_header(
        title="Teacher Dashboard",
        description="Manage subjects, conduct photo or voice attendance, and view attendance reports."
    )

    # Security & placeholder notice
    st.info("Placeholder Mode: This dashboard is not yet connected to Supabase Auth or database records. Teacher permissions and real student data will be enforced in future steps.")

    if st.button("← Back to Home", key="btn_back_home_teacher"):
        if "pages" in st.session_state and "Home" in st.session_state["pages"]:
            st.switch_page(st.session_state["pages"]["Home"])

    # 1. Subjects & Enrolled Students
    col_subj, col_stud = st.columns(2)
    with col_subj:
        with st.container(border=True):
            st.subheader("Subjects")
            st.caption("Manage your assigned courses.")
            st.text("• CS501 - Artificial Intelligence (Sample)")
            st.text("• CS502 - Computer Networks (Sample)")
            st.button("+ Add New Subject", disabled=True)

    with col_stud:
        with st.container(border=True):
            st.subheader("Enrolled Students")
            st.caption("View student rosters for your subjects.")
            st.text("Roster data will load after database connection.")
            st.button("View Student Roster", disabled=True)

    # 2. Two Visually Distinct Attendance Methods
    st.subheader("Conduct Attendance Session")
    col_photo, col_voice = st.columns(2)

    with col_photo:
        with st.container(border=True):
            st.markdown("### 📷 Photo-Based Attendance")
            st.write("Capture or upload classroom photos to automatically detect and mark present students using face recognition.")
            st.button("Start Photo Session (Placeholder)", disabled=True, use_container_width=True)
            st.caption("AI face-recognition model is not loaded in this step.")

    with col_voice:
        with st.container(border=True):
            st.markdown("### 🎙️ Voice-Based Attendance")
            st.write("Record students speaking an agreed pass-phrase to identify and verify each speaker.")
            st.button("Start Voice Session (Placeholder)", disabled=True, use_container_width=True)
            st.caption("AI speaker-recognition model is not loaded in this step.")

    # 3. Attendance Records and Reports
    with st.container(border=True):
        st.subheader("Attendance Records & Reports")
        st.write("Review session logs, export class attendance spreadsheets, and identify absent students.")
        st.button("Export Report (Placeholder)", disabled=True)
        st.caption("Reporting queries will be enabled once database schema and records are ready.")

if __name__ == "__main__":
    teacher_screen()
