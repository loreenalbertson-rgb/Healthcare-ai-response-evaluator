import streamlit as st


st.set_page_config(
    page_title="Healthcare AI Response Evaluator",
    page_icon="🩺",
    layout="centered",
)

st.title("Healthcare AI Response Evaluator")
st.subheader("A human-centered healthcare AI quality review tool")

st.write(
    """
    This application evaluates AI-generated healthcare responses for
    accuracy, safety, clarity, empathy, and appropriate escalation.
    """
)

st.info(
    "Portfolio demonstration only. This tool does not provide medical advice "
    "or replace review by a qualified healthcare professional."
)

