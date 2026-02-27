import pdfplumber
import docx

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = " ".join([para.text for para in doc.paragraphs])
    return text
