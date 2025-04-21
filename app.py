import streamlit as st
from xhtml2pdf import pisa

st.set_page_config(page_title="HTML to PDF Converter", layout="centered")

st.title("📄 HTML to PDF Converter")
st.markdown("Paste your HTML code below and download the generated PDF!")

# HTML input area
html_input = st.text_area("Paste HTML here:", height=300)

# Convert and download
if st.button("Convert to PDF"):
    pdf_file = "converted.pdf"
    with open(pdf_file, "wb") as f:
        pisa.CreatePDF(html_input, dest=f)

    with open(pdf_file, "rb") as f:
        st.download_button("📥 Download PDF", f, file_name="converted.pdf", mime="application/pdf")
