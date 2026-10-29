import streamlit as st
from src.styles.theme import apply_theme, render_html

# =============================================================================
# SAMPLE DATA (ILLUSTRATIVE DEMO DATA)
# =============================================================================
SAMPLE_STUDENT = {
    "name": "Alex Morgan",
    "id": "STU-2026-0814",
    "email": "alex.morgan@univ.edu",
    "department": "Computer Science & Engineering",
    "program": "B.Tech Computer Engineering",
    "year": "Year 3 • Semester 5",
    "term": "Fall Term 2026",
    "advisor": "Dr. K. S. Sharma",
    "status": "Active / Registered",
}

SAMPLE_SUBJECTS = [
    {
        "code": "CS501",
        "name": "Artificial Intelligence",
        "faculty": "Prof. Ramesh Kulkarni",
        "attended": 23,
        "total": 25,
        "percentage": 92.0,
        "status": "On Track",
        "status_class": "badge-matched",
        "progress_color": "#22D3EE",
        "next_class": "Tomorrow, 10:00 AM • Hall B-204",
    },
    {
        "code": "CS502",
        "name": "Database Management Systems",
        "faculty": "Dr. Sneha Mehta",
        "attended": 21,
        "total": 25,
        "percentage": 84.0,
        "status": "Good",
        "status_class": "badge-matched",
        "progress_color": "#8B5CF6",
        "next_class": "Thursday, 02:00 PM • Lab 3",
    },
    {
        "code": "CS503",
        "name": "Operating Systems",
        "faculty": "Prof. Amit Joshi",
        "attended": 22,
        "total": 25,
        "percentage": 88.0,
        "status": "On Track",
        "status_class": "badge-matched",
        "progress_color": "#22D3EE",
        "next_class": "Friday, 11:30 AM • Room C-102",
    },
    {
        "code": "CS504",
        "name": "Computer Networks",
        "faculty": "Dr. Vikram Rao",
        "attended": 19,
        "total": 25,
        "percentage": 76.0,
        "status": "Attention Needed",
        "status_class": "badge-review",
        "progress_color": "#F59E0B",
        "next_class": "Monday, 09:00 AM • Room B-105",
    },
]

SAMPLE_ATTENDANCE_RECORDS = [
    {
        "date": "2026-10-28",
        "subject": "Artificial Intelligence",
        "session": "Lecture 25: ResNet Architectures",
        "mode": "Classroom Photo AI",
        "status": "Present",
    },
    {
        "date": "2026-10-27",
        "subject": "Database Management Systems",
        "session": "Lecture 23: B-Tree Index Optimization",
        "mode": "Classroom Photo AI",
        "status": "Present",
    },
    {
        "date": "2026-10-26",
        "subject": "Computer Networks",
        "session": "Lab 12: TCP Flow & Congestion Control",
        "mode": "Voice Biometrics",
        "status": "Absent",
    },
    {
        "date": "2026-10-25",
        "subject": "Operating Systems",
        "session": "Lecture 24: Virtual Memory Management",
        "mode": "Classroom Photo AI",
        "status": "Present",
    },
    {
        "date": "2026-10-24",
        "subject": "Artificial Intelligence",
        "session": "Lab 11: PyTorch Model Training",
        "mode": "Voice Biometrics",
        "status": "Present",
    },
    {
        "date": "2026-10-23",
        "subject": "Computer Networks",
        "session": "Lecture 21: BGP Routing & Subnetting",
        "mode": "Classroom Photo AI",
        "status": "Pending Review",
    },
    {
        "date": "2026-10-21",
        "subject": "Database Management Systems",
        "session": "Lecture 22: ACID Transaction Locks",
        "mode": "Classroom Photo AI",
        "status": "Present",
    },
    {
        "date": "2026-10-20",
        "subject": "Operating Systems",
        "session": "Lecture 23: Banker's Deadlock Avoidance",
        "mode": "Classroom Photo AI",
        "status": "Present",
    },
    {
        "date": "2026-10-18",
        "subject": "Computer Networks",
        "session": "Lecture 20: Link Layer Framing & CRC",
        "mode": "Classroom Photo AI",
        "status": "Absent",
    },
    {
        "date": "2026-10-17",
        "subject": "Artificial Intelligence",
        "session": "Lecture 24: Convolutional Neural Networks",
        "mode": "Classroom Photo AI",
        "status": "Present",
    },
    {
        "date": "2026-10-16",
        "subject": "Operating Systems",
        "session": "Lab 10: POSIX Threads & Semaphores",
        "mode": "Voice Biometrics",
        "status": "Present",
    },
    {
        "date": "2026-10-15",
        "subject": "Database Management Systems",
        "session": "Lab 10: PostgreSQL Query EXPLAIN Plans",
        "mode": "Voice Biometrics",
        "status": "Present",
    },
]

# =============================================================================
# MODAL DIALOG: JOIN SUBJECT
# =============================================================================
@st.dialog("Join a Course Subject")
def join_subject_dialog():
    render_html(
        """
        <div style="font-size: 0.88rem; color: #A7B0C0; margin-bottom: 12px; line-height: 1.45;">
            Enter the unique course enrollment token or invitation link provided by your professor to request registration.
        </div>
        """
    )
    code_input = st.text_input(
        "Subject Invitation Code",
        placeholder="e.g. CS505-S26 or https://attendai.edu/join/CS505",
        key="dlg_subject_code_val",
    )
    st.caption("Verification check is local. Database enrollment will connect via Supabase in a future step.")

    def _on_close_join_dialog():
        st.session_state["show_join_dialog"] = False

    col_submit, col_cancel = st.columns([1, 1])
    with col_submit:
        if st.button("Submit Code", type="primary", use_container_width=True, key="btn_dlg_submit"):
            if not code_input.strip():
                st.error("Please enter a valid subject code or invitation link.")
            else:
                st.success(f"Format check passed for '{code_input.strip().upper()}'.")
                st.info("Demo Mode: Real student enrollment requires Supabase authentication and database connection, which will be integrated in a future step.")
    with col_cancel:
        st.button("Close", use_container_width=True, key="btn_dlg_close", on_click=_on_close_join_dialog)

# =============================================================================
# SECTION RENDERERS
# =============================================================================
def _render_overview_section():
    """Renders the balanced 4-panel overview metrics and summary previews."""
    # 1. Four Summary Metric Panels
    render_html(
        """
        <div class="metrics-grid">
            <div class="metric-panel">
                <div class="metric-panel-header">
                    <span class="metric-panel-label">Enrolled Subjects</span>
                    <div class="metric-panel-icon" style="background: rgba(34, 211, 238, 0.1);">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block;">
                            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
                            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
                        </svg>
                    </div>
                </div>
                <div class="metric-panel-value">4</div>
                <div class="metric-panel-desc">Active courses this semester</div>
            </div>

            <div class="metric-panel">
                <div class="metric-panel-header">
                    <span class="metric-panel-label">Overall Attendance</span>
                    <div class="metric-panel-icon" style="background: rgba(16, 185, 129, 0.1);">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#34D399" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block;">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                            <polyline points="22 4 12 14.01 9 11.01"/>
                        </svg>
                    </div>
                </div>
                <div class="metric-panel-value" style="color: #34D399;">85.0%</div>
                <div class="metric-panel-desc">+10.0% above 75% cutoff</div>
            </div>

            <div class="metric-panel">
                <div class="metric-panel-header">
                    <span class="metric-panel-label">Classes Attended</span>
                    <div class="metric-panel-icon" style="background: rgba(139, 92, 246, 0.1);">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block;">
                            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                            <line x1="16" y1="2" x2="16" y2="6"/>
                            <line x1="8" y1="2" x2="8" y2="6"/>
                            <line x1="3" y1="10" x2="21" y2="10"/>
                        </svg>
                    </div>
                </div>
                <div class="metric-panel-value">85</div>
                <div class="metric-panel-desc">Verified present sessions</div>
            </div>

            <div class="metric-panel">
                <div class="metric-panel-header">
                    <span class="metric-panel-label">Classes Missed</span>
                    <div class="metric-panel-icon" style="background: rgba(245, 158, 11, 0.1);">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FBBF24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block;">
                            <circle cx="12" cy="12" r="10"/>
                            <line x1="12" y1="8" x2="12" y2="12"/>
                            <line x1="12" y1="16" x2="12.01" y2="16"/>
                        </svg>
                    </div>
                </div>
                <div class="metric-panel-value" style="color: #CBD5E1;">15</div>
                <div class="metric-panel-desc">Across all 4 courses</div>
            </div>
        </div>
        """
    )

    # 2. Advisory Compliance Banner
    render_html(
        """
        <div class="advisory-bar">
            <div style="display: flex; align-items: center; gap: 10px;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: block; flex-shrink: 0;">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                </svg>
                <span style="color: #F8FAFC; font-weight: 600;">Academic Good Standing:</span>
                <span style="color: #A7B0C0;">Cumulative attendance (85.0%) satisfies university examination eligibility threshold (&ge; 75%).</span>
            </div>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.74rem; color: #22D3EE;">100 Sessions Recorded</span>
        </div>
        """
    )

    # 3. Two-Column Dashboard Snapshot
    col_ov_left, col_ov_right = st.columns([6, 6])

    with col_ov_left:
        render_html(
            """
            <div style="background: #111A30; border: 1px solid #1E2A4A; border-radius: 10px; padding: 18px 20px; height: 100%;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; border-bottom: 1px solid #1E2A4A; padding-bottom: 8px;">
                    <span style="font-size: 0.95rem; font-weight: 700; color: #F8FAFC;">Subject Attendance Snapshot</span>
                    <span style="font-size: 0.72rem; font-family: 'JetBrains Mono', monospace; color: #CBD5E1;">4 SUBJECTS</span>
                </div>
            """
        )

        for subj in SAMPLE_SUBJECTS:
            render_html(
                f"""
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.84rem; margin-bottom: 3px;">
                        <span style="color: #F8FAFC; font-weight: 600;">{subj['name']} <span style="font-family: 'JetBrains Mono', monospace; color: #A7B0C0; font-size: 0.75rem;">({subj['code']})</span></span>
                        <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: {subj['progress_color']};">{subj['percentage']}%</span>
                    </div>
                    <div class="progress-track">
                        <div class="progress-bar-fill" style="width: {subj['percentage']}%; background: {subj['progress_color']};"></div>
                    </div>
                </div>
                """
            )

        render_html(
            """
                <div style="font-size: 0.75rem; color: #A7B0C0; margin-top: 14px; text-align: right;">
                    * Navigate to "My Subjects" for full details or course enrollment.
                </div>
            </div>
            """
        )

    with col_ov_right:
        render_html(
            """
            <div style="background: #111A30; border: 1px solid #1E2A4A; border-radius: 10px; padding: 18px 20px; height: 100%;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; border-bottom: 1px solid #1E2A4A; padding-bottom: 8px;">
                    <span style="font-size: 0.95rem; font-weight: 700; color: #F8FAFC;">Recent Attendance Events</span>
                    <span style="font-size: 0.72rem; font-family: 'JetBrains Mono', monospace; color: #22D3EE;">LATEST LOGS</span>
                </div>
            """
        )

        for rec in SAMPLE_ATTENDANCE_RECORDS[:4]:
            status_style = "status-present" if rec["status"] == "Present" else ("status-absent" if rec["status"] == "Absent" else "status-pending")
            render_html(
                f"""
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid #1E2A4A; font-size: 0.82rem;">
                    <div>
                        <div style="color: #F8FAFC; font-weight: 600;">{rec['subject']}</div>
                        <div style="color: #A7B0C0; font-size: 0.74rem;">{rec['date']} &bull; {rec['mode']}</div>
                    </div>
                    <span class="{status_style}">{rec['status']}</span>
                </div>
                """
            )

        render_html(
            """
                <div style="font-size: 0.75rem; color: #A7B0C0; margin-top: 14px; text-align: right;">
                    * Navigate to "Attendance History" for full record filtering.
                </div>
            </div>
            """
        )

def _render_subjects_section():
    """Renders the compact list of enrolled subjects and Join Subject button."""
    col_hdr_left, col_hdr_right = st.columns([8, 4], vertical_alignment="center")
    with col_hdr_left:
        render_html(
            """
            <div style="margin-bottom: 8px;">
                <div class="section-tag">CURRICULUM ROSTER</div>
                <div style="font-size: 1.35rem; font-weight: 700; color: #F8FAFC;">My Enrolled Subjects</div>
                <div style="font-size: 0.85rem; color: #A7B0C0;">Active registered courses for Fall Term 2026. Minimum attendance requirement: 75.0%.</div>
            </div>
            """
        )
    with col_hdr_right:
        if st.button("+ Join Subject", type="primary", use_container_width=True, key="btn_open_join_dialog"):
            st.session_state["show_join_dialog"] = True

    if st.session_state.get("show_join_dialog", False):
        join_subject_dialog()

    # Subject Cards List
    for subj in SAMPLE_SUBJECTS:
        render_html(
            f"""
            <div class="subject-row-card">
                <div>
                    <span class="subject-code-tag">{subj['code']}</span>
                    <div class="subject-title">{subj['name']}</div>
                    <div class="subject-faculty">{subj['faculty']}</div>
                </div>

                <div>
                    <div style="font-size: 0.72rem; color: #A7B0C0; text-transform: uppercase; font-family: 'JetBrains Mono', monospace;">Attended Classes</div>
                    <div style="font-size: 1.15rem; font-weight: 800; color: #F8FAFC; margin-top: 2px;">
                        {subj['attended']} <span style="font-size: 0.82rem; color: #A7B0C0; font-weight: 500;">/ {subj['total']} sessions</span>
                    </div>
                    <div style="font-size: 0.75rem; color: #A7B0C0; margin-top: 2px;">Missed: {subj['total'] - subj['attended']} classes</div>
                </div>

                <div>
                    <div style="display: flex; justify-content: space-between; font-size: 0.78rem; margin-bottom: 2px;">
                        <span style="font-family: 'JetBrains Mono', monospace; color: #A7B0C0;">Attendance</span>
                        <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: {subj['progress_color']};">{subj['percentage']}%</span>
                    </div>
                    <div class="progress-track">
                        <div class="progress-bar-fill" style="width: {subj['percentage']}%; background: {subj['progress_color']};"></div>
                    </div>
                </div>

                <div style="text-align: right;">
                    <span class="{subj['status_class']}">{subj['status']}</span>
                    <div style="font-size: 0.73rem; color: #A7B0C0; margin-top: 6px;">{subj['next_class']}</div>
                </div>
            </div>
            """
        )

    render_html(
        """
        <div style="background: #111A30; border: 1px dashed #1E2A4A; border-radius: 8px; padding: 12px 16px; margin-top: 14px; font-size: 0.78rem; color: #A7B0C0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
            <span>Need to add an elective or lab? Click "+ Join Subject" above to submit your instructor course invitation code.</span>
            <span style="color: #22D3EE; font-family: 'JetBrains Mono', monospace;">SUPABASE DB SYNC PENDING</span>
        </div>
        """
    )

def _render_history_section():
    """Renders attendance records with working subject and status filters."""
    render_html(
        """
        <div style="margin-bottom: 12px;">
            <div class="section-tag">VERIFICATION LOGS</div>
            <div style="font-size: 1.35rem; font-weight: 700; color: #F8FAFC;">Attendance History</div>
            <div style="font-size: 0.85rem; color: #A7B0C0;">Session audit trail displaying timestamp, classroom verification modality, and confirmed status.</div>
        </div>
        """
    )

    # Local Interactive Filters
    subject_options = ["All Subjects", "Artificial Intelligence", "Database Management Systems", "Operating Systems", "Computer Networks"]
    status_options = ["All Statuses", "Present", "Absent", "Pending Review"]

    def _reset_history_filters():
        st.session_state["hist_filter_subj"] = "All Subjects"
        st.session_state["hist_filter_status"] = "All Statuses"

    col_f1, col_f2, col_f3 = st.columns([4, 4, 4])
    with col_f1:
        selected_subject = st.selectbox("Subject Filter", options=subject_options, key="hist_filter_subj")
    with col_f2:
        selected_status = st.selectbox("Status Filter", options=status_options, key="hist_filter_status")
    with col_f3:
        st.write("")
        st.write("")
        st.button("Reset Filters", use_container_width=True, key="btn_reset_filters", on_click=_reset_history_filters)

    # Filter evaluation
    filtered_records = []
    for rec in SAMPLE_ATTENDANCE_RECORDS:
        match_subject = (selected_subject == "All Subjects") or (rec["subject"] == selected_subject)
        match_status = (selected_status == "All Statuses") or (rec["status"] == selected_status)
        if match_subject and match_status:
            filtered_records.append(rec)

    # Result count indicator
    render_html(
        f"""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; font-size: 0.78rem; color: #A7B0C0;">
            <span>Showing <b style="color: #F8FAFC;">{len(filtered_records)}</b> of {len(SAMPLE_ATTENDANCE_RECORDS)} recorded sessions</span>
            <span style="font-family: 'JetBrains Mono', monospace; color: #22D3EE;">ACTIVE FILTERS: {selected_subject} &bull; {selected_status}</span>
        </div>
        """
    )

    # Responsive Table or Empty State
    if filtered_records:
        render_html(
            """
            <div class="history-table-container">
                <div class="history-table">
                    <div class="history-row history-header">
                        <div>DATE</div>
                        <div>SUBJECT</div>
                        <div>SESSION / TOPIC</div>
                        <div>VERIFICATION MODE</div>
                        <div>STATUS</div>
                    </div>
            """
        )

        for rec in filtered_records:
            status_style = "status-present" if rec["status"] == "Present" else ("status-absent" if rec["status"] == "Absent" else "status-pending")
            render_html(
                f"""
                <div class="history-row">
                    <div style="font-family: 'JetBrains Mono', monospace; color: #CBD5E1;">{rec['date']}</div>
                    <div style="color: #F8FAFC; font-weight: 600;">{rec['subject']}</div>
                    <div style="color: #A7B0C0;">{rec['session']}</div>
                    <div style="color: #CBD5E1; font-size: 0.78rem;">
                        <span style="color: #22D3EE;">&bull;</span> {rec['mode']}
                    </div>
                    <div><span class="{status_style}">{rec['status']}</span></div>
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
        # Sensible Empty State
        render_html(
            f"""
            <div style="background: #111A30; border: 1px dashed #1E2A4A; border-radius: 10px; padding: 42px 20px; text-align: center; color: #A7B0C0; margin-top: 10px;">
                <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#A7B0C0" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" style="display: block; margin: 0 auto 12px auto;">
                    <circle cx="11" cy="11" r="8"/>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"/>
                </svg>
                <div style="font-size: 1.05rem; font-weight: 700; color: #F8FAFC; margin-bottom: 6px;">No Matching Attendance Records</div>
                <div style="font-size: 0.84rem; max-width: 480px; margin: 0 auto 12px auto; line-height: 1.45;">
                    No recorded sessions match the filters: <b>"{selected_subject}"</b> with status <b>"{selected_status}"</b>.
                </div>
                <div style="font-size: 0.78rem; color: #64748B;">
                    Try clicking "Reset Filters" above to display all 12 sample course records.
                </div>
            </div>
            """
        )

def _render_profile_section():
    """Renders student profile information and biometric registration status."""
    render_html(
        """
        <div style="margin-bottom: 12px;">
            <div class="section-tag">INSTITUTIONAL PROFILE</div>
            <div style="font-size: 1.35rem; font-weight: 700; color: #F8FAFC;">My Profile & Biometric Status</div>
            <div style="font-size: 0.85rem; color: #A7B0C0;">Official student registration data and biometric feature template enrollment status.</div>
        </div>
        """
    )

    col_prof_left, col_prof_right = st.columns([6, 6])

    with col_prof_left:
        # Academic Credentials Card
        render_html(
            f"""
            <div class="profile-card">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1E2A4A; padding-bottom: 10px; margin-bottom: 16px;">
                    <span style="font-size: 0.95rem; font-weight: 700; color: #F8FAFC;">Academic Credentials</span>
                    <span class="badge-demo"><span class="status-dot-amber"></span> SAMPLE DATA</span>
                </div>

                <div class="profile-grid">
                    <div>
                        <div class="profile-field-label">Student Name</div>
                        <div class="profile-field-val">{SAMPLE_STUDENT['name']}</div>
                    </div>
                    <div>
                        <div class="profile-field-label">Student ID</div>
                        <div class="profile-field-val" style="font-family: 'JetBrains Mono', monospace; color: #22D3EE;">{SAMPLE_STUDENT['id']}</div>
                    </div>
                    <div>
                        <div class="profile-field-label">Department</div>
                        <div class="profile-field-val">{SAMPLE_STUDENT['department']}</div>
                    </div>
                    <div>
                        <div class="profile-field-label">Academic Program</div>
                        <div class="profile-field-val">{SAMPLE_STUDENT['program']}</div>
                    </div>
                    <div>
                        <div class="profile-field-label">Academic Standing</div>
                        <div class="profile-field-val">{SAMPLE_STUDENT['year']} ({SAMPLE_STUDENT['term']})</div>
                    </div>
                    <div>
                        <div class="profile-field-label">Institutional Email</div>
                        <div class="profile-field-val" style="font-family: 'JetBrains Mono', monospace; font-size: 0.84rem; color: #CBD5E1;">{SAMPLE_STUDENT['email']}</div>
                    </div>
                    <div>
                        <div class="profile-field-label">Faculty Advisor</div>
                        <div class="profile-field-val">{SAMPLE_STUDENT['advisor']}</div>
                    </div>
                    <div>
                        <div class="profile-field-label">Registration Status</div>
                        <div class="profile-field-val" style="color: #34D399;">{SAMPLE_STUDENT['status']}</div>
                    </div>
                </div>
            </div>
            """
        )

    with col_prof_right:
        # Biometric Registration Status Panel
        render_html(
            """
            <div class="profile-card">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1E2A4A; padding-bottom: 10px; margin-bottom: 16px;">
                    <span style="font-size: 0.95rem; font-weight: 700; color: #F8FAFC;">Biometric Enrollment Status</span>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #22D3EE;">AI PIPELINE MOCK</span>
                </div>

                <!-- Face Template -->
                <div class="biometric-panel">
                    <div>
                        <div style="font-weight: 700; color: #F8FAFC; font-size: 0.88rem; display: flex; align-items: center; gap: 6px;">
                            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="12" cy="12" r="10"/>
                                <circle cx="12" cy="10" r="3"/>
                                <path d="M7 20.662V19a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v1.662"/>
                            </svg>
                            <span>Face Recognition Reference Template</span>
                        </div>
                        <div style="font-size: 0.74rem; color: #A7B0C0; margin-top: 3px;">
                            128D Landmark Embedding Vector &bull; Enrolled Sep 15, 2026
                        </div>
                    </div>
                    <span class="badge-matched">Enrolled (Active)</span>
                </div>

                <!-- Voiceprint Template -->
                <div class="biometric-panel">
                    <div>
                        <div style="font-weight: 700; color: #F8FAFC; font-size: 0.88rem; display: flex; align-items: center; gap: 6px;">
                            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
                                <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
                                <line x1="12" y1="19" x2="12" y2="23"/>
                                <line x1="8" y1="23" x2="16" y2="23"/>
                            </svg>
                            <span>Voice Biometrics Template</span>
                        </div>
                        <div style="font-size: 0.74rem; color: #A7B0C0; margin-top: 3px;">
                            Agreed Passphrase: "Present for [Subject Code]" &bull; Enrolled Sep 16, 2026
                        </div>
                    </div>
                    <span class="badge-matched">Enrolled (Active)</span>
                </div>

                <!-- Privacy Standard Notice -->
                <div style="border-left: 3px solid #8B5CF6; padding-left: 10px; margin-top: 14px; font-size: 0.76rem; color: #A7B0C0; line-height: 1.45;">
                    <div style="color: #8B5CF6; font-weight: 700; text-transform: uppercase; margin-bottom: 2px;">Ethical AI Verification Policy</div>
                    Biometric templates are stored strictly as mathematical embeddings. Camera and microphone remain unactivated in demo mode. Unrecognized scans require explicit teacher verification.
                </div>
            </div>
            """
        )

# =============================================================================
# MAIN STUDENT SCREEN ENTRY POINT
# =============================================================================
def student_screen():
    # Apply centralized theme
    apply_theme()

    # Session State Initialization
    if "student_active_section" not in st.session_state:
        st.session_state["student_active_section"] = "Overview"
    if "student_sidebar_radio" not in st.session_state:
        st.session_state["student_sidebar_radio"] = st.session_state["student_active_section"]
    if "student_main_segment" not in st.session_state:
        st.session_state["student_main_segment"] = st.session_state["student_active_section"]

    sections = ["Overview", "My Subjects", "Attendance History", "My Profile"]

    # =========================================================================
    # SIDEBAR NAVIGATION
    # =========================================================================
    with st.sidebar:
        # Branding Header
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
                        <div style="font-size: 0.68rem; font-family: 'JetBrains Mono', monospace; color: #8B5CF6; font-weight: 700; letter-spacing: 0.06em;">STUDENT PORTAL</div>
                    </div>
                </div>
            </div>
            """
        )

        render_html(
            """
            <div style="font-size: 0.72rem; font-weight: 700; color: #A7B0C0; letter-spacing: 0.06em; text-transform: uppercase; font-family: 'JetBrains Mono', monospace; margin-bottom: 8px;">
                DASHBOARD SECTIONS
            </div>
            """
        )

        def on_sidebar_nav_change():
            st.session_state["student_active_section"] = st.session_state["student_sidebar_radio"]
            st.session_state["student_main_segment"] = st.session_state["student_sidebar_radio"]

        st.radio(
            "Student Portal Navigation",
            options=sections,
            key="student_sidebar_radio",
            on_change=on_sidebar_nav_change,
            label_visibility="collapsed",
        )

        # Quick Return to Home
        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        if st.button("← Return to Home", key="btn_return_home_sidebar", use_container_width=True):
            if "pages" in st.session_state and "Home" in st.session_state["pages"]:
                st.switch_page(st.session_state["pages"]["Home"])

        # Sidebar Status Card
        render_html(
            """
            <div style="margin-top: 24px; padding: 12px; background: #111A30; border: 1px solid #1E2A4A; border-radius: 8px; font-size: 0.72rem; color: #A7B0C0;">
                <div style="display: flex; align-items: center; gap: 6px; color: #22D3EE; font-weight: 700; margin-bottom: 4px;">
                    <span class="status-dot"></span>
                    <span>ACTIVE SESSION</span>
                </div>
                <div>Student: <span style="color: #F8FAFC; font-weight: 600;">Alex Morgan</span></div>
                <div>ID: <span style="font-family: 'JetBrains Mono', monospace; color: #CBD5E1;">STU-2026-0814</span></div>
                <div style="margin-top: 8px; padding-top: 8px; border-top: 1px solid #1E2A4A; font-size: 0.68rem; color: #64748B;">
                    * All student attendance records and metrics shown are illustrative placeholders.
                </div>
            </div>
            """
        )

    # =========================================================================
    # MAIN CONTENT AREA
    # =========================================================================

    # 1. Top Header Banner
    render_html(
        """
        <div class="student-header-box">
            <div class="student-profile-summary">
                <div class="student-avatar">AM</div>
                <div class="student-title-block">
                    <h2>Student Dashboard</h2>
                    <div class="student-subtitle">Welcome back, <b>Alex Morgan</b> &bull; ID: <span style="font-family: 'JetBrains Mono', monospace; color: #CBD5E1;">STU-2026-0814</span> &bull; Computer Science &amp; Engineering</div>
                </div>
            </div>
            <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
                <span class="badge-academic">B.Tech &bull; Year 3 &bull; Sem 5</span>
                <span class="badge-demo"><span class="status-dot" style="background-color: #FBBF24;"></span> DEMO DATA</span>
            </div>
        </div>
        """
    )

    # 2. In-Page Responsive Navigation Bar (Allows 1-click tab switching on mobile/tablet)
    def on_segmented_change():
        if st.session_state["student_main_segment"]:
            st.session_state["student_active_section"] = st.session_state["student_main_segment"]
            st.session_state["student_sidebar_radio"] = st.session_state["student_main_segment"]

    st.segmented_control(
        "Dashboard Section View",
        options=sections,
        key="student_main_segment",
        on_change=on_segmented_change,
        label_visibility="collapsed",
    )

    active_section = st.session_state["student_active_section"]

    # =========================================================================
    # RENDER ACTIVE SECTION
    # =========================================================================
    if active_section == "Overview":
        _render_overview_section()
    elif active_section == "My Subjects":
        _render_subjects_section()
    elif active_section == "Attendance History":
        _render_history_section()
    elif active_section == "My Profile":
        _render_profile_section()

    st.write("")

if __name__ == "__main__":
    student_screen()
