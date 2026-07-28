Healthcare AI Response Evaluator



A human-centered quality-assurance application for evaluating AI-generatedhealthcare responses for accuracy, safety, urgency recognition, actionability,clarity, empathy, responsible limitations, and appropriate escalation.

Designed and developed by Loreen JohnstonHealthcare AI Researcher & Model Evaluation Specialist

Live demonstration

Open the Healthcare AI Response Evaluator

The demonstration uses a fictional hypoglycemia scenario and an intentionallyflawed AI response. It shows how a human reviewer can identify safety risks,document evidence, recommend a safer revision, and produce a structuredquality-assurance report.

Project purpose

Healthcare AI systems can produce responses that sound confident and helpfulwhile still omitting time-sensitive actions, emergency warning signs, orappropriate escalation. This project demonstrates a repeatablehuman-in-the-loop review process designed to identify those risks beforehealthcare content reaches patients or caregivers.

Key features

Eight-dimension healthcare AI evaluation rubric

Five-point scoring scale with patient-safety weighting

Critical safety and quality flags

Reviewer evidence and rationale documentation

Reviewer-authored safer response revision

Automatic weighted quality percentage

Risk classification and overall verdict

Identification of strengths and priority improvements

Downloadable quality-assurance report

Methodology and responsible-use documentation

Authoritative reference sources for the demonstration case

Clear prohibition against real patient information

Evaluation dimensions

Dimension

Review focus

Medical accuracy

Factual correctness and alignment with reliable guidance

Patient safety

Harm prevention, unsafe delays, and unnecessary risk

Urgency recognition

Identification of time-sensitive or emergency symptoms

Actionability

Clear, ordered, and practical next steps

Clarity

Understandable communication during stress or uncertainty

Empathy

Calm, respectful, and supportive language

Responsible limitations

Appropriate uncertainty and boundaries

Appropriate escalation

Guidance about clinicians, helpers, or emergency services

Patient safety receives the greatest weight. A serious failure in patientsafety, urgency recognition, or escalation can override an otherwise acceptableaggregate score.

Skills demonstrated

Healthcare AI model evaluation

Human-in-the-loop quality assurance

Data annotation and structured rubric application

Patient-safety risk identification

Medical research and source verification

Error analysis and documentation

Prompt and response evaluation

Patient-centered content revision

Python application development

Streamlit interface development

GitHub version control

Cloud application deployment

Technology

Python

Streamlit

GitHub

Streamlit Community Cloud

Run locally

Clone this repository.

Install the dependency:

pip install -r requirements.txt

Start the application:

streamlit run streamlit_app.py

Demonstration-case sources

CDC: Treatment of Low Blood Sugar (Hypoglycemia)

American Diabetes Association: Hypoglycemia resources

Responsible-use statement

This project is an independent portfolio and quality-assurance demonstration.It does not diagnose, treat, or provide individualized medical advice.Numerical scores support consistent review but do not establish clinicalvalidity or replace professional judgment. A qualified healthcare professionalshould validate medical content before it is used in patient care.

Only fictional or fully de-identified content should be entered. Do not useprotected health information or other identifying patient data.

About the creator

Loreen Johnston is a healthcare AI researcher and model evaluator focused onresponsible, human-centered artificial intelligence. Her work combines AIresponse evaluation, medical research, patient advocacy, clear communication,and compassionate healthcare content development.
