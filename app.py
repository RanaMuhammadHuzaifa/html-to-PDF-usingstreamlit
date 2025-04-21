import streamlit as st
from weasyprint import HTML

st.set_page_config(page_title="HTML to PDF Converter", layout="centered")

st.title("📄 HTML to PDF Converter")
st.markdown("Paste your HTML code below and download the generated PDF!")

# HTML input area
html_input = st.text_area("Paste HTML here:", height=300)

# Convert and download
if st.button("Convert to PDF"):
    pdf_file = "converted.pdf"
    HTML(string=html_input).write_pdf(pdf_file)

    with open(pdf_file, "rb") as f:
        st.download_button("📥 Download PDF", f, file_name="converted.pdf", mime="application/pdf")
