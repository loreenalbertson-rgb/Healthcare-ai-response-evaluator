import streamlit as st
import pandas as pd
from datetime import date, datetime
from io import StringIO

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Care Companion AI",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# PROFESSIONAL CUSTOM STYLING
# ---------------------------------------------------------

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'DM Sans', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at top right, rgba(181, 220, 214, 0.32), transparent 32%),
                linear-gradient(180deg, #f8fbfb 0%, #f3f8f7 100%);
        }

        .block-container {
            max-width: 1220px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        .hero {
            background:
                linear-gradient(135deg, rgba(38, 91, 85, 0.98), rgba(67, 124, 116, 0.94)),
                url('https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1600&q=80');
            background-size: cover;
            background-position: center;
            border-radius: 28px;
            padding: 3.5rem 3rem;
            color: white;
            box-shadow: 0 20px 50px rgba(35, 78, 73, 0.18);
            margin-bottom: 2rem;
        }

        .hero-eyebrow {
            display: inline-block;
            background: rgba(255, 255, 255, 0.16);
            border: 1px solid rgba(255, 255, 255, 0.24);
            padding: 0.45rem 0.8rem;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 600;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            margin-bottom: 1rem;
        }

        .hero-title {
            font-family: 'Playfair Display', serif;
            font-size: 3.5rem;
            line-height: 1.05;
            margin: 0;
            max-width: 760px;
        }

        .hero-subtitle {
            font-size: 1.12rem;
            line-height: 1.7;
            max-width: 720px;
            color: rgba(255, 255, 255, 0.88);
            margin-top: 1.25rem;
            margin-bottom: 1.5rem;
        }

        .hero-note {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.75);
        }

        .section-label {
            color: #3f7770;
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.45rem;
        }

        .section-title {
            font-family: 'Playfair Display', serif;
            color: #234f4a;
            font-size: 2.15rem;
            line-height: 1.2;
            margin-bottom: 0.6rem;
        }

        .section-description {
            color: #607571;
            line-height: 1.65;
            margin-bottom: 1.5rem;
        }

        .feature-card {
            height: 100%;
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid #dceae7;
            border-radius: 20px;
            padding: 1.5rem;
            box-shadow: 0 10px 30px rgba(35, 79, 74, 0.06);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .feature-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 16px 38px rgba(35, 79, 74, 0.11);
        }

        .feature-icon {
            width: 48px;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #e7f3f1;
            border-radius: 14px;
            font-size: 1.45rem;
            margin-bottom: 1rem;
        }

        .feature-card h3 {
            color: #285b55;
            margin-bottom: 0.5rem;
        }

        .feature-card p {
            color: #677b77;
            line-height: 1.6;
            margin-bottom: 0;
        }

        .metric-card {
            background: white;
            border: 1px solid #deebe8;
            border-radius: 18px;
            padding: 1.25rem;
            text-align: center;
            box-shadow: 0 8px 22px rgba(35, 79, 74, 0.05);
        }

        .metric-number {
            font-size: 2rem;
            font-weight: 700;
            color: #316b64;
            margin-bottom: 0.15rem;
        }

        .metric-label {
            color: #6b7e7a;
            font-size: 0.92rem;
        }

        .content-card {
            background: rgba(255, 255, 255, 0.94);
            border: 1px solid #dce9e7;
            border-radius: 22px;
            padding: 1.7rem;
            box-shadow: 0 12px 30px rgba(35, 79, 74, 0.06);
            margin-bottom: 1rem;
        }

        .result-card {
            background: #ffffff;
            border: 1px solid #d8e8e5;
            border-left: 6px solid #4f8e85;
            border-radius: 18px;
            padding: 1.5rem;
            margin-top: 1rem;
            box-shadow: 0 10px 28px rgba(35, 79, 74, 0.06);
        }

        .privacy-card {
            background: linear-gradient(135deg, #eef7f5, #f8fbfa);
            border: 1px solid #d5e7e3;
            border-radius: 18px;
            padding: 1.35rem;
            margin-top: 1rem;
        }

        .emergency-card {
            background: #fff5f5;
            border: 1px solid #f1d4d4;
            border-left: 6px solid #bf5f5f;
            border-radius: 16px;
            padding: 1.15rem 1.25rem;
            margin-top: 1.5rem;
            color: #6f3b3b;
        }

        .support-card {
            background: linear-gradient(135deg, #f7fbfa, #eef6f4);
            border: 1px solid #d9e8e5;
            border-radius: 20px;
            padding: 1.5rem;
            margin-bottom: 1rem;
        }

        .footer-card {
            background: #285b55;
            color: rgba(255, 255, 255, 0.82);
            border-radius: 20px;
            padding: 1.5rem;
            margin-top: 3rem;
            text-align: center;
        }

        .footer-card strong {
            color: white;
        }

        div[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #eaf4f2, #f4f8f7);
            border-right: 1px solid #d9e7e4;
        }

        div[data-testid="stSidebar"] .block-container {
            padding-top: 1.5rem;
        }

        .sidebar-brand {
            font-family: 'Playfair Display', serif;
            color: #285b55;
            font-size: 1.7rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }

        .sidebar-tagline {
            color: #6a7f7b;
            font-size: 0.88rem;
            line-height: 1.5;
            margin-bottom: 1.25rem;
        }

        .stButton > button {
            background: linear-gradient(135deg, #326f67, #4f8e85);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.65rem 1.1rem;
            font-weight: 600;
            box-shadow: 0 6px 18px rgba(50, 111, 103, 0.18);
        }

        .stButton > button:hover {
            background: linear-gradient(135deg, #285f58, #427c74);
            color: white;
            border: none;
        }

        .stDownloadButton > button {
            background: white;
            color: #326f67;
            border: 1px solid #8fb8b2;
            border-radius: 12px;
            font-weight: 600;
        }

        .stDownloadButton > button:hover {
            background: #eef7f5;
            color: #285f58;
            border: 1px solid #6d9f98;
        }

        .stTextInput input,
        .stTextArea textarea,
        .stDateInput input {
            border-radius: 12px;
        }

        h1, h2, h3 {
            color: #285b55;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "symptoms" not in st.session_state:
    st.session_state.symptoms = []

if "medications" not in st.session_state:
    st.session_state.medications = []

# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------

def create_plain_language_summary(medical_text: str) -> str:
    cleaned_text = medical_text.strip()

    return f"""
### Plain Language Review

**What this information may include**

This text may describe a diagnosis, test result, treatment plan, medical observation, or follow up recommendation.

**Information provided**

{cleaned_text}

**Important details to identify**

1. The main medical concern
2. Recommended next steps
3. Follow up appointments or testing
4. Medication instructions
5. Symptoms that should be monitored
6. Warning signs requiring urgent care

**Questions to ask the care team**

1. What is the most important takeaway from this information?
2. What should we do next?
3. What changes should we monitor?
4. Are there warning signs that require immediate care?
5. When should follow up occur?

**Recommended next step**

Review this information with a qualified healthcare professional who can explain how it applies to the individual patient.
"""


def generate_doctor_questions(
    concern: str,
    symptoms: str,
    goals: str,
) -> list[str]:

    questions = [
        "What are the most likely explanations for these symptoms or concerns?",
        "Are there tests or evaluations that may help clarify what is happening?",
        "What changes should we monitor at home?",
        "Which symptoms would require urgent or emergency care?",
        "What treatment or management options should we discuss?",
        "Could any medications be contributing to these changes?",
        "What should we expect before the next appointment?",
        "When should follow up care be scheduled?",
    ]

    if concern.strip():
        questions.insert(
            0,
            f"How should we understand this primary concern: {concern.strip()}?",
        )

    if symptoms.strip():
        questions.append(
            f"How might these observations affect the care plan: {symptoms.strip()}?"
        )

    if goals.strip():
        questions.append(
            f"What steps could help us work toward this goal: {goals.strip()}?"
        )

    return questions


def create_appointment_summary(
    patient_name: str,
    appointment_date: date,
    provider_name: str,
    main_concern: str,
    symptom_notes: str,
    medication_questions: str,
    changes_since_last_visit: str,
    caregiver_questions: str,
) -> str:

    return f"""
CARE COMPANION AI
APPOINTMENT PREPARATION SUMMARY

Patient
{patient_name or "Not provided"}

Provider or clinic
{provider_name or "Not provided"}

Appointment date
{appointment_date.strftime("%B %d, %Y")}

Prepared
{datetime.now().strftime("%B %d, %Y at %I:%M %p")}

PRIMARY CONCERN

{main_concern or "No primary concern entered."}

SYMPTOMS AND OBSERVATIONS

{symptom_notes or "No symptom notes entered."}

CHANGES SINCE THE LAST VISIT

{changes_since_last_visit or "No changes entered."}

MEDICATION QUESTIONS

{medication_questions or "No medication questions entered."}

QUESTIONS FOR THE CARE TEAM

{caregiver_questions or "No additional questions entered."}

IMPORTANT NOTICE

This summary was created for educational and organizational purposes.
It is not a diagnosis and does not replace professional medical care.
"""


def symptom_dataframe() -> pd.DataFrame:
    if not st.session_state.symptoms:
        return pd.DataFrame()

    return pd.DataFrame(st.session_state.symptoms)


def medication_dataframe() -> pd.DataFrame:
    if not st.session_state.medications:
        return pd.DataFrame()

    return pd.DataFrame(st.session_state.medications)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.markdown(
    """
    <div class="sidebar-brand">Care Companion AI</div>
    <div class="sidebar-tagline">
        A calm, organized space for caregivers navigating complex care.
    </div>
    """,
    unsafe_allow_html=True,
)

selected_tool = st.sidebar.radio(
    "Explore the toolkit",
    [
        "Home",
        "Medical Information Simplifier",
        "Doctor Question Generator",
        "Symptom Journal",
        "Medication Organizer",
        "Appointment Prep",
        "Caregiver Support",
        "About This Project",
    ],
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div class="privacy-card">
        <strong>Privacy minded design</strong>
        <p style="margin-bottom:0; margin-top:0.5rem; color:#607571;">
            This version does not use a permanent patient database.
            Information remains temporary within the active session.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.caption(
    "Educational and organizational support only. Not medical advice."
)

# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------

if selected_tool == "Home":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-eyebrow">Human centered healthcare technology</div>
            <h1 class="hero-title">Caregiving is complicated. Your information should not be.</h1>
            <p class="hero-subtitle">
                Care Companion AI helps caregivers organize symptoms, medications,
                medical notes, and appointment questions in one calm, supportive space.
            </p>
            <p class="hero-note">
                Designed to support better preparation and clearer conversations with healthcare professionals.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-label">Built for real caregiving</div>
        <div class="section-title">A more organized way to prepare, track, and advocate</div>
        <div class="section-description">
            Care Companion AI brings together practical tools that help families
            prepare for appointments and communicate important observations clearly.
        </div>
        """,
        unsafe_allow_html=True,
    )

    feature_col1, feature_col2, feature_col3 = st.columns(3)

    with feature_col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🌿</div>
                <h3>Understand information</h3>
                <p>
                    Organize medical notes and identify the questions that need clarification.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with feature_col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📝</div>
                <h3>Track meaningful changes</h3>
                <p>
                    Record symptoms, severity, timing, triggers, and caregiver observations.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with feature_col3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🩺</div>
                <h3>Prepare with confidence</h3>
                <p>
                    Build appointment summaries and thoughtful questions for the care team.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

    metrics = [
        ("7", "Caregiver tools"),
        ("1", "Organized workspace"),
        ("0", "Permanent records stored"),
        ("100%", "Caregiver focused"),
    ]

    for column, metric in zip(
        [metric_col1, metric_col2, metric_col3, metric_col4],
        metrics,
    ):
        with column:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-number">{metric[0]}</div>
                    <div class="metric-label">{metric[1]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        <div class="emergency-card">
            <strong>Emergency notice</strong><br>
            Care Companion AI is not an emergency service. Call 911 or seek immediate
            medical care for severe, sudden, or life threatening symptoms.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# MEDICAL INFORMATION SIMPLIFIER
# ---------------------------------------------------------

elif selected_tool == "Medical Information Simplifier":

    st.markdown(
        """
        <div class="section-label">Understand</div>
        <div class="section-title">Medical Information Simplifier</div>
        <div class="section-description">
            Organize complicated medical information into a clearer review format
            and identify important questions for the care team.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="content-card">', unsafe_allow_html=True)

    medical_text = st.text_area(
        "Paste medical information",
        height=280,
        placeholder=(
            "Paste a diagnosis description, discharge instruction, test explanation, "
            "visit note, or other medical information here."
        ),
    )

    sample_col, clear_col = st.columns([1, 1])

    with sample_col:
        if st.button("Use sample information"):
            st.session_state.sample_medical_text = (
                "The patient should continue current medication and schedule "
                "follow up testing in four weeks. Seek urgent care for sudden "
                "weakness, severe confusion, chest pain, or difficulty breathing."
            )

    with clear_col:
        if st.button("Clear text"):
            st.session_state.sample_medical_text = ""
            st.rerun()

    if "sample_medical_text" in st.session_state and not medical_text:
        medical_text = st.session_state.sample_medical_text

    if st.button("Create Plain Language Review", type="primary"):
        if not medical_text.strip():
            st.warning("Please enter medical information first.")
        else:
            summary = create_plain_language_summary(medical_text)

            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown(summary)
            st.markdown("</div>", unsafe_allow_html=True)

            st.download_button(
                "Download Review",
                data=summary,
                file_name="care_companion_plain_language_review.txt",
                mime="text/plain",
            )

            st.warning(
                "This tool organizes information but may miss important clinical context. "
                "Always confirm medical meaning with a qualified healthcare professional."
            )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# DOCTOR QUESTION GENERATOR
# ---------------------------------------------------------

elif selected_tool == "Doctor Question Generator":

    st.markdown(
        """
        <div class="section-label">Prepare</div>
        <div class="section-title">Doctor Question Generator</div>
        <div class="section-description">
            Turn caregiver concerns and observations into organized questions
            for a medical appointment.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="content-card">', unsafe_allow_html=True)

    concern = st.text_area(
        "Main diagnosis, concern, or topic",
        placeholder="Example: Increased sleepiness after a medication change",
    )

    symptoms = st.text_area(
        "Symptoms or observations",
        placeholder=(
            "Describe what you noticed, when it began, how often it occurs, "
            "and whether it is changing."
        ),
    )

    goals = st.text_area(
        "What do you hope to understand or accomplish?",
        placeholder="Example: Understand whether medication adjustments should be discussed",
    )

    if st.button("Generate Appointment Questions", type="primary"):
        if not concern.strip() and not symptoms.strip() and not goals.strip():
            st.warning("Please enter at least one concern, symptom, or goal.")
        else:
            questions = generate_doctor_questions(
                concern=concern,
                symptoms=symptoms,
                goals=goals,
            )

            question_text = "\n".join(
                f"{number}. {question}"
                for number, question in enumerate(questions, start=1)
            )

            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.subheader("Questions for the care team")

            for number, question in enumerate(questions, start=1):
                st.write(f"**{number}.** {question}")

            st.markdown("</div>", unsafe_allow_html=True)

            st.download_button(
                "Download Question List",
                data=question_text,
                file_name="care_companion_doctor_questions.txt",
                mime="text/plain",
            )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# SYMPTOM JOURNAL
# ---------------------------------------------------------

elif selected_tool == "Symptom Journal":

    st.markdown(
        """
        <div class="section-label">Track</div>
        <div class="section-title">Symptom Journal</div>
        <div class="section-description">
            Record changes in symptoms and observations so patterns are easier
            to review and communicate.
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("symptom_form"):
        col1, col2 = st.columns(2)

        with col1:
            symptom_date = st.date_input("Date", value=date.today())

            symptom_name = st.text_input(
                "Symptom or observation",
                placeholder="Example: Headache, nausea, fatigue, increased alertness",
            )

            severity = st.slider(
                "Severity",
                min_value=1,
                max_value=10,
                value=5,
            )

        with col2:
            timing = st.text_input(
                "Timing and duration",
                placeholder="Example: Began around 2 PM and lasted two hours",
            )

            possible_triggers = st.text_input(
                "Possible triggers or related events",
                placeholder="Example: Medication, meal, activity, or poor sleep",
            )

            notes = st.text_area(
                "Additional notes",
                placeholder="Include anything else that may help identify a pattern.",
            )

        submitted = st.form_submit_button("Add Symptom Entry")

        if submitted:
            if not symptom_name.strip():
                st.warning("Please enter a symptom or observation.")
            else:
                st.session_state.symptoms.append(
                    {
                        "Date": symptom_date.strftime("%Y-%m-%d"),
                        "Symptom": symptom_name,
                        "Severity": severity,
                        "Timing": timing,
                        "Possible Triggers": possible_triggers,
                        "Notes": notes,
                    }
                )

                st.success("Symptom entry added successfully.")

    symptom_df = symptom_dataframe()

    if not symptom_df.empty:
        st.subheader("Symptom history")
        st.dataframe(symptom_df, use_container_width=True, hide_index=True)

        csv_data = symptom_df.to_csv(index=False)

        download_col, clear_col = st.columns(2)

        with download_col:
            st.download_button(
                "Download Symptom Report",
                data=csv_data,
                file_name="care_companion_symptom_report.csv",
                mime="text/csv",
            )

        with clear_col:
            if st.button("Clear Symptom Journal"):
                st.session_state.symptoms = []
                st.rerun()
    else:
        st.info("No symptom entries have been added yet.")

# ---------------------------------------------------------
# MEDICATION ORGANIZER
# ---------------------------------------------------------

elif selected_tool == "Medication Organizer":

    st.markdown(
        """
        <div class="section-label">Organize</div>
        <div class="section-title">Medication Organizer</div>
        <div class="section-description">
            Build a temporary medication list with dosing information,
            purposes, and questions for the care team.
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("medication_form"):
        col1, col2 = st.columns(2)

        with col1:
            medication_name = st.text_input(
                "Medication name",
                placeholder="Example: Levetiracetam",
            )

            dose = st.text_input(
                "Dose",
                placeholder="Example: 500 mg",
            )

            schedule = st.text_input(
                "Schedule",
                placeholder="Example: Twice daily",
            )

        with col2:
            purpose = st.text_input(
                "Purpose",
                placeholder="Why is this medication being taken?",
            )

            prescribing_provider = st.text_input(
                "Prescribing provider",
                placeholder="Optional",
            )

            medication_notes = st.text_area(
                "Questions or observations",
                placeholder="Example: Increased sleepiness after the dose changed",
            )

        medication_submitted = st.form_submit_button("Add Medication")

        if medication_submitted:
            if not medication_name.strip():
                st.warning("Please enter a medication name.")
            else:
                st.session_state.medications.append(
                    {
                        "Medication": medication_name,
                        "Dose": dose,
                        "Schedule": schedule,
                        "Purpose": purpose,
                        "Provider": prescribing_provider,
                        "Questions or Observations": medication_notes,
                    }
                )

                st.success("Medication added successfully.")

    medication_df = medication_dataframe()

    if not medication_df.empty:
        st.subheader("Medication list")
        st.dataframe(medication_df, use_container_width=True, hide_index=True)

        medication_csv = medication_df.to_csv(index=False)

        download_col, clear_col = st.columns(2)

        with download_col:
            st.download_button(
                "Download Medication List",
                data=medication_csv,
                file_name="care_companion_medication_list.csv",
                mime="text/csv",
            )

        with clear_col:
            if st.button("Clear Medication List"):
                st.session_state.medications = []
                st.rerun()
    else:
        st.info("No medications have been added yet.")

# ---------------------------------------------------------
# APPOINTMENT PREP
# ---------------------------------------------------------

elif selected_tool == "Appointment Prep":

    st.markdown(
        """
        <div class="section-label">Advocate</div>
        <div class="section-title">Appointment Preparation</div>
        <div class="section-description">
            Bring your most important concerns, changes, and questions together
            in one downloadable summary.
        </div>
        """,
        unsafe_allow_html=True,
    )

    patient_col, provider_col = st.columns(2)

    with patient_col:
        patient_name = st.text_input("Patient name or initials")

    with provider_col:
        provider_name = st.text_input("Provider or clinic")

    appointment_date = st.date_input(
        "Appointment date",
        value=date.today(),
    )

    main_concern = st.text_area(
        "Primary concern",
        placeholder="What is the most important issue to discuss?",
    )

    symptom_notes = st.text_area(
        "Symptoms and observations",
        placeholder="Include timing, frequency, severity, and recent patterns.",
    )

    changes_since_last_visit = st.text_area(
        "Changes since the last visit",
        placeholder="Include improvements, declines, new symptoms, or care changes.",
    )

    medication_questions = st.text_area(
        "Medication questions",
        placeholder="Include side effects, missed doses, or questions about adjustments.",
    )

    caregiver_questions = st.text_area(
        "Additional questions for the care team",
        placeholder="List anything else you want to remember to ask.",
    )

    if st.button("Create Appointment Summary", type="primary"):
        summary = create_appointment_summary(
            patient_name=patient_name,
            appointment_date=appointment_date,
            provider_name=provider_name,
            main_concern=main_concern,
            symptom_notes=symptom_notes,
            medication_questions=medication_questions,
            changes_since_last_visit=changes_since_last_visit,
            caregiver_questions=caregiver_questions,
        )

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.text_area(
            "Prepared summary",
            value=summary,
            height=520,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        st.download_button(
            "Download Appointment Summary",
            data=summary,
            file_name="care_companion_appointment_summary.txt",
            mime="text/plain",
        )

# ---------------------------------------------------------
# CAREGIVER SUPPORT
# ---------------------------------------------------------

elif selected_tool == "Caregiver Support":

    st.markdown(
        """
        <div class="section-label">Support</div>
        <div class="section-title">Caregiver Check In</div>
        <div class="section-description">
            Caregiving requires attention, advocacy, organization, and emotional strength.
            Your needs matter too.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="support-card">
            <h3>You do not have to solve everything today.</h3>
            <p>
                Choose the next clear step. Write down what matters most.
                Ask for help where possible. Rest is part of caregiving too.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Today I have")

    st.checkbox("Had something to eat")
    st.checkbox("Had water")
    st.checkbox("Taken my own medication, if applicable")
    st.checkbox("Written down the most urgent task")
    st.checkbox("Asked someone for help where possible")
    st.checkbox("Taken at least one quiet moment for myself")

    st.info(
        "Caregiver stress is real. Reach out to a trusted person, healthcare "
        "professional, or local support resource when the weight feels too heavy."
    )

# ---------------------------------------------------------
# ABOUT
# ---------------------------------------------------------

elif selected_tool == "About This Project":

    st.markdown(
        """
        <div class="section-label">The mission</div>
        <div class="section-title">Technology that supports the human side of healthcare</div>
        <div class="section-description">
            Care Companion AI was created to explore how accessible technology
            can help caregivers feel more prepared, informed, and organized.
        </div>
        """,
        unsafe_allow_html=True,
    )

    about_col1, about_col2 = st.columns([1.2, 1])

    with about_col1:
        st.markdown(
            """
            <div class="content-card">
                <h3>Why this project exists</h3>
                <p>
                    Caregivers are often expected to remember symptoms, medication
                    changes, medical terminology, provider instructions, and important
                    questions during highly stressful moments.
                </p>
                <p>
                    Care Companion AI brings those tasks together in one calm workspace.
                    It is designed to support preparation and communication without
                    replacing the judgment of healthcare professionals.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with about_col2:
        st.markdown(
            """
            <div class="content-card">
                <h3>Created by Lori DeGandi</h3>
                <p>
                    Healthcare AI creator, researcher, caregiver advocate,
                    and accessible health content developer.
                </p>
                <p>
                    This project is part of a growing portfolio focused on
                    human centered healthcare technology.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="privacy-card">
            <strong>Current development status</strong>
            <p style="margin-bottom:0; margin-top:0.5rem;">
                This is an early portfolio version. Future development may include
                secure accounts, accessibility options, editable records, appointment
                history, and optional AI powered medical language support.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer-card">
        <strong>Care Companion AI</strong><br>
        Educational and organizational support for caregivers and families.<br><br>
        This application does not diagnose conditions, prescribe treatment,
        or replace qualified medical care.
    </div>
    """,
    unsafe_allow_html=True,
)
