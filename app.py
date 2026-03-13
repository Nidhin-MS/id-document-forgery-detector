import streamlit as st
from analyzer import analyze_document
from report_generator import generate_report
from PIL import Image

st.title("ID Document Forgery Detection Prototype")

uploaded_file =st.file_uploader("Upload ID Document",type=["jpg","jpeg","png"])

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Document")

    result=analyze_document(image)

    report=generate_report(result)

    st.subheader("Forgery Risk Report")
    st.json(report)