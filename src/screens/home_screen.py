import streamlit as st
from src.styles.theme import apply_theme, render_html
from src.components.navbar import render_navbar

def home_screen():
    # Apply centralized deep navy theme
    apply_theme()

    # Anchor target for Home
    render_html('<div id="home"></div>')

    # 1. Premium Top Navbar
    render_navbar()

    # =========================================================================
    # 2. HERO SECTION
    # =========================================================================
    col_hero_left, col_hero_right = st.columns([6, 6], vertical_alignment="center")

    with col_hero_left:
        render_html(
            """
            <div class="hero-content">
                <span class="hero-label">INTELLIGENT ATTENDANCE SYSTEM</span>
                <h1 class="hero-title">
                    Attendance, <span class="hero-highlight">Made Intelligent.</span>
                </h1>
                <p class="hero-desc">
                    Simplify classroom attendance with AI-powered face and voice recognition,
                    designed to make the process faster, smarter, and easier to review.
                </p>
                <div style="margin-bottom: 1rem;">
                    <span class="feature-tag-pill"><span class="feature-dot-violet"></span> Face Recognition</span>
                    <span class="feature-tag-pill"><span class="feature-dot-cyan"></span> Voice Recognition</span>
                </div>
                <div class="hero-indicator">
                    Two recognition methods. One smarter workflow.
                </div>
            </div>
            """
        )

    with col_hero_right:
        # Cohesive Static AI Visual Illustration (Custom SVG & Layered Panels)
        render_html(
            """
            <div style="background: linear-gradient(145deg, #111A30 0%, #16203D 100%); border: 1px solid rgba(139, 92, 246, 0.35); border-radius: 14px; padding: 18px 20px; box-shadow: 0 16px 36px rgba(0, 0, 0, 0.4); color: #F8FAFC;">
                <!-- Header of Product Visual -->
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1E2A4A; padding-bottom: 10px; margin-bottom: 12px; gap: 8px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <svg width="14" height="14" viewBox="0 0 16 16" fill="none" style="display: block; flex-shrink: 0;">
                            <rect width="16" height="16" rx="4" fill="#8B5CF6"/>
                            <circle cx="8" cy="8" r="3" fill="#22D3EE"/>
                        </svg>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #CBD5E1; font-weight: 700; letter-spacing: 0.05em; white-space: nowrap;">CLASSROOM CAPTURE &bull; HUD</span>
                    </div>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: #22D3EE; background: rgba(34, 211, 238, 0.1); border: 1px solid rgba(34, 211, 238, 0.3); padding: 2px 7px; border-radius: 4px; white-space: nowrap;">AI INFERENCE PIPELINE</span>
                </div>

                <!-- Classroom Silhouettes with Face Bounding Boxes -->
                <div style="background: #0B1020; border: 1px solid #1E2A4A; border-radius: 8px; padding: 12px; margin-bottom: 10px; position: relative;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.68rem; color: #A7B0C0; margin-bottom: 6px;">
                        <span style="text-transform: uppercase; font-weight: 700; color: #8B5CF6;">Visual Detection Roster</span>
                        <span>38 Students Detected</span>
                    </div>

                    <svg width="100%" height="86" viewBox="0 0 320 86" fill="none" style="display: block; width: 100%;">
                        <!-- Student Silhouettes -->
                        <path d="M15 82 C15 58, 42 58, 42 82 Z" fill="#1E2A4A"/>
                        <circle cx="28.5" cy="45" r="11" fill="#2D3B60"/>

                        <path d="M80 82 C80 56, 110 56, 110 82 Z" fill="#1E2A4A"/>
                        <circle cx="95" cy="43" r="12" fill="#2D3B60"/>

                        <path d="M148 82 C148 58, 175 58, 175 82 Z" fill="#1E2A4A"/>
                        <circle cx="161.5" cy="45" r="11" fill="#2D3B60"/>

                        <path d="M212 82 C212 54, 244 54, 244 82 Z" fill="#1E2A4A"/>
                        <circle cx="228" cy="41" r="12" fill="#2D3B60"/>

                        <path d="M278 82 C278 58, 305 58, 305 82 Z" fill="#1E2A4A"/>
                        <circle cx="291.5" cy="45" r="11" fill="#2D3B60"/>

                        <!-- Target Bounding Box 1 -->
                        <rect x="80" y="27" width="30" height="32" rx="4" stroke="#22D3EE" stroke-width="1.8"/>
                        <path d="M78 33 V25 H86M112 33 V25 H104" stroke="#22D3EE" stroke-width="1.5" stroke-linecap="round"/>
                        <text x="76" y="20" fill="#22D3EE" font-size="7.5" font-family="'JetBrains Mono', monospace" font-weight="bold">ID: CS-104 &#8226; 99.2%</text>

                        <!-- Target Bounding Box 2 -->
                        <rect x="213" y="25" width="30" height="32" rx="4" stroke="#8B5CF6" stroke-width="1.8"/>
                        <path d="M211 31 V23 H219M245 31 V23 H237" stroke="#8B5CF6" stroke-width="1.5" stroke-linecap="round"/>
                        <text x="209" y="18" fill="#8B5CF6" font-size="7.5" font-family="'JetBrains Mono', monospace" font-weight="bold">ID: CS-119 &#8226; 98.7%</text>
                    </svg>
                </div>

                <!-- Layered Sub-Panels: Miniature Attendance Preview + Static Voice Waveform -->
                <div style="display: grid; grid-template-columns: 1.3fr 1fr; gap: 8px;">
                    <!-- Attendance Preview -->
                    <div style="background: #0B1020; border: 1px solid #1E2A4A; border-radius: 6px; padding: 8px 10px; font-family: 'JetBrains Mono', monospace; font-size: 0.68rem;">
                        <div style="color: #A7B0C0; font-size: 0.64rem; text-transform: uppercase; margin-bottom: 4px;">Proposed Status</div>
                        <div style="color: #F8FAFC;">Arjun S. &mdash; <span style="color: #34D399; font-weight: 700;">Confirmed</span></div>
                        <div style="color: #F8FAFC;">Priya K. &mdash; <span style="color: #34D399; font-weight: 700;">Confirmed</span></div>
                    </div>

                    <!-- Voice Waveform Element -->
                    <div style="background: #0B1020; border: 1px solid #1E2A4A; border-radius: 6px; padding: 8px 10px;">
                        <div style="font-size: 0.64rem; color: #22D3EE; font-family: 'JetBrains Mono', monospace; font-weight: 700; text-transform: uppercase; margin-bottom: 4px;">Acoustic Spectrum</div>
                        <svg width="100%" height="18" viewBox="0 0 100 18" fill="none" style="display: block; width: 100%;">
                            <rect x="4" y="6" width="3" height="6" rx="1.5" fill="#8B5CF6"/>
                            <rect x="12" y="3" width="3" height="12" rx="1.5" fill="#22D3EE"/>
                            <rect x="20" y="1" width="3" height="16" rx="1.5" fill="#8B5CF6"/>
                            <rect x="28" y="5" width="3" height="8" rx="1.5" fill="#22D3EE"/>
                            <rect x="36" y="2" width="3" height="14" rx="1.5" fill="#8B5CF6"/>
                            <rect x="44" y="6" width="3" height="6" rx="1.5" fill="#22D3EE"/>
                            <rect x="52" y="1" width="3" height="16" rx="1.5" fill="#8B5CF6"/>
                            <rect x="60" y="4" width="3" height="10" rx="1.5" fill="#22D3EE"/>
                            <rect x="68" y="7" width="3" height="4" rx="1.5" fill="#8B5CF6"/>
                            <rect x="76" y="3" width="3" height="12" rx="1.5" fill="#22D3EE"/>
                            <rect x="84" y="5" width="3" height="8" rx="1.5" fill="#8B5CF6"/>
                            <rect x="92" y="7" width="3" height="4" rx="1.5" fill="#22D3EE"/>
                        </svg>
                    </div>
                </div>

                <div style="font-size: 0.65rem; color: #A7B0C0; text-align: right; margin-top: 8px;">
                    &lowast; Illustrative demonstration data only. Real student biometrics are protected.
                </div>
            </div>
            """
        )

    st.write("")
    st.divider()

    # =========================================================================
    # 3. SECTION A — HOW IT WORKS
    # =========================================================================
    render_html(
        """
        <div id="how-it-works"></div>
        <div class="section-tag">SYSTEM WORKFLOW</div>
        <div class="section-title">How It Works</div>
        <div class="section-desc">A structured five-step process designed to simplify attendance capture while ensuring complete instructor oversight.</div>
        <div class="workflow-grid">
            <div class="workflow-step-card">
                <span class="workflow-num">01</span>
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="display:block; margin-bottom:8px;">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                    <circle cx="12" cy="7" r="4"/>
                </svg>
                <div class="workflow-step-title">Register Identity</div>
                <div class="workflow-step-text">Students register their institutional profiles and reference biometrics with consent.</div>
            </div>

            <div class="workflow-step-card">
                <span class="workflow-num">02</span>
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="display:block; margin-bottom:8px;">
                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                    <line x1="16" y1="2" x2="16" y2="6"/>
                    <line x1="8" y1="2" x2="8" y2="6"/>
                    <line x1="3" y1="10" x2="21" y2="10"/>
                </svg>
                <div class="workflow-step-title">Start Session</div>
                <div class="workflow-step-text">Teacher selects course subject and initiates either photo capture or voice verification.</div>
            </div>

            <div class="workflow-step-card">
                <span class="workflow-num">03</span>
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="display:block; margin-bottom:8px;">
                    <circle cx="12" cy="12" r="3"/>
                    <path d="M12 2v3m0 14v3M2 12h3m14 0h3"/>
                    <path d="M4.93 4.93l2.12 2.12m9.9 9.9l2.12 2.12M4.93 19.07l2.12-2.12m9.9-9.9l2.12-2.12"/>
                </svg>
                <div class="workflow-step-title">Recognize Biometrics</div>
                <div class="workflow-step-text">Pretrained models match faces or voices against enrolled student reference profiles.</div>
            </div>

            <div class="workflow-step-card">
                <span class="workflow-num">04</span>
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="display:block; margin-bottom:8px;">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                    <polyline points="14 2 14 8 20 8"/>
                    <line x1="16" y1="13" x2="8" y2="13"/>
                    <line x1="16" y1="17" x2="8" y2="17"/>
                </svg>
                <div class="workflow-step-title">Review Proposed</div>
                <div class="workflow-step-text">Teacher reviews AI proposals; ambiguous or occluded matches are flagged for check.</div>
            </div>

            <div class="workflow-step-card">
                <span class="workflow-num">05</span>
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="display:block; margin-bottom:8px;">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                    <path d="m9 12 2 2 4-4"/>
                </svg>
                <div class="workflow-step-title">Teacher Finalizes</div>
                <div class="workflow-step-text">Teacher confirms official attendance records, committing the register to institutional logs.</div>
            </div>
        </div>
        """
    )

    st.write("")
    st.divider()

    # =========================================================================
    # 4. SECTION B — FACE RECOGNITION
    # =========================================================================
    render_html(
        """
        <div id="face-recognition"></div>
        <div class="section-tag">METHOD 01 &bull; COMPUTER VISION</div>
        <div class="section-title">Face Recognition</div>
        <div class="section-desc">Classroom visual scanning enables fast, non-intrusive group verification from lecture hall photographs.</div>
        """
    )

    col_face_text, col_face_visual = st.columns([6, 6], vertical_alignment="center")

    with col_face_text:
        render_html(
            """
            <div style="background: #111A30; border: 1px solid rgba(139, 92, 246, 0.25); border-radius: 8px; padding: 18px 20px;">
                <div style="font-weight: 700; color: #F8FAFC; font-size: 0.98rem; margin-bottom: 8px;">How Face Recognition Works</div>
                <p style="color: #A7B0C0; font-size: 0.88rem; line-height: 1.55; margin-bottom: 12px;">
                    The instructor uploads or captures high-resolution lecture hall photographs. Pretrained deep neural networks
                    detect facial landmarks across the entire room simultaneously, mapping vector embeddings against enrolled subject rosters.
                </p>
                <div style="border-left: 3px solid #22D3EE; padding-left: 12px; margin-top: 10px;">
                    <div style="color: #22D3EE; font-size: 0.78rem; font-weight: 700; text-transform: uppercase; margin-bottom: 4px;">Ethical Verification Standard</div>
                    <div style="color: #A7B0C0; font-size: 0.82rem; line-height: 1.45;">
                        An unrecognized face alone does not prove that a student is absent. The teacher explicitly reviews ambiguous or obstructed detections before finalizing.
                    </div>
                </div>
            </div>
            """
        )

    with col_face_visual:
        render_html(
            """
            <div style="background: #111A30; border: 1px solid #1E2A4A; border-radius: 10px; padding: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1E2A4A; padding-bottom: 8px; margin-bottom: 10px;">
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #CBD5E1; font-weight: 700;">VISUAL MATCH ENGINE</span>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: #34D399; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); padding: 2px 6px; border-radius: 4px;">41 MATCHED &bull; 1 REVIEW</span>
                </div>

                <!-- Detection Mock Grid -->
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 10px;">
                    <div style="background: #0B1020; border: 1px solid #1E2A4A; border-radius: 6px; padding: 8px 10px;">
                        <div style="font-size: 0.78rem; font-weight: 700; color: #F8FAFC;">Arjun Sharma</div>
                        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #22D3EE;">Match: 98.7% &bull; Proposed Present</div>
                    </div>
                    <div style="background: #0B1020; border: 1px solid #1E2A4A; border-radius: 6px; padding: 8px 10px;">
                        <div style="font-size: 0.78rem; font-weight: 700; color: #F8FAFC;">Priya Kulkarni</div>
                        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #22D3EE;">Match: 96.4% &bull; Proposed Present</div>
                    </div>
                    <div style="background: #0B1020; border: 1px solid rgba(245, 158, 11, 0.35); border-radius: 6px; padding: 8px 10px;">
                        <div style="font-size: 0.78rem; font-weight: 700; color: #FBBF24;">Tanvi Joshi</div>
                        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #FBBF24;">Match: 74.2% &bull; Review Flagged</div>
                    </div>
                    <div style="background: #0B1020; border: 1px solid #1E2A4A; border-radius: 6px; padding: 8px 10px;">
                        <div style="font-size: 0.78rem; font-weight: 700; color: #F8FAFC;">Devendra Patil</div>
                        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #22D3EE;">Match: 99.1% &bull; Proposed Present</div>
                    </div>
                </div>

                <div style="font-size: 0.72rem; color: #A7B0C0; background: #0B1020; padding: 6px 10px; border-radius: 4px;">
                    Result: 42 faces detected &bull; System prepared proposed attendance roster
                </div>
            </div>
            """
        )

    st.write("")
    st.divider()

    # =========================================================================
    # 5. SECTION C — VOICE RECOGNITION
    # =========================================================================
    render_html(
        """
        <div id="voice-recognition"></div>
        <div class="section-tag">METHOD 02 &bull; ACOUSTIC BIOMETRICS</div>
        <div class="section-title">Voice Recognition</div>
        <div class="section-desc">Acoustic speaker verification for individual roll validation and low-light classroom environments.</div>
        """
    )

    col_voice_visual, col_voice_text = st.columns([6, 6], vertical_alignment="center")

    with col_voice_visual:
        render_html(
            """
            <div style="background: #111A30; border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 10px; padding: 18px; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
                <!-- Microphone Icon and Status -->
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1E2A4A; padding-bottom: 8px; margin-bottom: 12px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block; flex-shrink: 0;">
                            <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
                            <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
                            <line x1="12" y1="19" x2="12" y2="23"/>
                            <line x1="8" y1="23" x2="16" y2="23"/>
                        </svg>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #CBD5E1; font-weight: 700;">ACTIVE ACOUSTIC SESSION</span>
                    </div>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: #34D399; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); padding: 2px 6px; border-radius: 4px;">SPEAKER VERIFIED</span>
                </div>

                <!-- Static Audio Waveform Graph -->
                <div style="background: #0B1020; border: 1px solid #1E2A4A; border-radius: 8px; padding: 14px; text-align: center; margin-bottom: 10px;">
                    <div style="font-size: 0.74rem; color: #A7B0C0; margin-bottom: 8px;">
                        Passphrase: <span style="color: #F8FAFC; font-weight: 600;">"Present for CS501 Machine Learning"</span>
                    </div>

                    <svg width="100%" height="28" viewBox="0 0 240 28" fill="none" style="display:block; width: 100%; margin: 0 auto;">
                        <rect x="10" y="10" width="4" height="8" rx="2" fill="#8B5CF6"/>
                        <rect x="22" y="6" width="4" height="16" rx="2" fill="#22D3EE"/>
                        <rect x="34" y="2" width="4" height="24" rx="2" fill="#8B5CF6"/>
                        <rect x="46" y="8" width="4" height="12" rx="2" fill="#22D3EE"/>
                        <rect x="58" y="4" width="4" height="20" rx="2" fill="#8B5CF6"/>
                        <rect x="70" y="10" width="4" height="8" rx="2" fill="#22D3EE"/>
                        <rect x="82" y="1" width="4" height="26" rx="2" fill="#8B5CF6"/>
                        <rect x="94" y="5" width="4" height="18" rx="2" fill="#22D3EE"/>
                        <rect x="106" y="9" width="4" height="10" rx="2" fill="#8B5CF6"/>
                        <rect x="118" y="3" width="4" height="22" rx="2" fill="#22D3EE"/>
                        <rect x="130" y="7" width="4" height="14" rx="2" fill="#8B5CF6"/>
                        <rect x="142" y="2" width="4" height="24" rx="2" fill="#22D3EE"/>
                        <rect x="154" y="8" width="4" height="12" rx="2" fill="#8B5CF6"/>
                        <rect x="166" y="4" width="4" height="20" rx="2" fill="#22D3EE"/>
                        <rect x="178" y="10" width="4" height="8" rx="2" fill="#8B5CF6"/>
                        <rect x="190" y="3" width="4" height="22" rx="2" fill="#22D3EE"/>
                        <rect x="202" y="7" width="4" height="14" rx="2" fill="#8B5CF6"/>
                        <rect x="214" y="9" width="4" height="10" rx="2" fill="#22D3EE"/>
                        <rect x="226" y="11" width="4" height="6" rx="2" fill="#8B5CF6"/>
                    </svg>
                </div>

                <div style="display: flex; justify-content: space-between; font-size: 0.72rem; background: #0B1020; padding: 7px 10px; border-radius: 4px;">
                    <span style="color: #A7B0C0;">Acoustic Matching:</span>
                    <span style="color: #34D399; font-weight: 700;">ID CS-118 &bull; 98.9% Match &bull; Proposed Present</span>
                </div>
            </div>
            """
        )

    with col_voice_text:
        render_html(
            """
            <div style="background: #111A30; border: 1px solid rgba(34, 211, 238, 0.25); border-radius: 8px; padding: 18px 20px;">
                <div style="font-weight: 700; color: #F8FAFC; font-size: 0.98rem; margin-bottom: 8px;">How Voice Recognition Works</div>
                <p style="color: #A7B0C0; font-size: 0.88rem; line-height: 1.55; margin-bottom: 12px;">
                    During a teacher-initiated voice session, students speak an agreed academic phrase individually. The system processes
                    acoustic frequency features, comparing embeddings against registered student voiceprints.
                </p>
                <div style="border-left: 3px solid #8B5CF6; padding-left: 12px; margin-top: 10px;">
                    <div style="color: #8B5CF6; font-size: 0.78rem; font-weight: 700; text-transform: uppercase; margin-bottom: 4px;">Supplemental Modality</div>
                    <div style="color: #A7B0C0; font-size: 0.82rem; line-height: 1.45;">
                        Enables seamless verification during seminars, viva examinations, and lab environments where visual cameras may experience lighting or physical constraints.
                    </div>
                </div>
            </div>
            """
        )

    st.write("")
    st.divider()

    # =========================================================================
    # 6. SECTION D — TEACHER REVIEW
    # =========================================================================
    render_html(
        """
        <div id="teacher-review"></div>
        <div class="section-tag">AUDIT & FINALIZATION</div>
        <div class="section-title">Teacher Review</div>
        <div class="section-desc">AI produces proposed attendance; the instructor retains ultimate authority over every confirmed record.</div>

        <div style="background: #111A30; border: 1px solid #1E2A4A; border-radius: 10px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
            <!-- Review Console Header -->
            <div style="display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1px solid #1E2A4A; padding-bottom: 10px; margin-bottom: 14px; flex-wrap: wrap; gap: 8px;">
                <div>
                    <span style="font-size: 1.05rem; font-weight: 700; color: #F8FAFC;">Attendance Register Review</span>
                    <span style="font-size: 0.82rem; color: #A7B0C0; margin-left: 10px;">CS501 &bull; Session 14 &bull; Hall B-204</span>
                </div>
                <div style="display: flex; gap: 8px;">
                    <span class="badge-matched">60 Matched</span>
                    <span class="badge-review">2 Needs Review</span>
                    <span class="badge-pending">2 Pending</span>
                </div>
            </div>

            <!-- Responsive Table Container -->
            <div class="review-table-container">
                <div class="review-table">
                    <!-- Static Table Header -->
                    <div class="review-row review-header">
                        <div>ROLL NUMBER</div>
                        <div>STUDENT NAME</div>
                        <div>VERIFICATION MODE</div>
                        <div>PROPOSED STATUS</div>
                    </div>

                    <!-- Static Table Rows -->
                    <div class="review-row">
                        <div style="font-family: 'JetBrains Mono', monospace; color: #CBD5E1;">2026-081</div>
                        <div style="color: #F8FAFC; font-weight: 600;">Arjun Sharma</div>
                        <div style="color: #A7B0C0;">Face Recognition (98.7%)</div>
                        <div><span class="badge-matched">Matched</span></div>
                    </div>

                    <div class="review-row">
                        <div style="font-family: 'JetBrains Mono', monospace; color: #CBD5E1;">2026-094</div>
                        <div style="color: #F8FAFC; font-weight: 600;">Priya Kulkarni</div>
                        <div style="color: #A7B0C0;">Face Recognition (96.4%)</div>
                        <div><span class="badge-matched">Matched</span></div>
                    </div>

                    <div class="review-row">
                        <div style="font-family: 'JetBrains Mono', monospace; color: #CBD5E1;">2026-102</div>
                        <div style="color: #F8FAFC; font-weight: 600;">Tanvi Joshi</div>
                        <div style="color: #A7B0C0;">Face Occlusion (74.2%)</div>
                        <div><span class="badge-review">Needs Review</span></div>
                    </div>

                    <div class="review-row">
                        <div style="font-family: 'JetBrains Mono', monospace; color: #CBD5E1;">2026-118</div>
                        <div style="color: #F8FAFC; font-weight: 600;">Devendra Patil</div>
                        <div style="color: #A7B0C0;">Voice Verification (98.9%)</div>
                        <div><span class="badge-matched">Matched</span></div>
                    </div>

                    <div class="review-row" style="border-bottom: none;">
                        <div style="font-family: 'JetBrains Mono', monospace; color: #CBD5E1;">2026-135</div>
                        <div style="color: #F8FAFC; font-weight: 600;">Sneha Deshmukh</div>
                        <div style="color: #A7B0C0;">Standby Check</div>
                        <div><span class="badge-pending">Pending</span></div>
                    </div>
                </div>
            </div>

            <!-- Action Bar Footer -->
            <div style="margin-top: 16px; padding-top: 14px; border-top: 1px solid #1E2A4A; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="font-size: 0.78rem; color: #A7B0C0;">
                    Clarification: Unrecognized face alone does not prove student absence. Teacher confirms final presence.
                </div>
                <div style="background: rgba(139, 92, 246, 0.15); border: 1px solid rgba(139, 92, 246, 0.4); border-radius: 6px; padding: 6px 14px; font-size: 0.82rem; font-weight: 700; color: #F8FAFC;">
                    Finalize Attendance Register &bull; Teacher Authorization Required
                </div>
            </div>
        </div>
        """
    )

    st.write("")

if __name__ == "__main__":
    home_screen()
