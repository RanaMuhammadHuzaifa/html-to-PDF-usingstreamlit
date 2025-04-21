import streamlit as st
from xhtml2pdf import pisa

st.set_page_config(page_title="HTML to PDF Converter", layout="centered")

st.title("📄 HTML to PDF Converter")
st.markdown("You can either paste HTML code or upload an HTML file to convert it to PDF!")

# Option to paste HTML code
html_input = st.text_area("Paste HTML here:", height=300)

# Option to upload an HTML file
html_file = st.file_uploader("Or upload an HTML file", type=["html"])

# Check for either input
if html_input:
    html_to_convert = html_input
elif html_file:
    html_to_convert = html_file.read().decode("utf-8")
else:
    html_to_convert = None

# Convert and download
if st.button("Convert to PDF") and html_to_convert:
    pdf_file = "converted.pdf"
    with open(pdf_file, "wb") as f:
        pisa.CreatePDF(html_to_convert, dest=f)

    with open(pdf_file, "rb") as f:
        st.download_button("📥 Download PDF", f, file_name="converted.pdf", mime="application/pdf")
else:
    st.warning("Please paste HTML code or upload an HTML file to proceed.")
