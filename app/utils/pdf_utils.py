# utils/pdf_utils.py
import fitz  # PyMuPDF

def extract_text_from_pdf(filepath):
    text = ""
    with fitz.open(filepath) as pdf:
        for page in pdf:
            text += page.get_text()
    return text