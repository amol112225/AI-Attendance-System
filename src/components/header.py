import streamlit as st

def render_header(title: str = "AI Attendance System", description: str | None = None):
    """Render a clean, standard header across pages."""
    st.title(title)
    if description:
        st.write(description)
    st.divider()

def header_home():
    """Backward-compatible header for existing references."""
    render_header(
        title="AI Attendance System",
        description="A simple, automated attendance tracking system powered by classroom photos and voice recognition."
    )
