import streamlit as st
from src.components.header import render_header

def home_screen():
    render_header(
        title="AI Attendance System",
        description="A simple, automated attendance tracking system powered by classroom photos and voice recognition."
    )

    # Security & placeholder notice
    st.info("System Notice: Navigation placeholder mode. Authentication and database integration will be connected in future steps.")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Student")
            st.write("Join registered subjects, track your attendance summary, and view session history.")
            if st.button("Open Student Dashboard", key="btn_student_portal", type="primary", use_container_width=True):
                if "pages" in st.session_state and "Student Dashboard" in st.session_state["pages"]:
                    st.switch_page(st.session_state["pages"]["Student Dashboard"])

    with col2:
        with st.container(border=True):
            st.subheader("Teacher")
            st.write("Manage classes and subjects, conduct photo or voice attendance, and review student attendance reports.")
            if st.button("Open Teacher Dashboard", key="btn_teacher_portal", type="primary", use_container_width=True):
                if "pages" in st.session_state and "Teacher Dashboard" in st.session_state["pages"]:
                    st.switch_page(st.session_state["pages"]["Teacher Dashboard"])

    st.subheader("How Attendance Works")
    col_a, col_b = st.columns(2)
    with col_a:
        with st.container(border=True):
            st.markdown("**Photo-Based Attendance**")
            st.caption("The teacher uploads or captures a classroom photo, and pretrained face recognition identifies registered students present.")
    with col_b:
        with st.container(border=True):
            st.markdown("**Voice-Based Attendance**")
            st.caption("Students individually speak an agreed phrase, and pretrained speaker recognition verifies attendance.")

if __name__ == "__main__":
    home_screen()
