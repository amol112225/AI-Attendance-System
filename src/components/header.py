import streamlit as st
from src.styles.theme import apply_theme

def render_header(title: str = "AI Attendance System", description: str | None = None):
    """Render a clean, standard header across pages with centralized styling applied."""
    apply_theme()
    st.title(title)
    if description:
        st.write(description)
    st.divider()

def header_home():
    """Backward-compatible header for existing references."""
    render_header(
        title="AttendAI",
        description="Attendance, Made Intelligent."
    )
