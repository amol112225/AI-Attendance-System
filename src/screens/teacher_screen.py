import streamlit as st
from datetime import date
from src.styles.theme import apply_theme, render_html

# =============================================================================
# SAMPLE DATA (ILLUSTRATIVE TEACHER DATA)
# =============================================================================
SAMPLE_TEACHER = {
    "name": "Dr. Sneha Mehta",
    "id": "FAC-2026-042",
    "department": "Computer Science & Engineering",
    "designation": "Associate Professor",
    "email": "sneha.mehta@univ.edu",
    "office": "Faculty Block B, Room 304",
}

SAMPLE_TEACHER_SUBJECTS = [
    {
        "code": "CS501",
        "name": "Artificial Intelligence",
        "enrolled_count": 42,
        "department": "Computer Science & Engineering",
        "hall": "Lecture Hall B-204",
        "schedule": "Tue & Thu • 10:00 AM – 11:30 AM",
        "avg_attendance": 91.8,
        "total_sessions": 26,
    },
    {
        "code": "CS502",
        "name": "Database Management Systems",
        "enrolled_count": 45,
        "department": "Computer Science & Engineering",
        "hall": "Database Lab 3",
        "schedule": "Mon & Wed • 02:00 PM – 03:30 PM",
        "avg_attendance": 84.6,
        "total_sessions": 24,
    },
    {
        "code": "CS503",
        "name": "Operating Systems",
        "enrolled_count": 37,
        "department": "Computer Science & Engineering",
        "hall": "Room C-102",
        "schedule": "Wed & Fri • 11:30 AM – 01:00 PM",
        "avg_attendance": 86.2,
        "total_sessions": 23,
    },
]

DEFAULT_REVIEW_PROPOSALS = [
    {
        "student_id": "2026-081",
        "name": "Arjun Sharma",
        "mode": "Classroom Photo AI",
        "confidence": "98.7%",
        "proposed_status": "Present",
        "match_status": "Matched",
        "flag_reason": "High visual landmark correlation",
    },
    {
        "student_id": "2026-094",
        "name": "Priya Kulkarni",
        "mode": "Classroom Photo AI",
        "confidence": "96.4%",
        "proposed_status": "Present",
        "match_status": "Matched",
        "flag_reason": "Clean frontal face orientation",
    },
    {
        "student_id": "2026-102",
        "name": "Tanvi Joshi",
        "mode": "Classroom Photo AI",
        "confidence": "74.2%",
        "proposed_status": "Needs Review",
        "match_status": "Review Flagged",
        "flag_reason": "Partial face occlusion (Notebook obstruction)",
    },
    {
        "student_id": "2026-118",
        "name": "Devendra Patil",
        "mode": "Voice Biometrics",
        "confidence": "98.9%",
        "proposed_status": "Present",
        "match_status": "Matched",
        "flag_reason": "Passphrase frequency spectrum verified",
    },
    {
        "student_id": "2026-135",
        "name": "Sneha Deshmukh",
        "mode": "Classroom Photo AI",
        "confidence": "68.5%",
        "proposed_status": "Needs Review",
        "match_status": "Review Flagged",
        "flag_reason": "Peripheral seating / low contrast lighting",
    },
    {
        "student_id": "2026-144",
        "name": "Rahul Verma",
        "mode": "Unverified",
        "confidence": "0.0%",
        "proposed_status": "Needs Review",
        "match_status": "Unrecognized",
        "flag_reason": "Face not detected in frame; verify absence with class",
    },
]

SAMPLE_TEACHER_SESSIONS = [
    {
        "date": "2026-10-28",
        "subject": "CS501 — Artificial Intelligence",
        "session_topic": "Lecture 26: ResNet & Deep Convolutional Nets",
        "method": "Classroom Photo AI",
        "present_count": 41,
        "enrolled_count": 42,
        "review_count": 1,
        "status": "Finalized",
    },
    {
        "date": "2026-10-27",
        "subject": "CS502 — Database Management Systems",
        "session_topic": "Lecture 24: B-Tree Indexing & Query Tuning",
        "method": "Classroom Photo AI",
        "present_count": 42,
        "enrolled_count": 45,
        "review_count": 0,
        "status": "Finalized",
    },
    {
        "date": "2026-10-26",
        "subject": "CS503 — Operating Systems",
        "session_topic": "Lab 12: Semaphore Synchronization in C",
        "method": "Voice Biometrics",
        "present_count": 34,
        "enrolled_count": 37,
        "review_count": 0,
        "status": "Finalized",
    },
    {
        "date": "2026-10-25",
        "subject": "CS501 — Artificial Intelligence",
        "session_topic": "Lab 11: PyTorch Optimization & Backprop",
        "method": "Voice Biometrics",
        "present_count": 39,
        "enrolled_count": 42,
        "review_count": 1,
        "status": "Finalized",
    },
    {
        "date": "2026-10-24",
        "subject": "CS502 — Database Management Systems",
        "session_topic": "Lecture 23: Multi-Version Concurrency (MVCC)",
        "method": "Classroom Photo AI",
        "present_count": 43,
        "enrolled_count": 45,
        "review_count": 0,
        "status": "Finalized",
    },
    {
        "date": "2026-10-23",
        "subject": "CS503 — Operating Systems",
        "session_topic": "Lecture 22: Virtual Memory & Page Tables",
        "method": "Classroom Photo AI",
        "present_count": 33,
        "enrolled_count": 37,
        "review_count": 2,
        "status": "Finalized",
    },
    {
        "date": "2026-10-21",
        "subject": "CS501 — Artificial Intelligence",
        "session_topic": "Lecture 25: CNN Architectures (AlexNet to VGG)",
        "method": "Classroom Photo AI",
        "present_count": 40,
        "enrolled_count": 42,
        "review_count": 1,
        "status": "Finalized",
    },
    {
        "date": "2026-10-20",
        "subject": "CS502 — Database Management Systems",
        "session_topic": "Lab 11: PostgreSQL Query Plan Profiling",
        "method": "Voice Biometrics",
        "present_count": 41,
        "enrolled_count": 45,
        "review_count": 0,
        "status": "Finalized",
    },
]

SAMPLE_ROSTER = [
    {
        "id": "STU-2026-081",
        "name": "Arjun Sharma",
        "subject": "CS501 — Artificial Intelligence",
        "attended": 24,
        "total": 26,
        "percentage": 92.3,
        "status": "Good Standing",
        "status_class": "badge-matched",
    },
    {
        "id": "STU-2026-094",
        "name": "Priya Kulkarni",
        "subject": "CS501 — Artificial Intelligence",
        "attended": 25,
        "total": 26,
        "percentage": 96.2,
        "status": "Excellent",
        "status_class": "badge-matched",
    },
    {
        "id": "STU-2026-102",
        "name": "Tanvi Joshi",
        "subject": "CS501 — Artificial Intelligence",
        "attended": 18,
        "total": 26,
        "percentage": 69.2,
        "status": "At Risk (<75%)",
        "status_class": "badge-risk",
    },
    {
        "id": "STU-2026-118",
        "name": "Devendra Patil",
        "subject": "CS502 — Database Management Systems",
        "attended": 22,
        "total": 24,
        "percentage": 91.7,
        "status": "Good Standing",
        "status_class": "badge-matched",
    },
    {
        "id": "STU-2026-135",
        "name": "Sneha Deshmukh",
        "subject": "CS502 — Database Management Systems",
        "attended": 21,
        "total": 24,
        "percentage": 87.5,
        "status": "Good Standing",
        "status_class": "badge-matched",
    },
    {
        "id": "STU-2026-144",
        "name": "Rahul Verma",
        "subject": "CS502 — Database Management Systems",
        "attended": 16,
        "total": 24,
        "percentage": 66.7,
        "status": "At Risk (<75%)",
        "status_class": "badge-risk",
    },
    {
        "id": "STU-2026-151",
        "name": "Ananya Iyer",
        "subject": "CS503 — Operating Systems",
        "attended": 22,
        "total": 23,
        "percentage": 95.7,
        "status": "Excellent",
        "status_class": "badge-matched",
    },
    {
        "id": "STU-2026-163",
        "name": "Vikram Rathod",
        "subject": "CS503 — Operating Systems",
        "attended": 19,
        "total": 23,
        "percentage": 82.6,
        "status": "Good Standing",
        "status_class": "badge-matched",
    },
    {
        "id": "STU-2026-172",
        "name": "Neha Gupta",
        "subject": "CS503 — Operating Systems",
        "attended": 18,
        "total": 23,
        "percentage": 78.3,
        "status": "Good Standing",
        "status_class": "badge-matched",
    },
    {
        "id": "STU-2026-189",
        "name": "Karan Malhotra",
        "subject": "CS501 — Artificial Intelligence",
        "attended": 23,
        "total": 26,
        "percentage": 88.5,
        "status": "Good Standing",
        "status_class": "badge-matched",
    },
]

# =============================================================================
# MODAL DIALOGS
# =============================================================================
@st.dialog("Create a New Subject")
def create_subject_dialog():
    render_html(
        """
        <div style="font-size: 0.88rem; color: #A7B0C0; margin-bottom: 12px; line-height: 1.45;">
            Define curriculum parameters for a newly assigned academic subject.
        </div>
        """
    )
    subj_name = st.text_input("Subject Name *", placeholder="e.g. Distributed Cloud Computing", key="create_sub_name")
    subj_code = st.text_input("Subject Code *", placeholder="e.g. CS505", key="create_sub_code")
    dept = st.selectbox("Department", ["Computer Science & Engineering", "AI & Data Science", "Information Technology"], key="create_sub_dept")
    hall = st.text_input("Assigned Lecture Hall / Lab", placeholder="e.g. Hall A-101", key="create_sub_hall")
    st.caption("Required fields are marked with *. Database persistence will connect via Supabase in a future step.")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Save & Create Subject", type="primary", use_container_width=True, key="btn_save_subject"):
            if not subj_name.strip() or not subj_code.strip():
                st.error("Please provide both Subject Name and Subject Code.")
            else:
                st.success(f"Subject '{subj_code.strip().upper()} — {subj_name.strip()}' validated successfully!")
                st.info("Demo Mode: Real subject creation requires Supabase PostgreSQL, which will be integrated in a future step. No database records were modified.")
    with col2:
        if st.button("Close", use_container_width=True, key="btn_close_create_subject"):
            st.session_state["show_create_subject_dialog"] = False
            st.rerun()

@st.dialog("Simulated Session Preview")
def simulated_session_dialog():
    subject = st.session_state.get("sim_session_subj", "CS501 — Artificial Intelligence")
    method = st.session_state.get("sim_session_method", "Face Recognition")
    session_date = st.session_state.get("sim_session_date", str(date.today()))

    render_html(
        f"""
        <div style="background: rgba(34, 211, 238, 0.08); border: 1px solid rgba(34, 211, 238, 0.3); border-radius: 8px; padding: 12px 14px; margin-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 8px; font-weight: 700; color: #22D3EE; font-size: 0.88rem;">
                <span class="status-dot"></span>
                <span>SIMULATED ATTENDANCE PIPELINE (DEMO ONLY)</span>
            </div>
            <div style="font-size: 0.78rem; color: #CBD5E1; margin-top: 4px;">
                Camera and microphone hardware are not accessed. Simulated detection vectors generated for interface validation.
            </div>
        </div>

        <div style="background: #0B1020; border: 1px solid #1E2A4A; border-radius: 8px; padding: 14px; margin-bottom: 14px; font-size: 0.82rem;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                <span style="color: #A7B0C0;">Subject:</span>
                <span style="color: #F8FAFC; font-weight: 600;">{subject}</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                <span style="color: #A7B0C0;">Date:</span>
                <span style="color: #F8FAFC; font-family: 'JetBrains Mono', monospace;">{session_date}</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                <span style="color: #A7B0C0;">Modality:</span>
                <span style="color: #22D3EE; font-weight: 600;">{method}</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #A7B0C0;">Simulated Detection Yield:</span>
                <span style="color: #34D399; font-weight: 700;">41 Matched &bull; 1 Flagged for Review</span>
            </div>
        </div>
        """
    )

    st.write("Click below to inspect the proposed attendance roster and perform teacher sign-off.")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Proceed to Attendance Review →", type="primary", use_container_width=True, key="btn_proceed_review"):
            st.session_state["show_sim_session_dialog"] = False
            st.session_state["teacher_active_section"] = "Attendance Review"
            st.rerun()
    with col2:
        if st.button("Dismiss", use_container_width=True, key="btn_dismiss_sim"):
            st.session_state["show_sim_session_dialog"] = False
            st.rerun()

# =============================================================================
# SECTION RENDERERS
# =============================================================================
def _render_overview_section():
    """Renders the 4 summary metrics and course overview breakdown."""
    render_html(
        """
        <div class="metrics-grid">
            <div class="metric-panel">
                <div class="metric-panel-header">
                    <span class="metric-panel-label">Total Subjects</span>
                    <div class="metric-panel-icon" style="background: rgba(34, 211, 238, 0.1);">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block;">
                            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
                            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
                        </svg>
                    </div>
                </div>
                <div class="metric-panel-value">3</div>
                <div class="metric-panel-desc">Active courses assigned</div>
            </div>

            <div class="metric-panel">
                <div class="metric-panel-header">
                    <span class="metric-panel-label">Enrolled Students</span>
                    <div class="metric-panel-icon" style="background: rgba(139, 92, 246, 0.1);">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block;">
                            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                            <circle cx="9" cy="7" r="4"/>
                            <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                            <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
                        </svg>
                    </div>
                </div>
                <div class="metric-panel-value">124</div>
                <div class="metric-panel-desc">Across all 3 course rosters</div>
            </div>

            <div class="metric-panel">
                <div class="metric-panel-header">
                    <span class="metric-panel-label">Sessions Conducted</span>
                    <div class="metric-panel-icon" style="background: rgba(16, 185, 129, 0.1);">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#34D399" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block;">
                            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                            <line x1="16" y1="2" x2="16" y2="6"/>
                            <line x1="8" y1="2" x2="8" y2="6"/>
                            <line x1="3" y1="10" x2="21" y2="10"/>
                        </svg>
                    </div>
                </div>
                <div class="metric-panel-value">48</div>
                <div class="metric-panel-desc">32 Photo AI &bull; 16 Voice Sessions</div>
            </div>

            <div class="metric-panel">
                <div class="metric-panel-header">
                    <span class="metric-panel-label">Average Attendance</span>
                    <div class="metric-panel-icon" style="background: rgba(34, 211, 238, 0.1);">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block;">
                            <line x1="18" y1="20" x2="18" y2="10"/>
                            <line x1="12" y1="20" x2="12" y2="4"/>
                            <line x1="6" y1="20" x2="6" y2="14"/>
                        </svg>
                    </div>
                </div>
                <div class="metric-panel-value" style="color: #34D399;">87.4%</div>
                <div class="metric-panel-desc">+12.4% above institutional 75% cutoff</div>
            </div>
        </div>
        """
    )

    # Ethical Rule Advisory Banner
    render_html(
        """
        <div class="advisory-bar">
            <div style="display: flex; align-items: center; gap: 10px;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block; flex-shrink: 0;">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                    <path d="m9 12 2 2 4-4"/>
                </svg>
                <span style="color: #F8FAFC; font-weight: 600;">Ethical Verification Policy:</span>
                <span style="color: #A7B0C0;">AI algorithms compile proposed attendance only. Instructor review is mandatory; an unrecognized face alone does not mark a student absent.</span>
            </div>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.74rem; color: #8B5CF6;">INSTRUCTOR SIGN-OFF MANDATORY</span>
        </div>
        """
    )

    col1, col2 = st.columns([6, 6])
    with col1:
        render_html(
            """
            <div style="background: #111A30; border: 1px solid #1E2A4A; border-radius: 10px; padding: 18px 20px; height: 100%;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; border-bottom: 1px solid #1E2A4A; padding-bottom: 8px;">
                    <span style="font-size: 0.95rem; font-weight: 700; color: #F8FAFC;">Active Course Breakdown</span>
                    <span style="font-size: 0.72rem; font-family: 'JetBrains Mono', monospace; color: #CBD5E1;">3 COURSES</span>
                </div>
            """
        )

        for subj in SAMPLE_TEACHER_SUBJECTS:
            render_html(
                f"""
                <div style="margin-bottom: 14px;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.84rem; margin-bottom: 4px;">
                        <span style="color: #F8FAFC; font-weight: 600;">{subj['name']} <span style="font-family: 'JetBrains Mono', monospace; color: #A7B0C0; font-size: 0.75rem;">({subj['code']})</span></span>
                        <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #22D3EE;">{subj['avg_attendance']}%</span>
                    </div>
                    <div style="font-size: 0.74rem; color: #A7B0C0; margin-bottom: 4px;">{subj['enrolled_count']} Students Enrolled &bull; {subj['hall']}</div>
                    <div class="progress-track">
                        <div class="progress-bar-fill" style="width: {subj['avg_attendance']}%; background: #22D3EE;"></div>
                    </div>
                </div>
                """
            )

        render_html(
            """
            </div>
            """
        )

    with col2:
        render_html(
            """
            <div style="background: #111A30; border: 1px solid #1E2A4A; border-radius: 10px; padding: 18px 20px; height: 100%;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; border-bottom: 1px solid #1E2A4A; padding-bottom: 8px;">
                    <span style="font-size: 0.95rem; font-weight: 700; color: #F8FAFC;">Pending Actions &amp; Recent Sessions</span>
                    <span style="font-size: 0.72rem; font-family: 'JetBrains Mono', monospace; color: #FBBF24;">1 NEEDS REVIEW</span>
                </div>

                <div style="background: #0B1020; border: 1px solid rgba(245, 158, 11, 0.35); border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div style="font-weight: 700; color: #FBBF24; font-size: 0.85rem;">CS501 &bull; Lecture 26</div>
                        <span class="badge-review">Action Required</span>
                    </div>
                    <div style="font-size: 0.78rem; color: #CBD5E1; margin-top: 4px;">
                        41 Matched &bull; 1 Ambiguous Face Detection (Tanvi Joshi - 74.2% occlusion)
                    </div>
                </div>

                <div style="font-size: 0.82rem; color: #A7B0C0; margin-bottom: 8px; font-weight: 600;">RECENT FINALIZED SESSIONS:</div>
                <div style="font-size: 0.78rem; color: #CBD5E1; padding: 6px 0; border-bottom: 1px solid #1E2A4A;">
                    &bull; CS502 DBMS &bull; Oct 27 &bull; 42/45 Present (Finalized)
                </div>
                <div style="font-size: 0.78rem; color: #CBD5E1; padding: 6px 0; border-bottom: 1px solid #1E2A4A;">
                    &bull; CS503 OS &bull; Oct 26 &bull; 34/37 Present (Finalized)
                </div>
                <div style="font-size: 0.78rem; color: #CBD5E1; padding: 6px 0;">
                    &bull; CS501 AI &bull; Oct 25 &bull; 39/42 Present (Finalized)
                </div>
            </div>
            """
        )

def _render_subjects_section():
    """Renders assigned subject cards and the Create Subject modal trigger."""
    col_hdr_left, col_hdr_right = st.columns([8, 4], vertical_alignment="center")
    with col_hdr_left:
        render_html(
            """
            <div style="margin-bottom: 8px;">
                <div class="section-tag">FACULTY CURRICULUM</div>
                <div style="font-size: 1.35rem; font-weight: 700; color: #F8FAFC;">My Assigned Subjects</div>
                <div style="font-size: 0.85rem; color: #A7B0C0;">Manage course rosters, classroom allocations, and attendance thresholds.</div>
            </div>
            """
        )
    with col_hdr_right:
        if st.button("+ Create Subject", type="primary", use_container_width=True, key="btn_open_create_subject"):
            st.session_state["show_create_subject_dialog"] = True

    if st.session_state.get("show_create_subject_dialog", False):
        create_subject_dialog()

    # Subjects List
    for subj in SAMPLE_TEACHER_SUBJECTS:
        render_html(
            f"""
            <div class="subject-row-card">
                <div>
                    <span class="subject-code-tag">{subj['code']}</span>
                    <div class="subject-title">{subj['name']}</div>
                    <div class="subject-faculty">{subj['department']} &bull; {subj['hall']}</div>
                </div>

                <div>
                    <div style="font-size: 0.72rem; color: #A7B0C0; text-transform: uppercase; font-family: 'JetBrains Mono', monospace;">Enrollment &amp; Schedule</div>
                    <div style="font-size: 1.15rem; font-weight: 800; color: #F8FAFC; margin-top: 2px;">
                        {subj['enrolled_count']} <span style="font-size: 0.82rem; color: #A7B0C0; font-weight: 500;">students</span>
                    </div>
                    <div style="font-size: 0.75rem; color: #CBD5E1; margin-top: 2px;">{subj['schedule']}</div>
                </div>

                <div>
                    <div style="display: flex; justify-content: space-between; font-size: 0.78rem; margin-bottom: 2px;">
                        <span style="font-family: 'JetBrains Mono', monospace; color: #A7B0C0;">Avg Attendance</span>
                        <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #22D3EE;">{subj['avg_attendance']}%</span>
                    </div>
                    <div class="progress-track">
                        <div class="progress-bar-fill" style="width: {subj['avg_attendance']}%; background: #22D3EE;"></div>
                    </div>
                    <div style="font-size: 0.74rem; color: #A7B0C0; margin-top: 4px;">{subj['total_sessions']} sessions completed</div>
                </div>

                <div style="text-align: right;">
                    <span class="badge-matched">Active Course</span>
                    <div style="font-size: 0.74rem; color: #A7B0C0; margin-top: 6px;">Next: Tomorrow, 10:00 AM</div>
                </div>
            </div>
            """
        )

    render_html(
        """
        <div style="background: #111A30; border: 1px dashed #1E2A4A; border-radius: 8px; padding: 12px 16px; margin-top: 14px; font-size: 0.78rem; color: #A7B0C0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
            <span>Need to add a seminar or elective course? Click "+ Create Subject" above to define course parameters.</span>
            <span style="color: #22D3EE; font-family: 'JetBrains Mono', monospace;">SUPABASE DB SYNC PENDING</span>
        </div>
        """
    )

def _render_take_attendance_section():
    """Renders attendance session configuration and the simulated session preview trigger."""
    render_html(
        """
        <div style="margin-bottom: 12px;">
            <div class="section-tag">SESSION SETUP</div>
            <div style="font-size: 1.35rem; font-weight: 700; color: #F8FAFC;">Take Attendance</div>
            <div style="font-size: 0.85rem; color: #A7B0C0;">Select course subject, session date, and biometrics recognition modality.</div>
        </div>
        """
    )

    subject_names = [f"{s['code']} — {s['name']}" for s in SAMPLE_TEACHER_SUBJECTS]

    col_setup_l, col_setup_r = st.columns([6, 6])
    with col_setup_l:
        selected_subj = st.selectbox("1. Select Course Subject", options=subject_names, key="take_att_subj_sel")
        selected_date = st.date_input("2. Session Date", value=date.today(), key="take_att_date_sel")
        selected_method = st.radio(
            "3. Recognition Modality",
            options=["Face Recognition (Classroom Photo)", "Voice Recognition (Spoken Phrase)"],
            key="take_att_method_sel",
        )

    with col_setup_r:
        # Dynamic Explanatory Panel
        if "Face Recognition" in selected_method:
            render_html(
                """
                <div class="workflow-explanation-box">
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="3" y="3" width="18" height="18" rx="4"/>
                            <circle cx="8.5" cy="8.5" r="1.5"/>
                            <polyline points="21 15 16 10 5 21"/>
                        </svg>
                        <span style="font-weight: 700; color: #22D3EE; font-size: 0.88rem;">Face Recognition Workflow</span>
                    </div>
                    <div style="font-size: 0.82rem; color: #A7B0C0; line-height: 1.5; margin-bottom: 8px;">
                        The teacher captures or uploads classroom photos. Deep neural networks detect facial landmarks across the entire room simultaneously, mapping vector embeddings against enrolled student profiles.
                    </div>
                    <div style="font-size: 0.78rem; color: #CBD5E1; border-top: 1px solid #1E2A4A; padding-top: 6px;">
                        &bull; Ideal for: Large lecture halls &bull; Non-intrusive simultaneous capture &bull; Ambiguous faces flagged for review
                    </div>
                </div>
                """
            )
        else:
            render_html(
                """
                <div class="workflow-explanation-box" style="border-left-color: #8B5CF6;">
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
                            <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
                            <line x1="12" y1="19" x2="12" y2="23"/>
                        </svg>
                        <span style="font-weight: 700; color: #8B5CF6; font-size: 0.88rem;">Voice Recognition Workflow</span>
                    </div>
                    <div style="font-size: 0.82rem; color: #A7B0C0; line-height: 1.5; margin-bottom: 8px;">
                        Students individually speak an agreed academic passphrase (e.g. "Present for CS501"). Acoustic frequency spectrogram features are extracted and compared against registered reference voiceprints.
                    </div>
                    <div style="font-size: 0.78rem; color: #CBD5E1; border-top: 1px solid #1E2A4A; padding-top: 6px;">
                        &bull; Ideal for: Labs, seminars &amp; low-light rooms &bull; Sequential roll call &bull; Supplemental modality
                    </div>
                </div>
                """
            )

    # Session Summary & Launch Action
    render_html(
        f"""
        <div style="background: #111A30; border: 1px solid #1E2A4A; border-radius: 10px; padding: 18px 20px; margin-top: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid #1E2A4A; padding-bottom: 8px; flex-wrap: wrap; gap: 8px;">
                <span style="font-size: 0.95rem; font-weight: 700; color: #F8FAFC;">Configured Session Parameters</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #22D3EE;">READY FOR SIMULATION</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; font-size: 0.82rem; margin-bottom: 14px;">
                <div>
                    <span style="color: #A7B0C0;">Subject:</span> <b style="color: #F8FAFC;">{selected_subj.split('—')[0].strip()}</b>
                </div>
                <div>
                    <span style="color: #A7B0C0;">Date:</span> <b style="color: #F8FAFC;">{selected_date}</b>
                </div>
                <div>
                    <span style="color: #A7B0C0;">Modality:</span> <b style="color: #22D3EE;">{selected_method.split('(')[0].strip()}</b>
                </div>
            </div>
        </div>
        """
    )

    st.write("")
    if st.button("Start Demo Session", type="primary", use_container_width=True, key="btn_start_demo_session"):
        st.session_state["sim_session_subj"] = selected_subj
        st.session_state["sim_session_method"] = selected_method.split('(')[0].strip()
        st.session_state["sim_session_date"] = str(selected_date)
        st.session_state["show_sim_session_dialog"] = True

    if st.session_state.get("show_sim_session_dialog", False):
        simulated_session_dialog()

def _render_review_section():
    """Renders the core teacher review interface with local override controls and finalization."""
    render_html(
        """
        <div style="margin-bottom: 12px;">
            <div class="section-tag">AUDIT &amp; OVERRIDE</div>
            <div style="font-size: 1.35rem; font-weight: 700; color: #F8FAFC;">Attendance Review</div>
            <div style="font-size: 0.85rem; color: #A7B0C0;">Inspect AI-proposed attendance statuses, resolve flagged or occluded faces, and commit the official register.</div>
        </div>
        """
    )

    # Session Context Bar
    render_html(
        """
        <div style="background: #111A30; border: 1px solid #1E2A4A; border-radius: 8px; padding: 12px 16px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
            <div>
                <span style="font-weight: 700; color: #F8FAFC;">Session: CS501 &bull; Artificial Intelligence</span>
                <span style="font-size: 0.8rem; color: #A7B0C0; margin-left: 10px;">Today &bull; Lecture Hall B-204</span>
            </div>
            <div style="display: flex; gap: 8px;">
                <span class="badge-matched">41 Matched</span>
                <span class="badge-review">1 Needs Review</span>
                <span class="badge-pending">0 Pending</span>
            </div>
        </div>
        """
    )

    # Mandatory Ethical Rules Alert
    render_html(
        """
        <div style="background: rgba(139, 92, 246, 0.08); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 8px; padding: 12px 16px; margin-bottom: 16px; font-size: 0.82rem; color: #CBD5E1; line-height: 1.45;">
            <b style="color: #22D3EE;">Teacher Verification Principles:</b>
            <div style="margin-top: 4px;">
                &bull; AI yields <i>proposed attendance</i> only; official records require instructor sign-off.<br/>
                &bull; An unrecognized face alone does not prove student absence. Manually verify students flagged for review.<br/>
                &bull; Use the local decision selector to confirm presence, absence, or excused leave before finalization.
            </div>
        </div>
        """
    )

    # State initialization for review overrides
    if "review_overrides" not in st.session_state:
        st.session_state["review_overrides"] = {}

    render_html(
        """
        <div class="review-table-container">
            <div class="review-table" style="min-width: 720px;">
                <div class="review-row review-header" style="grid-template-columns: 1.1fr 1.6fr 1.8fr 1.4fr 1.5fr;">
                    <div>ROLL ID</div>
                    <div>STUDENT NAME</div>
                    <div>VERIFICATION &amp; REASON</div>
                    <div>PROPOSED STATUS</div>
                    <div>TEACHER DECISION</div>
                </div>
        """
    )

    for prop in DEFAULT_REVIEW_PROPOSALS:
        sid = prop["student_id"]
        current_decision = st.session_state["review_overrides"].get(sid, prop["proposed_status"])

        # Determine pill style
        if current_decision == "Present":
            badge_class = "badge-matched"
        elif current_decision == "Absent":
            badge_class = "status-absent"
        else:
            badge_class = "badge-review"

        render_html(
            f"""
            <div class="review-row" style="grid-template-columns: 1.1fr 1.6fr 1.8fr 1.4fr 1.5fr;">
                <div style="font-family: 'JetBrains Mono', monospace; color: #CBD5E1;">{prop['student_id']}</div>
                <div style="color: #F8FAFC; font-weight: 600;">{prop['name']}</div>
                <div style="color: #A7B0C0; font-size: 0.78rem;">
                    <div>{prop['mode']} ({prop['confidence']})</div>
                    <div style="font-size: 0.72rem; color: #CBD5E1;">{prop['flag_reason']}</div>
                </div>
                <div><span class="{badge_class}">{prop['proposed_status']}</span></div>
                <div style="color: #22D3EE; font-weight: 600; font-size: 0.8rem;">
                    Current: <span style="color: #F8FAFC;">{current_decision}</span>
                </div>
            </div>
            """
        )

    render_html(
        """
            </div>
        </div>
        """
    )

    # Local Teacher Override Controls
    st.write("")
    st.markdown("<p style='font-size: 0.82rem; font-weight: 700; color: #CBD5E1; text-transform: uppercase; font-family: JetBrains Mono;'>LOCAL DECISION OVERRIDES FOR FLAGGED STUDENTS:</p>", unsafe_allow_html=True)

    col_flag1, col_flag2 = st.columns(2)
    with col_flag1:
        st.markdown("**Tanvi Joshi (2026-102)** • *Flag: Partial face occlusion*")
        tanvi_choice = st.selectbox(
            "Decision for Tanvi Joshi",
            options=["Present (Verified in class)", "Absent", "Excused Leave"],
            index=0 if st.session_state["review_overrides"].get("2026-102") == "Present" else 0,
            key="tanvi_override_sel",
        )
        st.session_state["review_overrides"]["2026-102"] = "Present" if "Present" in tanvi_choice else ("Absent" if "Absent" in tanvi_choice else "Excused")

    with col_flag2:
        st.markdown("**Rahul Verma (2026-144)** • *Flag: Unrecognized face*")
        rahul_choice = st.selectbox(
            "Decision for Rahul Verma",
            options=["Absent (Confirmed not in room)", "Present (Manual check-in)", "Excused Leave"],
            index=0 if st.session_state["review_overrides"].get("2026-144") == "Absent" else 0,
            key="rahul_override_sel",
        )
        st.session_state["review_overrides"]["2026-144"] = "Present" if "Present" in rahul_choice else ("Absent" if "Absent" in rahul_choice else "Excused")

    st.write("")
    st.divider()

    # Finalize Demo Button
    if st.button("Finalize Demo Attendance", type="primary", use_container_width=True, key="btn_finalize_demo"):
        st.session_state["attendance_finalized_demo"] = True

    if st.session_state.get("attendance_finalized_demo", False):
        st.success(
            "✓ Demo Session Finalized: Attendance register signed off by Dr. Sneha Mehta. Official records updated (41 Present, 1 Absent, 0 Unresolved). "
            "Note: In demo mode, records are simulated and not committed to a persistent database."
        )

def _render_history_section():
    """Renders historical attendance sessions with working local filters and empty state."""
    render_html(
        """
        <div style="margin-bottom: 12px;">
            <div class="section-tag">SESSION ARCHIVE</div>
            <div style="font-size: 1.35rem; font-weight: 700; color: #F8FAFC;">Attendance History</div>
            <div style="font-size: 0.85rem; color: #A7B0C0;">Audit archive of historical course sessions, attendance totals, and resolution logs.</div>
        </div>
        """
    )

    subj_filter_options = ["All Subjects", "CS501 — Artificial Intelligence", "CS502 — Database Management Systems", "CS503 — Operating Systems"]
    method_filter_options = ["All Methods", "Classroom Photo AI", "Voice Biometrics"]

    def _reset_teacher_history_filters():
        st.session_state["t_hist_subj_filter"] = "All Subjects"
        st.session_state["t_hist_method_filter"] = "All Methods"

    col_hf1, col_hf2, col_hf3 = st.columns([5, 4, 3])
    with col_hf1:
        sel_subj = st.selectbox("Filter by Subject", options=subj_filter_options, key="t_hist_subj_filter")
    with col_hf2:
        sel_method = st.selectbox("Filter by Method", options=method_filter_options, key="t_hist_method_filter")
    with col_hf3:
        st.write("")
        st.write("")
        st.button("Reset Filters", use_container_width=True, key="btn_reset_t_filters", on_click=_reset_history_filters if False else _reset_teacher_history_filters)

    # Filter evaluation
    filtered_sessions = []
    for s in SAMPLE_TEACHER_SESSIONS:
        match_subj = (sel_subj == "All Subjects") or (s["subject"] == sel_subj)
        match_meth = (sel_method == "All Methods") or (s["method"] == sel_method)
        if match_subj and match_meth:
            filtered_sessions.append(s)

    render_html(
        f"""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; font-size: 0.78rem; color: #A7B0C0;">
            <span>Showing <b style="color: #F8FAFC;">{len(filtered_sessions)}</b> of {len(SAMPLE_TEACHER_SESSIONS)} past sessions</span>
            <span style="font-family: 'JetBrains Mono', monospace; color: #22D3EE;">ACTIVE FILTERS: {sel_subj.split('—')[0].strip()} &bull; {sel_method}</span>
        </div>
        """
    )

    if filtered_sessions:
        render_html(
            """
            <div class="history-table-container">
                <div class="history-table" style="min-width: 720px;">
                    <div class="history-row history-header" style="grid-template-columns: 1.1fr 1.6fr 2fr 1.3fr 1.2fr 1fr;">
                        <div>DATE</div>
                        <div>SUBJECT</div>
                        <div>SESSION / TOPIC</div>
                        <div>METHOD</div>
                        <div>ATTENDANCE</div>
                        <div>STATUS</div>
                    </div>
            """
        )

        for s in filtered_sessions:
            render_html(
                f"""
                <div class="history-row" style="grid-template-columns: 1.1fr 1.6fr 2fr 1.3fr 1.2fr 1fr;">
                    <div style="font-family: 'JetBrains Mono', monospace; color: #CBD5E1;">{s['date']}</div>
                    <div style="color: #F8FAFC; font-weight: 600;">{s['subject'].split('—')[0].strip()}</div>
                    <div style="color: #A7B0C0; font-size: 0.78rem;">{s['session_topic']}</div>
                    <div style="color: #CBD5E1; font-size: 0.76rem;">{s['method']}</div>
                    <div>
                        <b style="color: #34D399;">{s['present_count']}/{s['enrolled_count']}</b>
                        <span style="font-size: 0.72rem; color: #A7B0C0;"> ({round(s['present_count']/s['enrolled_count']*100, 1)}%)</span>
                    </div>
                    <div><span class="badge-matched">{s['status']}</span></div>
                </div>
                """
            )

        render_html(
            """
                </div>
            </div>
            """
        )
    else:
        render_html(
            f"""
            <div style="background: #111A30; border: 1px dashed #1E2A4A; border-radius: 10px; padding: 42px 20px; text-align: center; color: #A7B0C0; margin-top: 10px;">
                <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#A7B0C0" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" style="display: block; margin: 0 auto 12px auto;">
                    <circle cx="11" cy="11" r="8"/>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"/>
                </svg>
                <div style="font-size: 1.05rem; font-weight: 700; color: #F8FAFC; margin-bottom: 6px;">No Matching Historical Sessions</div>
                <div style="font-size: 0.84rem; max-width: 480px; margin: 0 auto 12px auto; line-height: 1.45;">
                    No sessions match: <b>"{sel_subj}"</b> with method <b>"{sel_method}"</b>.
                </div>
                <div style="font-size: 0.78rem; color: #64748B;">
                    Try clicking "Reset Filters" above to display all past sessions.
                </div>
            </div>
            """
        )

def _render_roster_section():
    """Renders student roster with live local search by name or ID and subject filter."""
    render_html(
        """
        <div style="margin-bottom: 12px;">
            <div class="section-tag">STUDENT DIRECTORY</div>
            <div style="font-size: 1.35rem; font-weight: 700; color: #F8FAFC;">Student Roster</div>
            <div style="font-size: 0.85rem; color: #A7B0C0;">Search student attendance standings and verification ratios across enrolled course subjects.</div>
        </div>
        """
    )

    col_s1, col_s2 = st.columns([7, 5])
    with col_s1:
        search_query = st.text_input("Search Student Name or ID", placeholder="e.g. Arjun, STU-2026-081, Priya...", key="roster_search_txt")
    with col_s2:
        subj_roster_opts = ["All Subjects", "CS501 — Artificial Intelligence", "CS502 — Database Management Systems", "CS503 — Operating Systems"]
        sel_roster_subj = st.selectbox("Subject Filter", options=subj_roster_opts, key="roster_subj_sel")

    # Local search & filter evaluation
    q = search_query.strip().lower()
    filtered_roster = []
    for st_row in SAMPLE_ROSTER:
        matches_query = (not q) or (q in st_row["name"].lower()) or (q in st_row["id"].lower())
        matches_subj = (sel_roster_subj == "All Subjects") or (st_row["subject"] == sel_roster_subj)
        if matches_query and matches_subj:
            filtered_roster.append(st_row)

    render_html(
        f"""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; font-size: 0.78rem; color: #A7B0C0;">
            <span>Showing <b style="color: #F8FAFC;">{len(filtered_roster)}</b> of {len(SAMPLE_ROSTER)} students</span>
            <span style="font-family: 'JetBrains Mono', monospace; color: #22D3EE;">QUERY: "{search_query}" &bull; {sel_roster_subj.split('—')[0].strip()}</span>
        </div>
        """
    )

    if filtered_roster:
        render_html(
            """
            <div class="roster-table-container">
                <div class="roster-table">
                    <div class="roster-row roster-header">
                        <div>STUDENT NAME</div>
                        <div>STUDENT ID</div>
                        <div>SUBJECT</div>
                        <div>ATTENDANCE RATIO</div>
                        <div>ACADEMIC STATUS</div>
                    </div>
            """
        )

        for st_row in filtered_roster:
            render_html(
                f"""
                <div class="roster-row">
                    <div style="color: #F8FAFC; font-weight: 600;">{st_row['name']}</div>
                    <div style="font-family: 'JetBrains Mono', monospace; color: #22D3EE;">{st_row['id']}</div>
                    <div style="color: #A7B0C0; font-size: 0.8rem;">{st_row['subject']}</div>
                    <div>
                        <b style="color: #F8FAFC;">{st_row['attended']}/{st_row['total']}</b>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #22D3EE;"> ({st_row['percentage']}%)</span>
                    </div>
                    <div><span class="{st_row['status_class']}">{st_row['status']}</span></div>
                </div>
                """
            )

        render_html(
            """
                </div>
            </div>
            """
        )
    else:
        render_html(
            f"""
            <div style="background: #111A30; border: 1px dashed #1E2A4A; border-radius: 10px; padding: 42px 20px; text-align: center; color: #A7B0C0; margin-top: 10px;">
                <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#A7B0C0" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" style="display: block; margin: 0 auto 12px auto;">
                    <circle cx="11" cy="11" r="8"/>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"/>
                </svg>
                <div style="font-size: 1.05rem; font-weight: 700; color: #F8FAFC; margin-bottom: 6px;">No Students Found</div>
                <div style="font-size: 0.84rem; max-width: 480px; margin: 0 auto 12px auto; line-height: 1.45;">
                    No student records match search <b>"{search_query}"</b> in <b>"{sel_roster_subj}"</b>.
                </div>
            </div>
            """
        )

# =============================================================================
# MAIN TEACHER SCREEN ENTRY POINT
# =============================================================================
def teacher_screen():
    # Apply centralized theme
    apply_theme()

    # Session State Initialization
    if "teacher_active_section" not in st.session_state:
        st.session_state["teacher_active_section"] = "Overview"

    sections = [
        "Overview",
        "My Subjects",
        "Take Attendance",
        "Attendance Review",
        "Attendance History",
        "Student Roster",
    ]

    # =========================================================================
    # SIDEBAR NAVIGATION
    # =========================================================================
    with st.sidebar:
        render_html(
            """
            <div style="padding: 10px 4px 16px 4px; border-bottom: 1px solid #1E2A4A; margin-bottom: 16px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <svg width="28" height="28" viewBox="0 0 30 30" fill="none" style="display: block;">
                        <rect width="30" height="30" rx="8" fill="#111A30" stroke="rgba(139, 92, 246, 0.4)" stroke-width="1.2"/>
                        <circle cx="15" cy="15" r="6" stroke="#22D3EE" stroke-width="1.8"/>
                        <circle cx="15" cy="15" r="2.2" fill="#8B5CF6"/>
                        <path d="M15 4.5V7M15 23v2.5M4.5 15H7m16 0h2.5" stroke="#F8FAFC" stroke-width="1.5" stroke-linecap="round"/>
                    </svg>
                    <div>
                        <div style="font-weight: 800; font-size: 1.15rem; color: #F8FAFC; letter-spacing: -0.02em;">Attend<span style="color: #22D3EE;">AI</span></div>
                        <div style="font-size: 0.68rem; font-family: 'JetBrains Mono', monospace; color: #22D3EE; font-weight: 700; letter-spacing: 0.06em;">TEACHER PORTAL</div>
                    </div>
                </div>
            </div>
            """
        )

        render_html(
            """
            <div style="font-size: 0.72rem; font-weight: 700; color: #A7B0C0; letter-spacing: 0.06em; text-transform: uppercase; font-family: 'JetBrains Mono', monospace; margin-bottom: 8px;">
                FACULTY PORTAL NAVIGATION
            </div>
            """
        )

        cur_idx = 0
        if st.session_state["teacher_active_section"] in sections:
            cur_idx = sections.index(st.session_state["teacher_active_section"])

        def on_sidebar_teacher_nav_change():
            st.session_state["teacher_active_section"] = st.session_state["teacher_sidebar_radio"]

        selected_nav = st.radio(
            "Teacher Portal Navigation",
            options=sections,
            index=cur_idx,
            key="teacher_sidebar_radio",
            on_change=on_sidebar_teacher_nav_change,
            label_visibility="collapsed",
        )
        st.session_state["teacher_active_section"] = selected_nav

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        if st.button("← Return to Home", key="btn_return_home_teacher_sidebar", use_container_width=True):
            if "pages" in st.session_state and "Home" in st.session_state["pages"]:
                st.switch_page(st.session_state["pages"]["Home"])

        render_html(
            f"""
            <div style="margin-top: 24px; padding: 12px; background: #111A30; border: 1px solid #1E2A4A; border-radius: 8px; font-size: 0.72rem; color: #A7B0C0;">
                <div style="display: flex; align-items: center; gap: 6px; color: #8B5CF6; font-weight: 700; margin-bottom: 4px;">
                    <span class="status-dot" style="background-color: #8B5CF6;"></span>
                    <span>FACULTY SESSION</span>
                </div>
                <div>Faculty: <span style="color: #F8FAFC; font-weight: 600;">{SAMPLE_TEACHER['name']}</span></div>
                <div>ID: <span style="font-family: 'JetBrains Mono', monospace; color: #CBD5E1;">{SAMPLE_TEACHER['id']}</span></div>
                <div>Dept: <span style="color: #CBD5E1;">{SAMPLE_TEACHER['department']}</span></div>
                <div style="margin-top: 8px; padding-top: 8px; border-top: 1px solid #1E2A4A; font-size: 0.68rem; color: #64748B;">
                    * Faculty portal operating in local simulation mode.
                </div>
            </div>
            """
        )

    # =========================================================================
    # MAIN CONTENT AREA
    # =========================================================================

    # 1. Top Header Banner
    render_html(
        f"""
        <div class="teacher-header-box">
            <div class="student-profile-summary">
                <div class="teacher-avatar">SM</div>
                <div class="student-title-block">
                    <h2>Teacher Dashboard</h2>
                    <div class="student-subtitle">Manage your classes and attendance sessions &bull; <b>{SAMPLE_TEACHER['name']}</b> ({SAMPLE_TEACHER['id']})</div>
                </div>
            </div>
            <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
                <span class="badge-academic">{SAMPLE_TEACHER['designation']}</span>
                <span class="badge-demo"><span class="status-dot" style="background-color: #FBBF24;"></span> DEMO DATA</span>
            </div>
        </div>
        """
    )

    # 2. Responsive Segmented Control for Mobile / Tablet view
    def on_teacher_segment_change():
        st.session_state["teacher_active_section"] = st.session_state["teacher_main_segment"]

    active_tab = st.segmented_control(
        "Teacher Section View",
        options=sections,
        default=st.session_state["teacher_active_section"],
        key="teacher_main_segment",
        on_change=on_teacher_segment_change,
        label_visibility="collapsed",
    )
    if active_tab:
        st.session_state["teacher_active_section"] = active_tab

    active_section = st.session_state["teacher_active_section"]

    # =========================================================================
    # RENDER ACTIVE SECTION
    # =========================================================================
    if active_section == "Overview":
        _render_overview_section()
    elif active_section == "My Subjects":
        _render_subjects_section()
    elif active_section == "Take Attendance":
        _render_take_attendance_section()
    elif active_section == "Attendance Review":
        _render_review_section()
    elif active_section == "Attendance History":
        _render_history_section()
    elif active_section == "Student Roster":
        _render_roster_section()

    st.write("")

if __name__ == "__main__":
    teacher_screen()
