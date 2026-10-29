import streamlit as st
from src.styles.theme import render_html

NAVBAR_HTML = """
<div class="navbar-wrapper">
    <div class="navbar-container">
        <!-- Left: Branding with Custom SVG Biometric Aperture Logo -->
        <a href="#home" class="nav-brand">
            <svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: block;">
                <rect width="30" height="30" rx="8" fill="#111A30" stroke="rgba(139, 92, 246, 0.4)" stroke-width="1.2"/>
                <circle cx="15" cy="15" r="6" stroke="#22D3EE" stroke-width="1.8"/>
                <circle cx="15" cy="15" r="2.2" fill="#8B5CF6"/>
                <path d="M15 4.5V7M15 23v2.5M4.5 15H7m16 0h2.5" stroke="#F8FAFC" stroke-width="1.5" stroke-linecap="round"/>
                <path d="M7.5 7.5L9.5 9.5M20.5 20.5l2 2M22.5 7.5L20.5 9.5M9.5 20.5l-2 2" stroke="rgba(34, 211, 238, 0.5)" stroke-width="1.2" stroke-linecap="round"/>
            </svg>
            <span class="brand-text">Attend<span class="brand-accent">AI</span></span>
        </a>

        <!-- Middle: Direct In-Page Anchor Navigation -->
        <div class="nav-links">
            <a href="#home" class="nav-link">Home</a>
            <a href="#how-it-works" class="nav-link">How It Works</a>
            <a href="#face-recognition" class="nav-link">Face Recognition</a>
            <a href="#voice-recognition" class="nav-link">Voice Recognition</a>
            <a href="#teacher-review" class="nav-link">Teacher Review</a>
        </div>

        <!-- Right: Elegant Status Badge -->
        <div>
            <span class="nav-status-badge">
                <span class="status-dot"></span>
                AI-POWERED ATTENDANCE
            </span>
        </div>
    </div>
</div>
"""

def render_navbar():
    """Renders the static, premium AttendAI navbar."""
    render_html(NAVBAR_HTML)
