import streamlit as st

# Design Palette Tokens
COLOR_PRIMARY = "#1e3a8a"       # Dark Navy
COLOR_PRIMARY_HOVER = "#172554" # Deeper Navy for hover/active
COLOR_ACCENT = "#2563eb"        # Subtle secondary blue accent
COLOR_ACCENT_BG = "#eff6ff"     # Very soft blue tint
COLOR_BG_MAIN = "#ffffff"       # Clean white background
COLOR_BG_MUTED = "#f8fafc"      # Light neutral grey
COLOR_TEXT_MAIN = "#0f172a"     # Near-black readable text
COLOR_TEXT_MUTED = "#475569"    # Accessible secondary text
COLOR_BORDER = "#e2e8f0"        # Light neutral border
COLOR_FOCUS_RING = "#3b82f6"    # Visible focus indicator for accessibility

CUSTOM_CSS = f"""
<style>
/* Main app layout adjustments: reduce oversized empty padding */
.block-container {{
    padding-top: 2rem;
    padding-bottom: 2.5rem;
    max-width: 1200px;
}}

/* Typography: clear hierarchy and readable line-heights */
h1, h2, h3, h4 {{
    color: {COLOR_TEXT_MAIN};
    font-weight: 600;
    margin-bottom: 0.5rem;
}}

h1 {{
    font-size: 1.85rem !important;
}}

h2 {{
    font-size: 1.4rem !important;
}}

h3 {{
    font-size: 1.15rem !important;
}}

p, span, label {{
    color: {COLOR_TEXT_MAIN};
    font-size: 0.95rem;
}}

/* Accessible focus ring on all interactive elements */
button:focus-visible,
input:focus-visible,
textarea:focus-visible,
select:focus-visible {{
    outline: 2px solid {COLOR_FOCUS_RING} !important;
    outline-offset: 2px !important;
}}

/* Button styling: clean primary and secondary styling */
button[kind="primary"] {{
    background-color: {COLOR_PRIMARY} !important;
    color: #ffffff !important;
    border: 1px solid {COLOR_PRIMARY} !important;
    border-radius: 6px !important;
    font-weight: 500 !important;
}}

button[kind="primary"]:hover {{
    background-color: {COLOR_PRIMARY_HOVER} !important;
    border-color: {COLOR_PRIMARY_HOVER} !important;
}}

button[kind="secondary"] {{
    background-color: #ffffff !important;
    color: {COLOR_TEXT_MAIN} !important;
    border: 1px solid {COLOR_BORDER} !important;
    border-radius: 6px !important;
}}

button[kind="secondary"]:hover {{
    background-color: {COLOR_BG_MUTED} !important;
    border-color: #cbd5e1 !important;
}}

/* Container borders: crisp, light neutral styling */
div[data-testid="stVerticalBlockBorderWrapper"] > div {{
    border-color: {COLOR_BORDER} !important;
    border-radius: 8px !important;
    background-color: #ffffff;
}}

/* Form inputs: consistent borders and clear typography */
div[data-baseweb="input"] {{
    border-radius: 6px !important;
    border-color: {COLOR_BORDER} !important;
}}

/* Dividers */
hr {{
    margin-top: 1rem !important;
    margin-bottom: 1.25rem !important;
    border-color: {COLOR_BORDER} !important;
}}

/* Alert boxes: maintain high contrast and clean padding */
div[data-testid="stAlert"] {{
    border-radius: 6px !important;
    padding: 0.75rem 1rem !important;
    font-size: 0.9rem !important;
}}
</style>
"""

def apply_theme():
    """Inject the centralized design CSS into the current page."""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

