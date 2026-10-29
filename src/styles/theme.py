import textwrap
import streamlit as st

# AttendAI Design Palette
COLOR_NAVY_DEEP = "#0B1020"    # Canvas background
COLOR_NAVY_SURFACE = "#111A30" # Elevated panel surface
COLOR_NAVY_CARD = "#16203D"    # Card/container background
COLOR_BORDER = "#1E2A4A"       # Subtle border
COLOR_BORDER_VIOLET = "rgba(139, 92, 246, 0.28)"
COLOR_BORDER_CYAN = "rgba(34, 211, 238, 0.3)"
COLOR_VIOLET = "#8B5CF6"       # Violet accent
COLOR_CYAN = "#22D3EE"         # Cyan highlight
COLOR_TEXT_PRIMARY = "#F8FAFC" # Crisp white text
COLOR_TEXT_SECONDARY = "#A7B0C0" # Secondary readable slate
COLOR_SUCCESS = "#10B981"      # Status green
COLOR_WARNING = "#F59E0B"      # Status amber

CUSTOM_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

/* Strict No Animation Policy */
*, *::before, *::after {{
    animation: none !important;
    transition: none !important;
}}

html {{
    scroll-behavior: auto !important;
    background-color: {COLOR_NAVY_DEEP};
}}

body, .stApp {{
    background-color: {COLOR_NAVY_DEEP} !important;
    color: {COLOR_TEXT_PRIMARY} !important;
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif !important;
}}

/* Streamlit Container Layout */
.block-container {{
    padding-top: 1rem !important;
    padding-bottom: 3.5rem !important;
    max-width: 1180px !important;
}}

/* Ensure anchor links jump with clean clearance */
[id] {{
    scroll-margin-top: 1.5rem;
}}

/* Typography */
h1, h2, h3, h4, h5, h6 {{
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif !important;
    color: {COLOR_TEXT_PRIMARY} !important;
    font-weight: 700;
    letter-spacing: -0.025em;
}}

p, span, label, div {{
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    color: {COLOR_TEXT_PRIMARY};
}}

/* Heading Hierarchy */
h1 {{
    font-size: 2.35rem !important;
    line-height: 1.15 !important;
}}

h2 {{
    font-size: 1.5rem !important;
    line-height: 1.25 !important;
}}

h3 {{
    font-size: 1.15rem !important;
}}

/* Navbar Styling */
.navbar-wrapper {{
    background-color: {COLOR_NAVY_DEEP};
    border-bottom: 1px solid {COLOR_BORDER_VIOLET};
    padding: 12px 0 16px 0;
    margin-bottom: 2rem;
    position: relative;
    z-index: 100;
    width: 100%;
}}

.navbar-container {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1180px;
    margin: 0 auto;
    flex-wrap: wrap;
    gap: 16px;
    padding: 0 4px;
}}

.nav-brand {{
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none !important;
}}

.brand-text {{
    font-size: 1.35rem;
    font-weight: 800;
    color: {COLOR_TEXT_PRIMARY} !important;
    letter-spacing: -0.03em;
}}

.brand-accent {{
    color: {COLOR_CYAN};
}}

.nav-links {{
    display: flex;
    align-items: center;
    gap: 18px;
    list-style: none;
    margin: 0;
    padding: 0;
    flex-wrap: wrap;
}}

.nav-link {{
    color: {COLOR_TEXT_SECONDARY} !important;
    text-decoration: none !important;
    font-size: 0.88rem;
    font-weight: 500;
    padding: 4px 6px;
    white-space: nowrap;
}}

.nav-link:hover {{
    color: {COLOR_TEXT_PRIMARY} !important;
}}

.nav-status-badge {{
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(34, 211, 238, 0.08);
    border: 1px solid {COLOR_BORDER_CYAN};
    border-radius: 20px;
    padding: 4px 12px;
    color: {COLOR_CYAN};
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
    white-space: nowrap;
}}

.status-dot {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: {COLOR_CYAN};
    display: inline-block;
}}

/* Hero Section Elements */
.hero-content {{
    display: flex;
    flex-direction: column;
}}

.hero-label {{
    display: inline-block;
    align-self: flex-start;
    background: rgba(139, 92, 246, 0.12);
    border: 1px solid {COLOR_BORDER_VIOLET};
    border-radius: 6px;
    padding: 4px 10px;
    color: {COLOR_VIOLET};
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 0.85rem;
}}

.hero-title {{
    font-size: 2.6rem !important;
    font-weight: 800 !important;
    line-height: 1.15 !important;
    margin-bottom: 0.9rem !important;
    color: {COLOR_TEXT_PRIMARY} !important;
    letter-spacing: -0.025em !important;
}}

.hero-highlight {{
    color: {COLOR_CYAN};
}}

.hero-desc {{
    font-size: 1.02rem;
    line-height: 1.55;
    color: {COLOR_TEXT_SECONDARY};
    margin-bottom: 1.25rem;
}}

.feature-tag-pill {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: {COLOR_NAVY_SURFACE};
    border: 1px solid {COLOR_BORDER};
    border-radius: 6px;
    padding: 5px 12px;
    color: {COLOR_TEXT_PRIMARY};
    font-size: 0.82rem;
    font-weight: 600;
    margin-right: 8px;
    margin-bottom: 8px;
}}

.feature-dot-violet {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: {COLOR_VIOLET};
}}

.feature-dot-cyan {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: {COLOR_CYAN};
}}

.hero-indicator {{
    font-size: 0.82rem;
    color: {COLOR_TEXT_SECONDARY};
    margin-top: 0.75rem;
    padding-top: 0.75rem;
    border-top: 1px solid {COLOR_BORDER};
    font-style: italic;
}}

/* Standardized Content Panels */
div[data-testid="stVerticalBlockBorderWrapper"] > div {{
    border: 1px solid {COLOR_BORDER} !important;
    border-radius: 10px !important;
    background-color: {COLOR_NAVY_SURFACE} !important;
    padding: 1.25rem 1.4rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25) !important;
}}

/* Form inputs */
div[data-baseweb="input"] {{
    border-radius: 6px !important;
    border: 1px solid {COLOR_BORDER} !important;
    background-color: {COLOR_NAVY_DEEP} !important;
}}

div[data-baseweb="input"] input {{
    color: {COLOR_TEXT_PRIMARY} !important;
}}

/* Streamlit Native Dividers */
hr {{
    margin-top: 2rem !important;
    margin-bottom: 2.25rem !important;
    border: none !important;
    height: 1px !important;
    background: {COLOR_BORDER} !important;
}}

/* Section Headers */
.section-tag {{
    color: {COLOR_VIOLET};
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.35rem;
}}

.section-title {{
    color: {COLOR_TEXT_PRIMARY};
    font-size: 1.55rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
}}

.section-desc {{
    color: {COLOR_TEXT_SECONDARY};
    font-size: 0.92rem;
    line-height: 1.5;
    margin-bottom: 1.25rem;
}}

/* Responsive Workflow Grid */
.workflow-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 14px;
    width: 100%;
}}

@media (max-width: 1024px) {{
    .workflow-grid {{
        grid-template-columns: repeat(3, 1fr);
    }}
}}

@media (max-width: 640px) {{
    .workflow-grid {{
        grid-template-columns: 1fr;
    }}
}}

.workflow-step-card {{
    background: {COLOR_NAVY_SURFACE};
    border: 1px solid {COLOR_BORDER};
    border-radius: 8px;
    padding: 16px 14px;
    display: flex;
    flex-direction: column;
    min-height: 175px;
    box-sizing: border-box;
}}

.workflow-num {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 700;
    color: {COLOR_CYAN};
    background: rgba(34, 211, 238, 0.08);
    border: 1px solid rgba(34, 211, 238, 0.2);
    border-radius: 4px;
    padding: 2px 7px;
    display: inline-block;
    align-self: flex-start;
    margin-bottom: 10px;
}}

.workflow-step-title {{
    font-size: 0.92rem;
    font-weight: 700;
    color: {COLOR_TEXT_PRIMARY};
    margin-bottom: 6px;
    margin-top: 4px;
}}

.workflow-step-text {{
    font-size: 0.8rem;
    color: {COLOR_TEXT_SECONDARY};
    line-height: 1.45;
}}

/* Responsive Review Table */
.review-table-container {{
    overflow-x: auto;
    width: 100%;
    margin-top: 8px;
}}

.review-table {{
    min-width: 540px;
    width: 100%;
}}

.review-row {{
    display: grid;
    grid-template-columns: 1.2fr 2fr 1.6fr 1.2fr;
    gap: 10px;
    padding: 10px 12px;
    border-bottom: 1px solid {COLOR_BORDER};
    font-size: 0.82rem;
    align-items: center;
}}

.review-header {{
    font-weight: 700;
    color: {COLOR_TEXT_SECONDARY};
    background: rgba(255, 255, 255, 0.03);
    border-radius: 6px 6px 0 0;
}}

.badge-matched {{
    background: rgba(16, 185, 129, 0.12);
    color: #34D399;
    border: 1px solid rgba(16, 185, 129, 0.3);
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.72rem;
    font-weight: 700;
    display: inline-block;
    white-space: nowrap;
}}

.badge-review {{
    background: rgba(245, 158, 11, 0.12);
    color: #FBBF24;
    border: 1px solid rgba(245, 158, 11, 0.3);
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.72rem;
    font-weight: 700;
    display: inline-block;
    white-space: nowrap;
}}

.badge-pending {{
    background: rgba(148, 163, 184, 0.12);
    color: #CBD5E1;
    border: 1px solid rgba(148, 163, 184, 0.3);
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.72rem;
    font-weight: 700;
    display: inline-block;
    white-space: nowrap;
}}
</style>
"""

def render_html(html_str: str) -> None:
    """Safely renders raw HTML/SVG markup in Streamlit without CommonMark markdown interference.

    Strips all leading whitespace from each line so the CommonMark parser never encounters
    4+ spaces of leading indentation (which would otherwise trigger <pre><code> code blocks).
    Also eliminates blank lines that would prematurely close HTML block mode.
    """
    cleaned = textwrap.dedent(html_str).strip()
    lines = [line.strip() for line in cleaned.splitlines() if line.strip()]
    st.markdown("\n".join(lines), unsafe_allow_html=True)

def apply_theme():
    """Inject the centralized design CSS into the current page."""
    if hasattr(st, "html"):
        st.html(CUSTOM_CSS)
    else:
        render_html(CUSTOM_CSS)
