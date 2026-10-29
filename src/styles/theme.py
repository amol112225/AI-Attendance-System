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
COLOR_DANGER = "#EF4444"       # Status red

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

/* Sidebar Styling */
section[data-testid="stSidebar"] {{
    background-color: #0E1528 !important;
    border-right: 1px solid {COLOR_BORDER} !important;
}}

section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] {{
    padding-top: 0.75rem !important;
    padding-bottom: 0.5rem !important;
}}

section[data-testid="stSidebar"] div[role="radiogroup"] {{
    gap: 6px !important;
}}


section[data-testid="stSidebar"] div[role="radiogroup"] label {{
    background-color: {COLOR_NAVY_SURFACE} !important;
    border: 1px solid {COLOR_BORDER} !important;
    border-radius: 8px !important;
    padding: 10px 14px !important;
    margin-bottom: 6px !important;
    color: {COLOR_TEXT_SECONDARY} !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    width: 100% !important;
    box-sizing: border-box !important;
}}


section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
    border-color: rgba(139, 92, 246, 0.45) !important;
    color: {COLOR_TEXT_PRIMARY} !important;
}}

section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"],
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {{
    background-color: rgba(139, 92, 246, 0.18) !important;
    border-color: {COLOR_VIOLET} !important;
    color: {COLOR_CYAN} !important;
}}

section[data-testid="stSidebar"] div[role="radiogroup"] label input[type="radio"],
section[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {{
    display: none !important;
}}

/* Segmented Control Styling */
div[data-testid="stSegmentedControl"] {{
    background: {COLOR_NAVY_SURFACE} !important;
    border: 1px solid {COLOR_BORDER} !important;
    border-radius: 8px !important;
    padding: 3px !important;
    margin-bottom: 1.25rem !important;
}}

/* Dialog / Modal Styling */
div[role="dialog"] {{
    background-color: {COLOR_NAVY_SURFACE} !important;
    border: 1px solid rgba(139, 92, 246, 0.4) !important;
    border-radius: 12px !important;
    color: {COLOR_TEXT_PRIMARY} !important;
}}

div[role="dialog"] h2 {{
    color: {COLOR_TEXT_PRIMARY} !important;
    font-size: 1.25rem !important;
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

/* Student Header Banner */
.student-header-box {{
    background: linear-gradient(135deg, #111A30 0%, #16203D 100%);
    border: 1px solid rgba(139, 92, 246, 0.28);
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 1.25rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
}}

.student-profile-summary {{
    display: flex;
    align-items: center;
    gap: 14px;
}}

.student-avatar {{
    width: 48px;
    height: 48px;
    border-radius: 10px;
    background: #0B1020;
    border: 1.5px solid {COLOR_CYAN};
    color: {COLOR_CYAN};
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    font-weight: 800;
    font-family: 'JetBrains Mono', monospace;
    flex-shrink: 0;
}}

.student-title-block h2 {{
    margin: 0 !important;
    font-size: 1.35rem !important;
    font-weight: 800 !important;
    color: {COLOR_TEXT_PRIMARY} !important;
}}

.student-subtitle {{
    font-size: 0.85rem;
    color: {COLOR_TEXT_SECONDARY};
    margin-top: 3px;
}}

/* Teacher Header Banner */
.teacher-header-box {{
    background: linear-gradient(135deg, #111A30 0%, #16203D 100%);
    border: 1px solid rgba(139, 92, 246, 0.28);
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 1.25rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
}}

.teacher-avatar {{
    width: 48px;
    height: 48px;
    border-radius: 10px;
    background: #0B1020;
    border: 1.5px solid {COLOR_VIOLET};
    color: {COLOR_VIOLET};
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    font-weight: 800;
    font-family: 'JetBrains Mono', monospace;
    flex-shrink: 0;
}}

/* Workflow Explanation Box */
.workflow-explanation-box {{
    background: #0B1020;
    border: 1px solid {COLOR_BORDER};
    border-left: 3px solid {COLOR_CYAN};
    border-radius: 8px;
    padding: 14px 18px;
    margin-top: 14px;
    margin-bottom: 14px;
}}

/* Roster Table */
.roster-table-container {{
    overflow-x: auto;
    width: 100%;
    background: {COLOR_NAVY_SURFACE};
    border: 1px solid {COLOR_BORDER};
    border-radius: 8px;
}}

.roster-table {{
    min-width: 680px;
    width: 100%;
}}

.roster-row {{
    display: grid;
    grid-template-columns: 1.8fr 1.3fr 2.1fr 1.3fr 1.4fr;
    gap: 12px;
    padding: 11px 16px;
    border-bottom: 1px solid {COLOR_BORDER};
    font-size: 0.83rem;
    align-items: center;
}}

.roster-header {{
    font-weight: 700;
    color: {COLOR_TEXT_SECONDARY};
    background: rgba(255, 255, 255, 0.02);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}}

.badge-excellent {{
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.35);
    color: #34D399;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.72rem;
    font-weight: 700;
    display: inline-block;
    white-space: nowrap;
}}

.badge-risk {{
    background: rgba(239, 68, 68, 0.12);
    border: 1px solid rgba(239, 68, 68, 0.35);
    color: #F87171;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.72rem;
    font-weight: 700;
    display: inline-block;
    white-space: nowrap;
}}

.badge-demo {{
    background: rgba(245, 158, 11, 0.12);
    border: 1px solid rgba(245, 158, 11, 0.35);
    color: #FBBF24;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 6px;
    letter-spacing: 0.05em;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
}}

.badge-academic {{
    background: rgba(34, 211, 238, 0.08);
    border: 1px solid rgba(34, 211, 238, 0.25);
    color: {COLOR_CYAN};
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 6px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
}}

/* Overview Metrics Grid */
.metrics-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin-bottom: 1.25rem;
    width: 100%;
}}

@media (max-width: 900px) {{
    .metrics-grid {{
        grid-template-columns: repeat(2, 1fr);
    }}
}}

@media (max-width: 520px) {{
    .metrics-grid {{
        grid-template-columns: 1fr;
    }}
}}

.metric-panel {{
    background-color: {COLOR_NAVY_SURFACE};
    border: 1px solid {COLOR_BORDER};
    border-radius: 10px;
    padding: 16px 18px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 115px;
}}

.metric-panel-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
}}

.metric-panel-label {{
    font-size: 0.72rem;
    font-weight: 700;
    color: {COLOR_TEXT_SECONDARY};
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-family: 'JetBrains Mono', monospace;
}}

.metric-panel-icon {{
    width: 28px;
    height: 28px;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
}}

.metric-panel-value {{
    font-size: 1.85rem;
    font-weight: 800;
    color: {COLOR_TEXT_PRIMARY};
    line-height: 1.1;
    margin-bottom: 4px;
    font-family: 'Plus Jakarta Sans', sans-serif;
}}

.metric-panel-desc {{
    font-size: 0.78rem;
    color: {COLOR_TEXT_SECONDARY};
}}

.advisory-bar {{
    background: {COLOR_NAVY_SURFACE};
    border: 1px solid rgba(34, 211, 238, 0.25);
    border-left: 3px solid {COLOR_CYAN};
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
    font-size: 0.85rem;
}}

/* My Subjects Section */
.subject-row-card {{
    background-color: {COLOR_NAVY_SURFACE};
    border: 1px solid {COLOR_BORDER};
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 12px;
    display: grid;
    grid-template-columns: 2fr 1.5fr 1.3fr 1.2fr;
    gap: 16px;
    align-items: center;
}}

@media (max-width: 900px) {{
    .subject-row-card {{
        grid-template-columns: 1fr 1fr;
    }}
}}

@media (max-width: 580px) {{
    .subject-row-card {{
        grid-template-columns: 1fr;
    }}
}}

.subject-code-tag {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 700;
    color: {COLOR_CYAN};
    background: rgba(34, 211, 238, 0.08);
    border: 1px solid rgba(34, 211, 238, 0.25);
    padding: 2px 6px;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 4px;
}}

.subject-title {{
    font-size: 1rem;
    font-weight: 700;
    color: {COLOR_TEXT_PRIMARY};
    margin-bottom: 3px;
}}

.subject-faculty {{
    font-size: 0.82rem;
    color: {COLOR_TEXT_SECONDARY};
}}

.progress-track {{
    background: #0B1020;
    border: 1px solid {COLOR_BORDER};
    border-radius: 6px;
    height: 8px;
    width: 100%;
    overflow: hidden;
    margin-top: 6px;
}}

.progress-bar-fill {{
    height: 100%;
    border-radius: 6px;
}}

/* Attendance History Table */
.history-table-container {{
    overflow-x: auto;
    width: 100%;
    background: {COLOR_NAVY_SURFACE};
    border: 1px solid {COLOR_BORDER};
    border-radius: 8px;
}}

.history-table {{
    min-width: 680px;
    width: 100%;
}}

.history-row {{
    display: grid;
    grid-template-columns: 1.1fr 1.8fr 2.1fr 1.4fr 1.1fr;
    gap: 12px;
    padding: 11px 16px;
    border-bottom: 1px solid {COLOR_BORDER};
    font-size: 0.83rem;
    align-items: center;
}}

.history-header {{
    font-weight: 700;
    color: {COLOR_TEXT_SECONDARY};
    background: rgba(255, 255, 255, 0.02);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}}

.status-present {{
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.35);
    color: #34D399;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.72rem;
    font-weight: 700;
    display: inline-block;
    white-space: nowrap;
}}

.status-absent {{
    background: rgba(239, 68, 68, 0.12);
    border: 1px solid rgba(239, 68, 68, 0.35);
    color: #F87171;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.72rem;
    font-weight: 700;
    display: inline-block;
    white-space: nowrap;
}}

.status-pending {{
    background: rgba(245, 158, 11, 0.12);
    border: 1px solid rgba(245, 158, 11, 0.35);
    color: #FBBF24;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.72rem;
    font-weight: 700;
    display: inline-block;
    white-space: nowrap;
}}

/* Profile Cards */
.profile-card {{
    background: {COLOR_NAVY_SURFACE};
    border: 1px solid {COLOR_BORDER};
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 16px;
}}

.profile-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
}}

@media (max-width: 640px) {{
    .profile-grid {{
        grid-template-columns: 1fr;
    }}
}}

.profile-field-label {{
    font-size: 0.72rem;
    color: {COLOR_TEXT_SECONDARY};
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 4px;
}}

.profile-field-val {{
    font-size: 0.94rem;
    font-weight: 600;
    color: {COLOR_TEXT_PRIMARY};
}}

.biometric-panel {{
    background: #0B1020;
    border: 1px solid {COLOR_BORDER};
    border-radius: 8px;
    padding: 14px 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
    flex-wrap: wrap;
    gap: 8px;
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
    margin-top: 1.5rem !important;
    margin-bottom: 1.75rem !important;
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
