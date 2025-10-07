import pdfplumber

def extract_text_from_pdf(file_path):
    """
    Extracts text from a given PDF file using pdfplumber.
    Returns the text in lowercase for easier analysis.
    """
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text.lower().strip()
