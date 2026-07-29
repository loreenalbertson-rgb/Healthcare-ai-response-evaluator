Healthcare AI Response Evaluator

Human-centered safety and communication quality assurance for AI-generated healthcare responses

The Healthcare AI Response Evaluator is a Python and Streamlit portfolio application that demonstrates a structured, human-in-the-loop process for reviewing AI-generated healthcare communication.

It evaluates responses across eight weighted dimensions:

Medical accuracy

Patient safety

Urgency recognition

Actionability

Clarity

Empathy

Responsible limitations

Appropriate escalation

Patient safety receives the greatest numerical weight. Critical failures in safety, urgency recognition, or escalation override an otherwise acceptable aggregate score.

Version 2.0 highlights

Professional multi-tab evaluation workspace

Four fictional safety-critical case studies

Weighted five-point evaluation rubric

Severity-labeled safety and quality taxonomy

Human-authored safer response revision

Side-by-side communication comparison

Readability and wording-pattern heuristics

Session-level QA analytics

Markdown and JSON report export

CSV analytics export

Responsible-use and methodology documentation

Clear prohibition against protected health information

Demonstration cases

Hypoglycemia with confusion

Possible stroke symptoms

Possible heart attack symptoms

Suicidal crisis with immediate risk

Each case includes an intentionally flawed AI response, documented reviewer rationale, a safer human-authored revision, and authoritative public guidance.

Skills demonstrated

Healthcare AI response evaluation

Human-in-the-loop quality assurance

Structured rubric and taxonomy design

Patient-safety risk identification

Data annotation

Error analysis

Medical source verification

Patient-centered content revision

Responsible AI design

Python

Streamlit

Pandas

GitHub version control

Cloud application deployment

Run locally

pip install -r requirements.txt
streamlit run streamlit_app.py

Deployment

Deploy streamlit_app.py from the repository root using Streamlit Community Cloud.

Responsible use

This project is an independent portfolio and quality-assurance demonstration. It does not diagnose, treat, prescribe, or provide individualized medical advice. Numerical scores support review consistency but do not establish clinical validity or replace professional judgment.

Only fictional or fully de-identified information should be entered. Do not enter protected health information or other identifying patient data. A qualified healthcare professional must validate medical content before it is used in patient care.

Creator

Loreen JohnstonHealthcare AI Researcher and Model Evaluation Specialist

Focused on responsible, human-centered artificial intelligence, patient-safety evaluation, medical research, accessible communication, and caregiver advocacy.
Only fictional or fully de-identified content should be entered. Do not useprotected health information or other identifying patient data.

About the creator

Loreen Johnston is a healthcare AI researcher and model evaluator focused onresponsible, human-centered artificial intelligence. Her work combines AIresponse evaluation, medical research, patient advocacy, clear communication,and compassionate healthcare content development.
